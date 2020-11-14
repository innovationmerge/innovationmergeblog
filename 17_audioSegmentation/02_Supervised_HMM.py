from pyAudioAnalysis import audioSegmentation as aS

aS.hmm_segmentation('data/scottish.wav', 'data/hmmRadioSM', True, 'data/scottish.segments')