import os
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw

y, sr = librosa.load('speech.wav')
y1, sr1 = librosa.load('speech - Anger1.wav')
print(y.shape)
mfccs = np.mean(librosa.feature.mfcc(y, n_mfcc=40, sr =sr).T, axis=0)
mfccs1 = np.mean(librosa.feature.mfcc(y1, n_mfcc=40, sr =sr1).T, axis=0)
#mfccs = np.mean(librosa.amplitude_to_db(y, ref=1.0, amin=1e-05, top_db=80.0).T, axis=0)
#mfccs1 = np.mean(librosa.amplitude_to_db(y1, ref=1.0, amin=1e-05, top_db=80.0).T, axis=0)

print("New mfcc feature voice values")
print(mfccs)
print("Trained mfcc feature voice values")
print(mfccs1)

distance = dtw.distance(mfccs, mfccs1)
print("Distance between training and input voice")
print(distance)

D = librosa.stft(y) # stft to y
S_db = librosa.amplitude_to_db(np.abs(D) , ref= np.max)

fig, ax = plt.subplots()
img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
ax.set(title='Spectogram:Using a logarithmic frequency axis')
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()

#dtw coding example
def dtw1(mfcc, mfcc1):
    mfcc_len = len(mfcc)
    mfcc1_len = len(mfcc1)

    cost = [[0 for i in range(mfcc1_len)] for i in range(mfcc1_len)]

    dis = []
    for i in range(mfcc_len):
        dis_row = []
        for j in range(mfcc1_len):
            dis_row.append(distance(mfcc[i],mfcc1[j]))
            dis.append(dis_row)
    return dis_row
    print("distance is"+ dis_row)






