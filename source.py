import tkinter as tk
import os
import speech_recognition as sr
from tkinter import *
import librosa.display
import numpy as np
from dtaidistance import dtw
import speech_recognition as sr_angry1
import speech_recognition as sr_angry2
import speech_recognition as sr_angry3
import speech_recognition as sr_disgust1
import speech_recognition as sr_disgust2
import speech_recognition as sr_disgust3

root = tk.Tk()
root.title("Animoji Evolution")

root.geometry('700x500')

Expression = {'angry', 'very angry', 'very very angry', 'is nasty', 'disgusting', 'so disgusting'}
def mfccrec():
    y, sr = librosa.load('speech.wav')
    y1, sr1 = librosa.load('speech - Anger1.wav')
    print(y.shape)
    mfccs = np.mean(librosa.feature.mfcc(y, n_mfcc=40, sr=sr).T, axis=0)
    mfccs1 = np.mean(librosa.feature.mfcc(y1, n_mfcc=40, sr=sr1).T, axis=0)

    print("New mfcc feature voice values")
    print(mfccs)
    print("Trained mfcc feature voice values")
    print(mfccs1)

    distance = dtw.distance(mfccs, mfccs1)
    print("Distance between training and input voice")
    print(distance)
def rec_voi():

    T.delete("1.0", tk.END)
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        with open('speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    y0, sr0 = librosa.load('speech.wav')
    y1, sr1 = librosa.load('speech - Anger1.wav')
    y2, sr2 = librosa.load('speech - Anger2.wav')
    y3, sr3 = librosa.load('speech - Anger3.wav')
    y4, sr4 = librosa.load('speech - Disgust1.wav')
    y5, sr5 = librosa.load('speech - Disgust2.wav')
    y6, sr6 = librosa.load('speech - Disgust3.wav')
    print(y0.shape)
    mfccs = np.mean(librosa.feature.mfcc(y0, n_mfcc=40, sr=sr0).T, axis=0)
    mfccs1 = np.mean(librosa.feature.mfcc(y1, n_mfcc=40, sr=sr1).T, axis=0)
    mfccs2 = np.mean(librosa.feature.mfcc(y2, n_mfcc=40, sr=sr2).T, axis=0)
    mfccs3 = np.mean(librosa.feature.mfcc(y3, n_mfcc=40, sr=sr3).T, axis=0)
    mfccs4 = np.mean(librosa.feature.mfcc(y4, n_mfcc=40, sr=sr4).T, axis=0)
    mfccs5 = np.mean(librosa.feature.mfcc(y5, n_mfcc=40, sr=sr5).T, axis=0)
    mfccs6 = np.mean(librosa.feature.mfcc(y6, n_mfcc=40, sr=sr6).T, axis=0)
    AUDIO_FILE = "speech - Anger1.wav"
    ra1 = sr_angry1.Recognizer()
    with sr_angry1.AudioFile(AUDIO_FILE) as source:
        audio1 = ra1.record(source)
        S1_text = ra1.recognize_google(audio1)
    AUDIO_FILE2 = "speech - Anger2.wav"
    ra2 = sr_angry2.Recognizer()
    with sr_angry2.AudioFile(AUDIO_FILE2) as source:
        audio2 = ra2.record(source)
        S2_text = ra2.recognize_google(audio2)
    AUDIO_FILE3 = "speech - Anger3.wav"
    ra3 = sr_angry3.Recognizer()
    with sr_angry3.AudioFile(AUDIO_FILE3) as source:
        audio3 = ra3.record(source)
        S3_text = ra3.recognize_google(audio3)
    AUDIO_FILE4 = "speech - Disgust1.wav"
    ra4 = sr_disgust1.Recognizer()
    with sr_disgust1.AudioFile(AUDIO_FILE4) as source:
        audio4 = ra4.record(source)
        S4_text = ra4.recognize_google(audio4)
    AUDIO_FILE5 = "speech - Disgust2.wav"
    ra5 = sr_disgust2.Recognizer()
    with sr_disgust2.AudioFile(AUDIO_FILE5) as source:
        audio5 = ra5.record(source)
        S5_text = ra5.recognize_google(audio5)
    AUDIO_FILE6 = "speech - Disgust3.wav"
    ra6 = sr_disgust3.Recognizer()
    with sr_disgust3.AudioFile(AUDIO_FILE6) as source:
        audio6 = ra6.record(source)
        S6_text = ra6.recognize_google(audio6)

    #anger1 distance
    distanceA1 = dtw.distance(mfccs, mfccs1)
    print("Distance between training Anger level 1 and input voice")
    print(distanceA1)
    # anger1 distance
    distanceA2 = dtw.distance(mfccs, mfccs2)
    print("Distance between training Anger level 2 and input voice")
    print(distanceA2)
    # anger1 distance
    distanceA3 = dtw.distance(mfccs, mfccs3)
    print("Distance between training Anger level 3 and input voice")
    print(distanceA3)

    distanceD1 = dtw.distance(mfccs, mfccs4)
    print("Distance between training Disgust level 1 and input voice")
    print(distanceD1)
    distanceD2 = dtw.distance(mfccs, mfccs4)
    print("Distance between training Disgust level 2 and input voice")
    print(distanceD2)
    distanceD3 = dtw.distance(mfccs, mfccs6)
    print("Distance between training Disgust level 3 and input voice")
    print(distanceD3)
    dmin = min(distanceA1, distanceA2, distanceA3)
    dmax = min(distanceA1, distanceA2, distanceA3)
    dmid = min(distanceA1, distanceA2, distanceA3)

    dgmin = min(distanceD1, distanceD2, distanceD3)
    dgmax = min(distanceD1, distanceD2, distanceD3)
    dgmid = min(distanceD1, distanceD2, distanceD3)

    try:
        S_text = r.recognize_google(audio)
        T.insert(tk.END, "{}".format(S_text))
        print("You Said:\n{}".format(S_text)) 
        if 'very very angry' in S_text and 'very very angry' in S3_text and dmax == distanceA3 and dmax < 40:
            print("Your emotion are anger level 3")
            os.system("anger3.py")
        elif 'very angry' in S_text and 'very angry' in S2_text and dmid == distanceA3 and dmid < 40:
            print("Your emotion are anger level 2")
            os.system('anger2.py')
        elif 'angry' in S_text and 'angry' in S1_text and dmin == distanceA1 and dmin < 40:
            print("Your emotion are anger level 1")
            os.system('anger1.py')
        elif 'is so disgusting' in S_text and 'is so disgusting' in S6_text and dgmax == distanceD3 and dmax < 40:
            print("Your emotion are disgust level 3")
            os.system('disgust3.py')
        elif 'is disgusting' in S_text and 'is disgusting' in S5_text and dgmid == distanceD2 and dmax < 40:
            print("Your emotion are disgust level 2")
            os.system('disgust2.py')
        elif 'is nasty' in S_text and 'is nasty' in S4_text and dgmin == distanceD1 and dmax < 40:
            print("Your emotion are disgust level 1")
            os.system('disgust1.py')
        elif 'fine' in S_text:
             print("Your emotion are neutral")
             os.system('neutral.py')
        else:
             print("Your emotion are unidentified")
             os.system('unidentified.py')
    except:
        T.insert(tk.END, "Sorry please try again")
        print("Sorry please try again")

btn = tk.Button(root, text="Record.", command=rec_voi)
btn.pack(side=TOP, pady= 2)
label= Label(root,text="You Said:", bg="green", fg="white", font="Arial")
label.pack()

T =tk.Text(root, height=4, width=80, font=("Arial", 20))
T.pack()

# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy, bg="red", fg="white")
exit_button.pack(side=BOTTOM, pady=20)

root.mainloop()
