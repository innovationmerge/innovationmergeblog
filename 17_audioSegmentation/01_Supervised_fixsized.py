from pyAudioAnalysis import audioSegmentation as aS

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/svm_rbf_sm", "svm", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/svm_rbf_4class", "svm", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/svm_rbf_movie8class", "svm", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/svm_rbf_speaker_male_female", "svm", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/knn_sm", "knn", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/knn_4class", "knn", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/knn_movie8class", "knn", True, 'data/scottish.segments')

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/knn_speaker_male_female", "knn", True, 'data/scottish.segments')
