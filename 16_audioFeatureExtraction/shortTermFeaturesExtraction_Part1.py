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
        putTitleText("Feature 1 - Zero Crossing Rate(ZCR)")
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_3_zcrOutput.JPG')
        img1 = cv2.imread('images/106_3_zcrFormula.JPG')
        img2= cv2.imread('images/106_3_zcrOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('ZCR', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 1:
        putTitleText("Feature 2 - Energy")
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_4_energyOutput.JPG')
        img1 = cv2.imread('images/106_4_energyFormula.JPG')
        img2= cv2.imread('images/106_4_energyOutput.JPG')
        cv2.imshow('Formula', img1)
        cv2.waitKey(3000)
        cv2.imshow('Energy', img2)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 2:        
        putTitleText("Feature 3 - Entropy of Energy")
        cv2.waitKey(1000)
        plt.subplot(1,1,1); plt.plot(F[k,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[k]) ; plt.title('iNNovationMerge');
        plt.savefig('images/106_5_energyEntropyOutput.JPG')
        img2= cv2.imread('images/106_5_energyEntropyOutput.JPG')
        cv2.imshow('Entropy of Energy', img2)
        cv2.waitKey(3000)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows()
    elif k == 3:
        putTitleText("Feature 4 - Spectral Centroid")
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

    else:
        break




