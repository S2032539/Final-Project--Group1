import librosa
import librosa.display
import os
import matplotlib.pyplot as plt
import numpy as np
import dtw

audio_path = 'C:\\Animoji\\speech.wav'
y, sr = librosa.load(audio_path, sr=None)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
plt.figure()
plt.plot(np.tile(np.arange(pitches.shape[1]), [100, 1]).T, 
pitches[:100, :].T, '.')
print(plt.xlabel('samples', fontsize=18))
print(plt.ylabel('pitch (Hz)', fontsize=18))
print(plt.savefig("pitch_array_by_fps.png"))
print(pitches)