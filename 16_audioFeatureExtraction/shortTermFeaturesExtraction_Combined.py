from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import matplotlib.pyplot as plt
import cv2
import numpy as np

def putTitleText(title):
    font_scale = 2
    font = cv2.FONT_HERSHEY_PLAIN

    # set the rectangle background to white
    rectangle_bgr = (0, 0, 0)
    # make a black image
    img = np.zeros((200, 1000))
    # set some text
    text = "Next: "+str(title)
    # get the width and height of the text box
    (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
    # set the text start position
    text_offset_x = 10
    text_offset_y = img.shape[0] - 150

    text_offset_x1 = 10
    text_offset_y1 = img.shape[0] - 25
    # make the coords of the box with a small padding of two pixels
    box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height - 2))
    cv2.rectangle(img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
    cv2.putText(img, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(255, 255, 255), thickness=1)
    cv2.putText(img, "iNNovationMerge", (text_offset_x1, text_offset_y1), font, fontScale=font_scale, color=(255, 255, 255), thickness=1)
    cv2.imshow("Now", img)
    cv2.waitKey(0)


[Fs, x] = audioBasicIO.read_audio_file("data/doremi.wav")
F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050*Fs, 0.025*Fs)
print(len(f_names))
for k in range(len(f_names)):
    if k == 0:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge')
        plt.savefig('images/106_3_zcrOutput.JPG')
        img1 = cv2.imread('images/106_3_zcrFormula.JPG')
        img2= cv2.imread('images/106_3_zcrOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('ZCR', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 1:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge')
        plt.savefig('images/106_4_energyOutput.JPG')
        img1 = cv2.imread('images/106_4_energyFormula.JPG')
        img2= cv2.imread('images/106_4_energyOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Energy', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 2:        
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_5_energyEntropyOutput.JPG')
        img2= cv2.imread('images/106_5_energyEntropyOutput.JPG')
        cv2.imshow('Entropy of Energy', img2)
        cv2.waitKey(3000)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 3:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_6_SpectralCentroidOutput.JPG')
        img1 = cv2.imread('images/106_6_SpectralCentroidFormula.JPG')
        img2= cv2.imread('images/106_6_SpectralCentroidOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Spectral Centroid', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 4:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_7_SpectralSpreadOutput.JPG')
        img1 = cv2.imread('images/106_7_SpectralSpreadFormula.JPG')
        img2= cv2.imread('images/106_7_SpectralSpreadOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Spectral Spread', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 5:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_8_SpectralEntropyOutput.JPG')
        img1 = cv2.imread('images/106_8_SpectralEntropyFormula.JPG')
        img2= cv2.imread('images/106_8_SpectralEntropyOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Spectral entropy', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 6:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_9_SpectralFluxOutput.JPG')
        img1 = cv2.imread('images/106_9_SpectralFluxFormula.JPG')
        img2= cv2.imread('images/106_9_SpectralFluxOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Spectral Flux', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 7:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_10_SpectralRolloffOutput.JPG')
        img1 = cv2.imread('images/106_10_SpectralRolloffFormula.JPG')
        img2= cv2.imread('images/106_10_SpectralRolloffOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Spectral rolloff', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 8:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_11_MFCCsOutput.JPG')
        img1 = cv2.imread('images/106_11_MFCCsFormula.JPG')
        img2= cv2.imread('images/106_11_MFCCsOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('MFCCs', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()     
    elif k == 21:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_12_ChromaVectorOutput.JPG')
        img2= cv2.imread('images/106_12_ChromaVectorOutput.JPG')
        cv2.waitKey(3000)
        cv2.imshow('Chroma Vector', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()     
    elif k == 33:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_13_ChromaDeviationOutput.JPG')
        img2= cv2.imread('images/106_13_ChromaDeviationOutput.JPG')
        cv2.waitKey(3000)
        cv2.imshow('Chroma Deviation', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()   
    else:
        putTitleText("Feature "+str(k+1)+" "+f_names[k])
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_100_Output.JPG')
        img2= cv2.imread('images/106_100_Output.JPG')
        cv2.waitKey(3000)
        cv2.imshow("Feature "+str(k+1)+" "+f_names[k], img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows() 




