from pyAudioAnalysis import audioTrainTest as aT
c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_4class","svm")
print(f'P({p_nam[0]}={p[0]})')
print(f'P({p_nam[1]}={p[1]})')
print(f'P({p_nam[2]}={p[2]})')
print(f'P({p_nam[3]}={p[3]})')
print()