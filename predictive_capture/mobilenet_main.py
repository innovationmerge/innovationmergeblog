import os
from preditive_capture.capture import detect_capture, WebCamObjectDetection
from preditive_capture.exceptions import PreditiveCaptureMethodException
from preditive_capture.logger import logger, log_init
from innovationmerge.src.utils.responses import save_detection_image, show_detection_image

cwd = os.getcwd()

# Edge models Mobilenet
model_path = os.path.join(cwd, "models", "edge", "mobilenet_v2_1.0_224_quant")
model_file_path = os.path.join(model_path, "model.tflite")
labels_path = os.path.join(model_path, "labels.txt")
model_type="mobilenet"

# Declare paths
input_image_path = os.path.join(cwd, "Input", "sample.jpg")
output_image_path = os.path.join(cwd, "Output", "sample.jpg")
threshold = 0.6

if __name__ == "__main__":
    try:
        log_init()

        compute = "edge"
        
        # Detect objects in the Image
        detection_result, cv2_image = detect_capture(model_file_path, labels_path, input_image_path, compute, threshold, model_type)

        # Save Detections as Image
        save_detection_image(detection_result, cv2_image, output_image_path, model_type)

        # Show Detections
        show_detection_image(cv2_image)

        logger.info("processing time is " + str(detection_result["processing_time"]))
    except Exception as e:
        raise PreditiveCaptureMethodException(str(e))
