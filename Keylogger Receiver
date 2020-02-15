from pyautogui import *
import pyttsx3 as t2s
from os import listdir,mkdir
from os.path import isfile, join
import numpy as np
import cv2
from tkinter import messagebox
import threading
from tkinter import *
from time import *
from tkinter.font import  Font
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import ImageTk, Image

face_cascade = cv2.CascadeClassifier('face_cas.xml')
k1=''
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
                camera.release()
                root.geometry("600x600+500+100")
                def refresh():
                    scope = ['https://www.googleapis.com/auth/drive']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('Sheet.json', scope)
                    client = gspread.authorize(creds)
                    sheet = client.open('PythonSheet').sheet1
                    global k1
                    k1 = sheet.row_values(1)

                f2 = Font(family="Time New Roman", size=12, weight="bold")
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
                b1 = Button(root, text='Refresh', width=10, command=refresh, bg='orange', font=f3, height=1).place(x=10,y=520)
                b3 = Button(root, text='Exit', command=root.destroy, width=10, height=1, font=f3).place(x=450, y=520)
                def clock():

                    lab.config(text=k1)
                    T.delete(1.0, END)
                    T.insert(END, k1)
                    T.after(500, clock)

                clock()
        t1=thread1()
        t2=thread2()
        t1.start()
        sleep(0.5)
        t2.start()
    def Signup():
        L1 = Label(root, text='                                                                           ', font=f3).place(x=300, y=420)
        try:
            def sign_up():
                sig = sign.get()
                Label(root_signup, text='                                   ').place(x=200, y=180)
                if sig == 'Kundan':
                    x = listdir('C:/Face UnLock Face_Data')
                    if len(x) == 0:
                        pass
                    else:
                        for i in x:
                            os.remove('C:/Face UnLock Face_Data/%s' % i)

                    data_path = 'C:/Face UnLock Face_Data/'
                    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
                    Labels = []
                    for i, files in enumerate(onlyfiles):
                        Labels.append(i)
                    Labels = np.asarray(Labels, dtype=np.int32)
                    x1 = len(Labels)
                    root.destroy()
                    root_S = Tk()
                    root_S.geometry("210x200+1200+330")
                    app = Frame(root_S, bg="white")
                    app.place(x=1, y=1)
                    lmain = Label(app)
                    lmain.grid()
                    camera = cv2.VideoCapture(0)
                    def video_stream():
                        ret, image = camera.read()
                        frame = cv2.flip(image, 1)
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                        n = 0
                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                            n = faces.shape[0]
                            face_img = frame[y:y + h, x:x + w]

                        if n == 0:
                            cv2.putText(frame, 'No Face found', (10, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        else:
                            global count
                            count += 1
                            face = cv2.resize(face_img, (200, 200))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            cv2.imwrite('C:/Face UnLock Face_Data/user' + str(count + x1) + '.jpg', face)

                            cv2.putText(face, str(count), (5, 180), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        if count<20:
                            img = Image.fromarray(face)
                            imgtk = ImageTk.PhotoImage(image=img)
                            lmain.imgtk = imgtk
                            lmain.configure(image=imgtk)
                            lmain.after(1, video_stream)
                        else:
                            root_S.destroy()
                    video_stream()
                    root_S.attributes("-topmost", True)
                    root_S.mainloop()
                else:
                    Label(root_signup, text='Invalid Password').place(x=200, y=180)
            root.destroy()
            camera.release()
            root_signup = Tk()
            root_signup.geometry('360x500+900+100')
            img1 = ImageTk.PhotoImage(Image.open("12_lock.jpg"))
            panel = Label(root_signup, image=img1).place(x=1, y=20)
            sign = StringVar()
            l3 = Label(root_signup, text="Hackacthon Battle", fg='brown', font=f1).place(x=70, y=10)
            l3 = Label(root_signup, text=" Sign Up with Face_Lock", fg='darkblue', font=f1).place(x=60, y=40)
            l3 = Label(root_signup, text=" Enter Password ", fg='blue', font=f1).place(x=100, y=380)
            E1 = Entry(root_signup, show='*', textvariable=sign, font=f3).place(x=90, y=420)
            but = Button(root_signup, text='Login', command=sign_up, width=20, height=1, font=f3, bg='green').place(x=80,
                                                                                                                    y=460)
            root_signup.resizable('false', 'false')
            root_signup.mainloop()
        except:
            pass
    def login():
        s1 = ss1.get()
        s2 = ss2.get()
        if (s1 == 'Kundan' and s2 == 'Singh'):
            eng = t2s.init()
            try:
                eng.setProperty('rate', 140);
                eng.setProperty('volume', .9)
                eng.say('login successfuly. Loading the Content')
                eng.runAndWait()
            except:
                pass
            Main()
        elif s1 == '' and s2 == '':
            eng = t2s.init()
            try:
                eng.setProperty('rate', 140);
                eng.setProperty('volume', .9)
                eng.say('First You should Enter Username and Password.')
                eng.runAndWait()
            except:
                pass

            o1 = "Message: Please Enter Username and Password"
            L1 = Label(root, text=o1, font=f3).place(x=10, y=550)
        else:
            eng = t2s.init()
            try:
                eng.setProperty('rate', 140);
                eng.setProperty('volume', .9)
                eng.say('You have Entered Wrong username or password')
                eng.runAndWait()
            except:
                pass
            o2 = "Please Enter valid Username Or Password"
            L2 = Label(root, text=o2, font=f3).place(x=10, y=550)
    def win():
        ans1 = messagebox.askyesno("Exit", "DO You Want to Exit")
        if ans1 == True:
            root.quit()
    try:
        mkdir('C:/Face UnLock Face_Data/')
    except:
        pass
    root=Tk()
    app=Frame(root,bg="white",width=100,height=100)
    f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
    f2 = Font(family="Time New Roman", size=14, weight="bold")
    f3 = Font(family="Time New Roman", size=12, weight="bold")
    eng = t2s.init()
    def text2speech():
        try:
            eng.setProperty('rate', 140);
            eng.setProperty('volume', .9)
            eng.say('Welcome to KeyLogger Receiving Panel')
            eng.runAndWait()
        except:
            pass
    root.title("Keylogger Receiver : Cyber Security Project 2020")
    l3 = Label(root, text="Receiver Connected with Google Server", fg='brown', font=f2).place(x=300, y=15)
    l3 = Label(root, text=" Cyber Security Project 2020", fg='green', font=f2).place(x=70, y=80)
    l3 = Label(root, text="Enter Username and Password", fg='darkblue', font=f2).place(x=70, y=150)
    l3 = Label(root, text="Copyright @ Kundan Kumar (U-1701285) ", fg='skyblue',font=f2).place(x=550, y=560)
    l1 = Label(root, text='Username', fg='brown', font=f2).place(x=60, y=220)
    l2 = Label(root, text='Password', fg='brown', font=f2).place(x=60, y=280)
    ss1 = StringVar()
    ss2 = StringVar()
    e1 = Entry(root, textvariable=ss1,width=14,font=f2).place(x=210, y=220)
    e2 = Entry(root, textvariable=ss2, show='*',width=14,font=f2).place(x=210, y=280)
    b1 = Button(root, text='Login', command=login, width=31, height=1, bg='skyblue', fg='white', font=f3).place(x=50,y=330)
    b1=Button(root,text='Sign_up',width=31,command=Signup,bg='orange',font=f3,height=1).place(x=50,y=380)
    b3 = Button(root, text='Exit', command=root.quit, width=31, height=1, font=f3).place(x=50, y=430)

    app.place(x=450, y=60)
    lmain = Label(app)
    lmain.grid()
    camera = cv2.VideoCapture(0)
    try:
        data_path = 'C:/Face UnLock Face_Data/'
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
        Training_Data, Labels = [],[]
        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)

        if len(Labels) == 0:
            eng = t2s.init()
            try:
                eng.setProperty('rate', 140);
                eng.setProperty('volume', .9)
                eng.say('Firstly You should SignUp With Face ID')
                eng.runAndWait()
            except:
                pass
            o1 = "Message: Firstly You should SignUp With Face ID"
            L1 = Label(root, text=o1, font=f3).place(x=200, y=420)
        else:
            Labels = np.asarray(Labels, dtype=np.int32)
            model = cv2.face.LBPHFaceRecognizer_create()
            model.train(np.asarray(Training_Data), np.asarray(Labels))
            ct = 0

        def video_stream():
            ret, image = camera.read()
            image = cv2.flip(image, 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            n = 0
            try:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    face = gray[y:y + h, x:x + w]
                    face = cv2.resize(face, (200, 200))
                    n = face.shape[0]
                    j, k = model.predict(face)
                    confidence = int(100 * (1 - (k) / 300))
                if n > 0:
                    if k < 50:
                        if confidence > 75:
                            global ct
                            ct += 1
                            cv2.putText(image, '% Matching' + str(confidence), (20, 450), cv2.FONT_HERSHEY_COMPLEX, 1,
                                        (0, 0, 255), 1)

                            cv2.putText(image, 'unlocking', (420, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 125), 3)

                        else:
                            ct = 0
                            cv2.putText(image, "Unknown", (x + w, y + h + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0),
                                        1)
                    else:
                        ct = 0
                        cv2.putText(image, "Unknown", (x + w, y + h + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

                if n == 0:
                    cv2.putText(image,"Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            except:
                pass
            if ct == 20:
                eng = t2s.init()
                try:
                    eng.setProperty('rate', 140)
                    eng.setProperty('volume', .9)
                    eng.say('login successfuly. Loading the Content')
                    eng.runAndWait()
                except:
                    pass
                Main()
            img = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, video_stream)
        video_stream()
    except:
        pass

    root.geometry("1050x600+500+100")

    try:
        t = threading.Thread(name='child', target=text2speech, args=())
        if not t.is_alive():
            t.start()
    except:
        pass
    root.resizable('false','false')
    root.mainloop()
except:
    pass

