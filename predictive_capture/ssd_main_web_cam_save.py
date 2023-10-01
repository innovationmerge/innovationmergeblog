import os
from preditive_capture.capture import detect_capture, WebCamObjectDetection
from preditive_capture.exceptions import PreditiveCaptureMethodException
from preditive_capture.logger import logger, log_init
from innovationmerge.src.utils.responses import save_detection_image, show_detection_image

cwd = os.getcwd()

# Edge models SSD
model_path = os.path.join(cwd, "models", "edge", "ssd_mobilenet_v3_large_coco_2020_01_14")
model_file_path = os.path.join(model_path, "model.tflite")
labels_path = os.path.join(model_path, "labels.txt")
model_type="ssd"

# Declare paths
input_image_path = os.path.join(cwd, "Input", "sample.jpg")
output_image_path = os.path.join(cwd, "Output", "sample.jpg")
output_path = os.path.join(cwd, "Output")
threshold = 0.6

if __name__ == "__main__":
    try:
        log_init()

        compute = "edge"
        print("Object detection started. Press 'q' to stop.")
        
        web_cam_detect = WebCamObjectDetection(compute, model_file_path, labels_path, output_path, 640, 480)
        web_cam_detect.web_cam_predict_save(threshold, model_type)
                
    except Exception as e:
        raise PreditiveCaptureMethodException(str(e))
