from innovationmerge import EdgeObjectDetectionTfLite
from innovationmerge.configurations.constants import DETECTION_RESPONSE_BB
from innovationmerge.src.utils.responses import load_labels, read_image
from innovationmerge.src.utils.responses import draw_detections
import cv2
from threading import Thread
from preditive_capture.exceptions import PreditiveCaptureMethodException

def detect_capture(model_path: str, labels_file_path: str, input_image_path: str, compute: str = "cpu", threshold: float = 0.1, model_type: str = "ssd"):
    labels = load_labels(labels_file_path)
    cv2_image = read_image(input_image_path)
    if compute == "edge":
        detect_objects = EdgeObjectDetectionTfLite(model_path)
        detection_result = detect_objects.detect(cv2_image, labels, threshold, model_type)
        return detection_result, cv2_image
    else:
        raise PreditiveCaptureMethodException("Only Edge models are supported currently")


class VideoStream:
    """Camera object that controls video streaming from the Picamera"""
    def __init__(self,resolution=(640,480),framerate=30):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        ret = self.stream.set(3,resolution[0])
        ret = self.stream.set(4,resolution[1])
            
        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

	# Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
	# Start the thread that reads frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
	# Return the most recent frame
        return self.frame

    def stop(self):
	# Indicate that the camera and thread should be stopped
        self.stopped = True

class WebCamObjectDetection():
    def __init__(self, model_path, labels_path, imW, imH) -> None:
        # Initialize video stream
        self.videostream = VideoStream(resolution=(imW,imH), framerate=30).start()
        self.detect_objects = EdgeObjectDetectionTfLite(model_path)
        self.labels = load_labels(labels_path)

    def web_cam_predict(self, threshold: float = 0.1, model_type: str = "ssd"):
        while True:
            # Start timer (for calculating frame rate)
            t1 = cv2.getTickCount()

            # Grab frame from video stream
            frame1 = self.videostream.read()
            # Acquire frame and resize to expected shape [1xHxWx3]
            frame = frame1.copy()
            
            detection_result = self.detect_objects.detect(cv2_image=frame, labels_list=self.labels, threshold=threshold, model_type=model_type)
            print("detections", detection_result)
            frame = draw_detections(detection_result, frame)

            # All the results have been drawn on the frame, so it's time to display it.
            cv2.imshow('Object detector', frame)

            # Press 'q' to quit
            if cv2.waitKey(1) == ord('q'):
                break

        # Clean up
        cv2.destroyAllWindows()
        self.videostream.stop()