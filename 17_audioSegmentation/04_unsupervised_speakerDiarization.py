from pyAudioAnalysis import audioSegmentation
num_speakers = 4
audioSegmentation.speaker_diarization("data/diarizationExample.wav", num_speakers, plot_res=True)


