# -*- coding: utf-8 -*-
class PreditiveCaptureException(Exception):
    """Base class for exceptions raised by preditive_capture  modules"""


class PreditiveCaptureMethodException(Exception):
    """Base class for exceptions raised by preditive_capture  modules"""
    def __init__(self, message):
        super().__init__(str(message))