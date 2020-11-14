from pyAudioAnalysis import audioTrainTest as aT
c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_movie8class","svm")
for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')
"""
print(f'P({p_nam[0]}={p[0]})')
print(f'P({p_nam[1]}={p[1]})')
print(f'P({p_nam[2]}={p[2]})')
print(f'P({p_nam[3]}={p[3]})')
print(f'P({p_nam[4]}={p[4]})')
print(f'P({p_nam[5]}={p[5]})')
print(f'P({p_nam[6]}={p[6]})')
print(f'P({p_nam[7]}={p[7]})')
"""