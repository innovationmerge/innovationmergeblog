## readme of the preditive-capture

- Author : innovationmerge
- Version: 1.0
- Descritption: Auto capture of photos when object detected

#### Requirements: 
- Python > 3.7
- `pip install cookiecutter`
- `pip install poetry`

#### Install the project using poetry
- Raspberry Pi
    - `cd preditive_capture`
    - `poetry install`

- Windows
    - `pip install poetry`
    - `cd preditive_capture`
    - `poetry add innovationmerge=1.1.2[windows]`

#### Detection 1 using MobileNet Pretrained Model
- Test with Image Detection
    - `poetry run python mobilenet_main.py`
- Detect objects using webcam
    - `poetry run python mobilenet_main_web_cam.py`
- Detect objects and save an image when object is detected
    - `poetry run python mobilenet_main_web_cam_save.py`

#### Detection 2 using SSD MobileNet Pretrained Model
- Test with Image Detection
    - `poetry run python ssd_main.py`
- Detect objects using webcam
    - `poetry run python ssd_main_web_cam.py`
- Detect objects and save an image when object is detected
    - `poetry run python ssd_main_web_cam_save.py`

#### Explore this project
- Visit [iNNovationMerge Blog](https://www.innovationmerge.com/2023/10/08/predictive-capture-tensorflow-raspberrypi/)