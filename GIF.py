import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('C:\\Animoji\\angry3.gif')

y, sr = librosa.load('speech.wav')
print(y.shape)
mfccs = librosa.feature.mfcc(y, n_mfcc=8, sr =sr)
print(mfccs)

D = librosa.stft(y) # stft to y
S_db = librosa.amplitude_to_db(np.abs(D) , ref= np.max)

fig, ax = plt.subplots()
img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
ax.set(title='Using a logarithmic frequency axis')
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()

root.mainloop()