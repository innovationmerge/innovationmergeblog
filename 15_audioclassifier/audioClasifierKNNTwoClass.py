from pyAudioAnalysis import audioTrainTest as aT
c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/knn_sm","knn")
for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')