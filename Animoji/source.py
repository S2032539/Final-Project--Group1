import tkinter as tk
from tkinter import font
import os
import speech_recognition as sr
from tkinter import *
from dtw import *
from tkinter import *
import fnmatch

root = tk.Tk()
root.title("Animoji Evolution")

root.geometry('700x500')

Expression={'angry', 'very angry', 'very very angry', 'eww','disgusting', 'so disgusting'}


def rec_voi():  
    T.delete("1.0",tk.END)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        #print("Speak Anything: ")
        audio = r.listen(source)
        with open('speech.wav', 'wb') as f:
           f.write(audio.get_wav_data())
                
    try:
        S_text=r.recognize_google(audio)
        T.insert(tk.END, "{}".format(S_text))
        print("You Said:\n{}".format(S_text)) 
        if 'very very angry' in S_text:
            print("Your emotion are anger level 3")
            os.system ('anger3.py')
        elif 'very angry' in S_text:
            print("Your emotion are anger level 2")
            os.system ('anger2.py')
        elif 'angry' in S_text:
            print("Your emotion are anger level 1")
            os.system ('anger1.py')  
        elif 'is so disgusting' in S_text:
            print("Your emotion are disgust level 3")
            os.system ('disgust3.py')  
        elif 'is disgusting' in S_text:
            print("Your emotion are disgust level 2")
            os.system ('disgust2.py')   
        elif 'is nasty' in S_text:
            print("Your emotion are disgust level 1")
            os.system ('disgust1.py')    
        elif 'fine' in S_text:
             print("Your emotion are neutral")
             os.system ('neutral.py')
        else:
             print("Your emotion are unidentified")
             os.system ('unidentified.py')

    except:
        T.insert(tk.END, "Sorry please try again")
        print("Sorry We couldn't recognize your voice")

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

# zuha
#from dtaidistance import dtw
#from dtaidistance import dtw_visualisation as dtwvis
#import numpy as np
#s1 = np.array([0., 0, 1, 2, 1, 0, 1, 0, 0, 2, 1, 0, 0])
#s2 = np.array([0., 1, 2, 3, 1, 0, 0, 0, 2, 1, 0, 0, 0])
#path = dtw.warping_path(s1, s2)
#dtwvis.plot_warping(s1, s2, path, filename="warp.png")