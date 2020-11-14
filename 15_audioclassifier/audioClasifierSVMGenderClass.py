from pyAudioAnalysis import audioTrainTest as aT
c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_speaker_male_female","svm")
for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')