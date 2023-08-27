from sample import sample_func
from preditive_capture.logger import log_init


# Make sure to start function name with test
def test_sample_func():
    log_init()
    assert sample_func(1, 2) == 3
