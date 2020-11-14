from pyAudioAnalysis import audioTrainTest as aT
c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_sm","svm_rbf")
print(f'P({p_nam[0]}={p[0]})')
print(f'P({p_nam[1]}={p[1]})')
print()