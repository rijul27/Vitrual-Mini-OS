from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import time
import datetime
from datetime import datetime
from datetime import timedelta
import smtplib
import mysql.connector
import pyttsx3
import os
import webbrowser
import datetime
import speech_recognition as sr
import cv2
import numpy as np 
import time
from keys import *
from handTracker import *
from pynput.keyboard import Controller



root = Tk()
root.title("SPARK")
root.iconbitmap("aa.ico")
root.geometry("1500x780+300+150")
root.resizable(0, 0)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Welcome to our Spark virtual assistant. This is our project for 2nd yead. This project is made by Anmol Kaur,Kushal pratap singh,Pratyush Saraswat , Rijul Shakya and Shivam Prashad Gupta ") 
class maincode:
     def takeCommand1(self):
         import speech_recognition as sr
         r = sr.Recognizer()
         mic = sr.Microphone(device_index=1)
         with mic as source:
             r.adjust_for_ambient_noise(source, duration=1)
             audio = r.listen(source, timeout=5)
         try:
             SQ2 = r.recognize_google(audio, language='English')
         except:
             messagebox.showerror('SPARK', 'Sorry! Not able to uderstand')
             pass
         return SQ2





     def login(self):

         self.var1 = self.e1.get()
         self.var2 = self.e2.get()
         import mysql.connector
         mydb=mysql.connector.connect(host='localhost',user='root',password='abcd',database='SPARK')
         cursor=mydb.cursor()
         cursor.execute("SELECT * FROM USER WHERE USER_ID='"+self.var1+"' and Password='"+self.var2+"'") 
         self.ab = cursor.fetchone()
         if self.ab!=None:
               
             self.under_fm=Frame(root,height=780,width=1500,bg='#fff')
             self.under_fm.place(x=0,y=0)
             self.fm2=Frame(root,bg='#0f624c',height=80,width=1500)
             self.fm2.place(x=0,y=0)
            

             self.lbb=Label(self.fm2,bg='#0f624c')
             self.lbb.place(x=30,y=5)
             self.ig=PhotoImage(file='spark1.png')
             self.lbb.config(image=self.ig)
             self.lb3=Label(self.fm2,text='WELCOME TO SPARK  ',fg='White',bg='#0f624c',font=('Arial',30,'bold'))
             self.lb3.place(x=450,y=17)
             self.lbb5=Label(self.fm2,bg='#0f624c')
             self.lbb5.place(x=1400,y=5)
             self.ig3=PhotoImage(file='spark1.png')
             self.lbb5.config(image=self.ig3)





       





            

             self.name=Label(root,text="Name : ",bg='#fff',fg="black",font=('Arial',10,'bold'))
             self.name.place(x=5,y=83)
             self.name1=Label(root,text=self.ab[1],fg='black',bg='#fff',font=('Arial',10,'bold'))
             self.name1.place(x=60,y=83)

          

             self.today=date.today()
             self.dat=Label(root,text='Date : ',bg='#fff',fg='black',font=('Arial',10,'bold'))
             self.dat.place(x=1300,y=83)
             self.dat2 = Label(root, text=self.today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
             self.dat2.place(x=1350, y=83)

             self.cur()

         else:
               messagebox.showerror('SPARK assosiation', 'Your ID or Password is not Valid')
            
     def cur(self):
             self.fm3=Frame(root,bg='black',width=1500,height=780)
             self.fm3.place(x=0,y=110)
             self.canvas=Canvas(self.fm3,height=1000,width=1600,bg='#22224b')
             self.canvas.place(x=0,y=0)

             self.photo=PhotoImage(file="images (17).png")
             self.canvas.create_image(5,-37,image=self.photo,anchor=NW)

        

             def clock():
                 h = str(time.strftime("%H"))
                 m = str(time.strftime("%M"))
                 s = str(time.strftime("%S"))

                 if int(h) >=12 and int(m) >=0:
                       self.lb7_hr.config(text="PM")

                 
                 self.lb1_hr.config(text=h)
                 self.lb3_hr.config(text=m)
                 self.lb5_hr.config(text=s)

                 self.lb1_hr.after(200, clock)

             self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#fc1c1c', fg='white')
             self.lb1_hr.place(x=1220, y=570, width=60, height=30)


             self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#0ee38b', fg='white')
             self.lb3_hr.place(x=1295, y=570, width=60, height=30)


             self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#2b1dff', fg='white')
             self.lb5_hr.place(x=1370, y=570, width=60, height=30)


             self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#2b1dff', fg='white')
             self.lb7_hr.place(x=1445, y=570, width=60, height=30)


             clock()

            

             self.develop=Label(self.fm3,text='Developed By - Anmol Kaur,Kushal pratap singh,Prashant singh,Pratyush Saraswat , Rijul Shakya and Shivam Prashad Gupta',bg='#fff',fg='blue',height=5,width=150
                               ,font=('Cursive',12,'italic','bold'))
             self.develop.place(x=5,y=600)

             self.develop=Label(self.fm3,text='VIRTUAL TOOLS OF SPARK',bg='black',fg='blue',height=1,width=100
                               ,font=('Cursive',20,'italic','bold'))
             self.develop.place(x=-150,y=10)










             self.bt1=Button(self.fm3,text='Virtual keyboard',fg='black',bg='ghost white',font=('Arial',15,'bold'),width=200,
                          height=-3,bd=10,relief='flat',command=self.VB,cursor='hand2')
             self.bt1.place(x=15,y=60)
             self.logo = PhotoImage(file='bt1.png')
             self.bt1.config(image=self.logo, compound=LEFT)
             self.small_logo = self.logo.subsample(1,1)
             self.bt1.config(image=self.small_logo)

            

             self.bt2 = Button(self.fm3, text='  Virtual Mouse', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                            width=200,height=-3, bd=10,relief='flat',command=self.VM,cursor='hand2')
             self.bt2.place(x=250, y=60)
             self.log = PhotoImage(file='bt2.png')
             self.bt2.config(image=self.log, compound=LEFT)
             self.small_log = self.log.subsample(1, 1)
             self.bt2.config(image=self.small_log)

            

             self.bt3 = Button(self.fm3, text=' Virtual painter', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                           width=200,height=-3,bd=10,relief='flat',cursor='hand2',command=self.VP)
             self.bt3.place(x=485, y=60)
             self.logb = PhotoImage(file='bt3.png')
             self.bt3.config(image=self.logb, compound=LEFT)
             self.small_logb = self.logb.subsample(1, 1)
             self.bt3.config(image=self.small_logb)

            

             self.bt4 = Button(self.fm3, text='  camera', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=-3,bd=7,relief='flat',cursor='hand2',command=self.cam)
             self.bt4.place(x=720, y=60)
             self.log4 = PhotoImage(file='bt4.png')
             self.bt4.config(image=self.log4, compound=LEFT)
             self.small_log4 = self.log4.subsample(1, 1)
             self.bt4.config(image=self.small_log4)

            

             self.bt5 = Button(self.fm3, text=' video', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=-3,bd=7,relief='flat',cursor='hand2',command=self.vi)
             self.bt5.place(x=955, y=60)
             self.log5 = PhotoImage(file='bt5.png')
             self.bt5.config(image=self.log5, compound=LEFT)
             self.small_log5 = self.log5.subsample(1, 1)
             self.bt5.config(image=self.small_log5)

           

             self.bt6 = Button(self.fm3, text='  Security Camera', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                           width=200,height=-3,bd=7, relief='flat',cursor='hand2',command=self.sec)
             self.bt6.place(x=1190, y=60)
             self.log6 = PhotoImage(file='bt6.png')
             self.bt6.config(image=self.log6, compound=LEFT)
             self.small_log6 = self.log6.subsample(1, 1)
             self.bt6.config(image=self.small_log6)

            

            


             self.develop=Label(self.fm3,text='APPS  OF SPARK',bg='black',fg='blue',height=1,width=100
                               ,font=('Cursive',20,'italic','bold'))
             self.develop.place(x=-150,y=210)



             self.bt7 = Button(self.fm3, text=' ATTENDENCE SYSTEM', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.search)
             self.bt7.place(x=15, y=270)
             self.log7 = PhotoImage(file='bt9.png')
             self.bt7.config(image=self.log7, compound=LEFT)
             self.small_log7 = self.log7.subsample(1, 1)
             self.bt7.config(image=self.small_log7)


             self.bt10 = Button(self.fm3, text=' Snake Game', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.game)
             self.bt10.place(x=250, y=270)
             self.log10 = PhotoImage(file='bt10.png')
             self.bt10.config(image=self.log10, compound=LEFT)
             self.small_log10 = self.log10.subsample(1, 1)
             self.bt10.config(image=self.small_log10)



             self.bt111 = Button(self.fm3, text=' NotePad', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.note)
             self.bt111.place(x=485, y=270)
             self.log111 = PhotoImage(file='bt11.png')
             self.bt111.config(image=self.log111, compound=LEFT)
             self.small_log111 = self.log111.subsample(1, 1)
             self.bt111.config(image=self.small_log111)




             self.bt112 = Button(self.fm3, text=' Calculator', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.calc)
             self.bt112.place(x=720, y=270)
             self.log112 = PhotoImage(file='bt12.png')
             self.bt112.config(image=self.log112, compound=LEFT)
             self.small_log112 = self.log112.subsample(1, 1)
             self.bt112.config(image=self.small_log112)



             self.bt116 = Button(self.fm3, text=' Search Here', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.search1)
             self.bt116.place(x=955, y=270)
             self.log116 = PhotoImage(file='bt7.png')
             self.bt116.config(image=self.log116, compound=LEFT)
             self.small_log116 = self.log116.subsample(1, 1)
             self.bt116.config(image=self.small_log116)


             self.bt119 = Button(self.fm3, text=' About SPARK', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                          width=200,height=0,bd=7, relief='flat',cursor='hand2',command=self.help)
             self.bt119.place(x=1190, y=270)
             self.log119 = PhotoImage(file='bt13.png')
             self.bt119.config(image=self.log119, compound=LEFT)
             self.small_log119 = self.log119.subsample(1, 1)
             self.bt119.config(image=self.small_log119)






          

             
             try:

                self.bt8 = Button(self.fm3, text='  Shut down', fg='black', bg='ghost white', font=('Arial', 15, 'bold'),
                               width=200,
                          height=-3, bd=7, relief='flat',cursor='hand2',command=self.code)
                self.bt8.place(x=15, y=540)
                self.log8 = PhotoImage(file='bt8.png')
                self.bt8.config(image=self.log8, compound=LEFT)
                self.small_log8 = self.log8.subsample(1, 1)
                self.bt8.config(image=self.small_log8)

             except:

               self.bt9 = ttk.Button(self.fm3, text="ram", bg='#11d09a', font=('Arial', 15, 'bold'), width=150,
                                     height=0)
               self.bt9.place(x=10, y=350)
               self.log9 = PhotoImage(file='bt8.png')
               self.bt9.config(image=self.log9, compound=LEFT)
               self.small_log9 = self.log9.subsample(3, 3)
               self.bt9.config(image=self.small_log9)






     def mainclear(self):
         self.e1.delete(0,END)
         self.e2.delete(0,END)


    

     def VB(self):
         import virtualkeyboard

      
     def VM(self):
         import Virtual_Mouse
         

     def VP(self):
         import virtual_painter 

         
     def cam(self):
         import camera
    

     def vi(self):
         import video

     def search(self):
         class demt(maincode):
             def delmdata(self):

                 self.fc = Frame(root, bg='#a7ecd9', width=1500, height=780)
                 self.fc.place(x=0, y=110)
                 self.fc1 = Frame(self.fc, bg='#fff', width=700, height=350, bd=5, relief='flat')
                 self.fc1.place(x=350, y=30)
                 self.edm = Frame(self.fc1, bg='#0f624c', bd=0, relief='flat', width=700, height=35)
                 self.edm.place(x=0, y=0)
                 self.lac = Label(self.edm, text='ATTENDENCE ', bg='#0f624c', fg='#fff', font=('Arial', 12, 'bold'))
                 self.lac.place(x=280, y=5)
                 self.label8 = Label(self.fc1, text='Student Name', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label8.place(x=150, y=65)
                 self.entryl= Entry(self.fc1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entryl.place(x=250, y=65)



                 self.label81 = Label(self.fc1, text='Student UID', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label81.place(x=150, y=115)
                 self.entryl81= Entry(self.fc1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entryl81.place(x=250, y=115)



                 self.label812 = Label(self.fc1, text='Period', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label812.place(x=150, y=165)
                 self.entryl812= Entry(self.fc1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entryl812.place(x=250, y=165)





                 



                 self.butto = Button(self.fc1, text='Image Verification', bg='#0f624c', fg='#fff', width=24, height=0,
                                       font=('Arial', 10, 'bold'),command=self.srch)
                 self.butto.place(x=200, y=215)

                 self.backbt = Button(self.fc,width=60, bg='#a7ecd9',activebackground='#a7ecd9',bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)

                 self.mike4 = Button(self.fc1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entryl.insert(END, self.takeCommand()))
                 self.mike4.place(x=430, y=65)
                 self.log = PhotoImage(file='mike.png')
                 self.mike4.config(image=self.log, compound=LEFT)
                 self.small_log4 = self.log.subsample(1, 1)
                 self.mike4.config(image=self.small_log4)


                 self.mike5 = Button(self.fc1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entryl81.insert(END, self.takeCommand()))
                 self.mike5.place(x=430, y=115)
                 self.log = PhotoImage(file='mike.png')
                 self.mike5.config(image=self.log, compound=LEFT)
                 self.small_log5 = self.log.subsample(1, 1)
                 self.mike5.config(image=self.small_log5)




                 self.mike6 = Button(self.fc1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.entryl812.insert(END, self.takeCommand()))
                 self.mike6.place(x=430, y=165)
                 self.log = PhotoImage(file='mike.png')
                 self.mike6.config(image=self.log, compound=LEFT)
                 self.small_log6 = self.log.subsample(1, 1)
                 self.mike6.config(image=self.small_log6)





             def takeCommand(self):
                 import speech_recognition as sr
                 r = sr.Recognizer()
                 mic = sr.Microphone(device_index=1)
                 with mic as source:
                     r.adjust_for_ambient_noise(source, duration=1)
                     audio = r.listen(source, timeout=5)
                 try:
                     SQ1 = r.recognize_google(audio, language='English')
                 except:
                     messagebox.showerror('SPARK assosiation', 'Sorry! Not able to uderstand')
                     pass
                 return SQ1


             def srch(self):
                 import cv2
                 recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
                 recognizer.read('trainer/trainer.yml')   #load trained model
                 cascadePath = "haarcascade_frontalface_default.xml"
                 faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

                 font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


                 id = 2 #number of persons you want to Recognize


                 names = ['','PRATYUSH']  #names, leave first empty bcz counter starts from 0


                 cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
                 cam.set(3, 640) # set video FrameWidht
                 cam.set(4, 480) # set video FrameHeight
                 minW = 0.1*cam.get(3)
                 minH = 0.1*cam.get(4)
                 rt=0
                 for i in range(1):
                     ret, img =cam.read() #read the frames using the above created object
                     converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another
                     faces = faceCascade.detectMultiScale( 
                         converted_image,
                         scaleFactor = 1.2,
                         minNeighbors = 5,
                         minSize = (int(minW), int(minH)),)
                     for(x,y,w,h) in faces:
                         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image
                         id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
                         if (accuracy < 100):
                             id = names[id]
                             accuracy = "  {0}%".format(round(100 - accuracy))
                             speak("Your face is verified.........you are present in class")
                             rt=6
                         else:
                             speak("We are not able recognize your face....Please show me your face properly")
                             id = "unknown"
                             accuracy = "  {0}%".format(round(100 - accuracy))
                         cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                         cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
                     cv2.imshow('camera',img) 
                     k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
                     if k == 27:
                         break
                 if(rt==6):
                     self.a=self.entryl.get()
                     self.b=self.entryl81.get()
                     self.c=self.entryl812.get()
                     self.d="present"
                     mydb=mysql.connector.connect(host='localhost',user='root',password='abcd',database='school')
                     cursor=mydb.cursor()
                     s="INSERT INTO mark (name,UID,period,attendence) VALUES(%s,%s,%s,%s)"
                     b1=(self.a,self.b,self.c,self.d)
                     cursor.execute(s,b1)
                     mydb.commit()
                     messagebox.showinfo("SPARK Association","You are successfully marked present !")
                 else:
                     speak("We are not able recognize your face....Please show me your face properly")
                     speak("You are not there in class")
                     speak("You are marked as absent....")
                     self.a=self.entryl.get()
                     self.b=self.entryl81.get()
                     self.c=self.entryl812.get()
                     self.d="absent"
                     mydb=mysql.connector.connect(host='localhost',user='root',password='abcd',database='school')
                     cursor=mydb.cursor()
                     s="INSERT INTO mark (name,UID,period,attendence) VALUES(%s,%s,%s,%s)"
                     b1=(self.a,self.b,self.c,self.d)
                     cursor.execute(s,b1)
                     mydb.commit()
                     messagebox.showinfo("SPARK Association ","You are marked as absent !")

            

    
        
                 
         object=demt()
         object.delmdata()

     


   

     def sec(self):
         import security

     def game(self):
         import snake

     def calc(self):
         import tkinter as tk
         LARGE_FONT_STYLE = ("Arial", 40, "bold")
         SMALL_FONT_STYLE = ("Arial", 16)
         DIGITS_FONT_STYLE = ("Arial", 24, "bold")
         DEFAULT_FONT_STYLE = ("Arial", 20)
         OFF_WHITE = "#F8FAFF"
         WHITE = "#FFFFFF"
         LIGHT_BLUE = "#CCEDFF"
         LIGHT_GRAY = "#F5F5F5"
         LABEL_COLOR = "#25265E"






         class Calculator:
             def __init__(self):
                 self.window = tk.Tk()
                 self.window.geometry("375x667")
                 self.window.resizable(0, 0)
                 self.window.title("Calculator")
                 self.total_expression = ""
                 self.current_expression = ""
                 self.display_frame = self.create_display_frame()
                 self.total_label, self.label = self.create_display_labels()

                 self.digits = {
                      7: (1, 1), 8: (1, 2), 9: (1, 3),
                      4: (2, 1), 5: (2, 2), 6: (2, 3),
                      1: (3, 1), 2: (3, 2), 3: (3, 3),
                      0: (4, 2), '.': (4, 1)}
                 self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
                 self.buttons_frame = self.create_buttons_frame()

                 self.buttons_frame.rowconfigure(0, weight=1)
                 for x in range(1, 5):
                     self.buttons_frame.rowconfigure(x, weight=1)
                     self.buttons_frame.columnconfigure(x, weight=1)
                     self.create_digit_buttons()
                     self.create_operator_buttons()
                     self.create_special_buttons()
                     self.bind_keys()
             def bind_keys(self):
                 self.window.bind("<Return>", lambda event: self.evaluate())
                 for key in self.digits:
                     self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
                 for key in self.operations:
                     self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
             def create_special_buttons(self):
                 self.create_clear_button()
                 self.create_equals_button()
                 self.create_square_button()
                 self.create_sqrt_button()
             def create_display_labels(self):
                 total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
                 total_label.pack(expand=True, fill='both')

                 label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
                 label.pack(expand=True, fill='both')

                 return total_label, label

             def create_display_frame(self):
                 frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
                 frame.pack(expand=True, fill="both")
                 return frame
             def add_to_expression(self, value):
                 self.current_expression += str(value)
                 self.update_label()
             def create_digit_buttons(self):
                 for digit, grid_value in self.digits.items():
                     button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                     button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) 
             def append_operator(self, operator):
                 self.current_expression += operator
                 self.total_expression += self.current_expression
                 self.current_expression = ""
                 self.update_total_label()
                 self.update_label()

             def create_operator_buttons(self):
                 i = 0
                 for operator, symbol in self.operations.items():
                     button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=lambda x=operator: self.append_operator(x))
                     button.grid(row=i, column=4, sticky=tk.NSEW)
                     i += 1

             def clear(self):
                 self.current_expression = ""
                 self.total_expression = ""
                 self.update_label()
                 self.update_total_label()

             def create_clear_button(self):
                 button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=self.clear)
                 button.grid(row=0, column=1, sticky=tk.NSEW)

             def square(self):
                 self.current_expression = str(eval(f"{self.current_expression}**2"))
                 self.update_label()

             def create_square_button(self):
                 button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=self.square)
                 button.grid(row=0, column=2, sticky=tk.NSEW)

             def sqrt(self):
                 self.current_expression = str(eval(f"{self.current_expression}**0.5"))
                 self.update_label()

             def create_sqrt_button(self):
                 button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
                 button.grid(row=0, column=3, sticky=tk.NSEW)

             def evaluate(self):
                  self.total_expression += self.current_expression
                  self.update_total_label()
                  try:
                      self.current_expression = str(eval(self.total_expression))
                      self.total_expression = ""
                  except Exception as e:
                      self.current_expression = "Error"
                  finally:
                      self.update_label()
             def create_equals_button(self):
                  button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=self.evaluate)
                  button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
             def create_buttons_frame(self):
                 frame = tk.Frame(self.window)
                 frame.pack(expand=True, fill="both")
                 return frame

             def update_total_label(self):
                 expression = self.total_expression
                 for operator, symbol in self.operations.items():
                     expression = expression.replace(operator, f' {symbol} ')
                     self.total_label.config(text=expression)
             def update_label(self):
                 self.label.config(text=self.current_expression[:11])
             def run(self):
                 self.window.mainloop()
         if __name__ == "__main__":
             calc = Calculator()
             calc.run()

     



     def note(self):
         from tkinter.messagebox import showinfo
         from tkinter.filedialog import askopenfilename, asksaveasfilename
         import os
         import speech_recognition as sr
         def takeCommand1():
             import speech_recognition as sr
             r = sr.Recognizer()
             mic = sr.Microphone(device_index=1)
             with mic as source:
                 r.adjust_for_ambient_noise(source, duration=1)
                 audio = r.listen(source, timeout=5)
             try:
                 SQ2 = r.recognize_google(audio, language='English')
             except:
                 pass
             TextArea.insert(END,SQ2)
    



         def newFile(self):
             global file
             root.title("Untitled - Notepad")
             file = None
             TextArea.delete(1.0, END)
         def openFile():
             global file
             file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
             if file == "":
                 file = None
             else:
                 root.title(os.path.basename(file) + " - Notepad")
                 TextArea.delete(1.0, END)
                 f = open(file, "r")
                 TextArea.insert(1.0, f.read())
                 f.close()
         def saveFile(self):
             global file
             if file == None:
                 file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                                         filetypes=[("All Files", "*.*"),
                                                    ("Text Documents", "*.txt")])
                 if file =="":
                     file = None

                 else:
                     f = open(file, "w")
                     f.write(TextArea.get(1.0, END))
                     f.close()

                     root.title(os.path.basename(file) + " - Notepad")
                     print("File Saved")
             else:
                  f = open(file, "w")
                  f.write(TextArea.get(1.0, END))
                  f.close()
         def quitApp(self):
             root.destroy()
         def cut():
             TextArea.event_generate(("<>"))
         def copy():
             TextArea.event_generate(("<>"))
         def paste():
             TextArea.event_generate(("<>"))
         def about():
             showinfo("Notepad", "This Notepad is made by SPARK association")

         if __name__ == '__main__':
             root = Tk()
             root.title("Untitled - Notepad")
             root.wm_iconbitmap("aa.ico")
             root.geometry("644x788")

             TextArea = Text(root, font="lucida 13")
             file = None
             TextArea.pack(expand=True, fill=BOTH)

    
             MenuBar = Menu(root)

    
             FileMenu = Menu(MenuBar, tearoff=0)
   
             FileMenu.add_command(label="New", command=newFile)

     
             FileMenu.add_command(label="Open", command = openFile)

  

             FileMenu.add_command(label = "Save", command = saveFile)
             FileMenu.add_separator()
             FileMenu.add_command(label = "Exit", command = quitApp)
             MenuBar.add_cascade(label = "File", menu=FileMenu)
    
             EditMenu = Menu(MenuBar, tearoff=0)
     
             EditMenu.add_command(label = "Cut", command=cut)
             EditMenu.add_command(label = "Copy", command=copy)
             EditMenu.add_command(label = "Paste", command=paste)

             MenuBar.add_cascade(label="Edit", menu = EditMenu)

     


             speakMenu=Menu(MenuBar, tearoff=0)
             speakMenu.add_command(label = "Speak", command=takeCommand1)
             MenuBar.add_cascade(label="Mike", menu=speakMenu)




     
             HelpMenu = Menu(MenuBar, tearoff=0)
             HelpMenu.add_command(label = "About Notepad", command=about)
             MenuBar.add_cascade(label="Help", menu=HelpMenu)

    


    

             root.config(menu=MenuBar)

     
             Scroll = Scrollbar(TextArea)
             Scroll.pack(side=RIGHT,  fill=Y)
             Scroll.config(command=TextArea.yview)
             TextArea.config(yscrollcommand=Scroll.set)

             root.mainloop()


         

         
         

     def search1(self):
         def takeCommand1(self):
             import speech_recognition as sr
             r = sr.Recognizer()
             mic = sr.Microphone(device_index=1)
             with mic as source:
                 r.adjust_for_ambient_noise(source, duration=1)
                 audio = r.listen(source, timeout=5)
             try:
                 SQ2 = r.recognize_google(audio, language='English')
             except:
                 messagebox.showerror('SPARK', 'Sorry! Not able to uderstand')
                 pass
             if 'camera' in SQ2:
                 speak("Here I am going to open your camera")
                 import camera
             elif 'paint'in SQ2:
                 speak("Here I am going to open your painter")
                 import virtual_painter
             elif 'video' in SQ2:
                 speak("Here I am going to open your video capture")
                 import video
             elif 'mouse' in SQ2:
                 speak("Here I am going to open your virtual mouse")
                 import Virtual_Mouse
             elif 'security' in SQ2:
                 speak("Here I am going to open your security camera")
                 import security
             elif 'google' in SQ2:
                 speak("Here is your Google sir...")
                 webbrowser.open("google.com")
             elif 'calculator' in SQ2:
                 speak("Here is your Calculator")
                 import calculator
             elif 'notepad'in SQ2:
                 speak("Here is your Notepad::")
                 import notepad
             elif 'attendance'in SQ2:
                 speak("Here is your attendance application")
                 search(self)
             elif 'youtube' in SQ2:
                 speak("Here is your Youtube...")
                 webbrowser.open("youtube.com")


             else:
                 speak("Sorry your voice is not clear to me...please Try again")
         takeCommand1(self)
           
    

     def help(self):
         speak("The word technology and its uses have immensely changed since the 20th century, and with time, it has continued to evolve ever since. We are living in a world driven by technology. The advancement of technology has played an important role in the development of human civilization, along with cultural changes. This project is our second year project which will show you the concept of virtual assistant...In this project there are many virtual tools which will help your life easy ")

     def code(self):

         self.fm=Frame(root,height=1000,width=1600,bg='white')
         self.fm.place(x=0,y=0)

         self.canvas=Canvas(self.fm,height=1000,width=1600,bg='#22224b')
         self.canvas.place(x=0,y=0)

         self.photo=PhotoImage(file="images (17).png")
         self.canvas.create_image(5,-37,image=self.photo,anchor=NW)

         self.fm1=Frame(self.canvas,height=260,width=300,bg='ghost white',bd=3,relief='ridge')
         self.fm1.place(x=580,y=320)

         self.b1=Label(self.fm1,text='USER-ID',bg='ghost white',font=('Arial',10,'bold'))
         self.b1.place(x=20,y=42)

         self.e1=Entry(self.fm1,width=22,font=('arial',9,'bold'),bd=4,relief='groove')
         self.e1.place(x=100,y=40)

         self.lb2=Label(self.fm1,text='PASSWORD',bg='ghost white',font=('Arial',10,'bold'))
         self.lb2.place(x=20,y=102)

         self.e2=Entry(self.fm1,width=22,show='*',font=('arial',9,'bold'),bd=4,relief='groove')
         self.e2.place(x=100,y=100)


         self.btn1=Button(self.fm1,text='  login',fg='white',bg='red',width=100,font=('Arial',11,'bold'),
                 activebackground='ghost white',activeforeground='black',command=self.login,bd=3,relief='flat',cursor='hand2')
         self.btn1.place(x=25,y=160)
         self.logo = PhotoImage(file='user.png')
         self.btn1.config(image=self.logo, compound=LEFT)
         self.small_logo = self.logo.subsample(1, 1)
         self.btn1.config(image=self.small_logo)



         self.btn2=Button(self.fm1,text='Clear',fg='white',bg='blue',width=100,font=('Arial',11,'bold'),
                 activebackground='white',activeforeground='black',bd=3,relief='flat',cursor='hand2',
                          command=self.mainclear)
         self.btn2.place(x=155,y=160)
         self.log = PhotoImage(file='cart.png')
         self.btn2.config(image=self.log, compound=LEFT)
         self.small_log = self.log.subsample(1, 1)
         self.btn2.config(image=self.small_log)

         

         self.forgot=Label(self.fm1,text='Sign up',fg='red',bg='ghost white',bd=3,activeforeground='black',
                           font=('cursive',9,'bold'))
         self.forgot.place(x=120,y=220)
         self.forgot.bind("<Button>",self.mouseClick)



         self.mike70 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.e1.insert(END, self.takeCommand1()))
         self.mike70.place(x=255, y=38)
         self.log = PhotoImage(file='mike.png')
         self.mike70.config(image=self.log, compound=LEFT)
         self.small_log70 = self.log.subsample(1, 1)
         self.mike70.config(image=self.small_log70)

         self.mike25 = Button(self.fm1, width=25, bg='white',activebackground='white', bd=0, relief='flat',
                                                                                                 command=lambda:self.e2.insert(END,self.takeCommand1()))
         self.mike25.place(x=255, y=98)
         self.log = PhotoImage(file='mike.png')
         self.mike25.config(image=self.log, compound=LEFT)
         self.small_log25 = self.log.subsample(1, 1)
         self.mike25.config(image=self.small_log25)
         
         root.mainloop()

     def mouseClick(self,event):
         self.rog=Tk()
         self.rog.title("Sign up")
         self.rog.geometry("500x450+530+280")
         self.rog.iconbitmap("aa.ico")
         self.rog.resizable(0,0)
         self.rog.configure(bg='#fff')

         self.label=Label(self.rog,text="Add your deatils",bg='#fff',fg='red',font=("cursive",20,'bold'))
         self.label.place(x=115,y=15)

         self.user=Label(self.rog,text='USER-ID :',bg='#fff',fg='black',font=("cursive",10,'bold'))
         self.user.place(x=40,y=95)

         self.user=Label(self.rog,text='USER-NAME :',bg='#fff',fg='black',font=("cursive",10,'bold'))
         self.user.place(x=40,y=135)

         self.user = Label(self.rog, text='PASSWORD :', bg='#fff', fg='black', font=("cursive", 10, 'bold'))
         self.user.place(x=40, y=180)


         self.e1 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e1.place(x=170, y=95)

         self.e2 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e2.place(x=170, y=135)

         self.e3 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e3.place(x=170, y=175)



         self.btn1 = Button(self.rog, text=' capture your image', fg='white', bg='#5500ff', width=20, font=('Arial', 13, 'bold'),
                            activebackground='white', activeforeground='black',bd=3, relief='flat',
                            cursor='hand2',command=self.cap)
         self.btn1.place(x=115, y=240)

         self.btn1 = Button(self.rog, text=' Save the image', fg='white', bg='#5500ff', width=20, font=('Arial', 13, 'bold'),
                            activebackground='white', activeforeground='black',bd=3, relief='flat',
                            cursor='hand2',command=self.train)
         self.btn1.place(x=115, y=300)





         self.btn1 = Button(self.rog, text='Submit', fg='white', bg='#5500ff', width=20, font=('Arial', 13, 'bold'),
                            activebackground='white', activeforeground='black',bd=3, relief='flat',
                            cursor='hand2',command=self.sign_up)
         self.btn1.place(x=115, y=360)


     def sign_up(self):
         self.a=self.e1.get()
         self.b=self.e2.get()
         self.c=self.e3.get()
         mydb=mysql.connector.connect(host='localhost',user='root',password='abcd',database='SPARK')
         cursor=mydb.cursor()
         cursor.execute("SELECT USER_ID FROM USER WHERE USER_ID='"+self.a+"'" ) 
         self.data=cursor.fetchone()
         if self.data==None:
             s="INSERT INTO USER (USER_ID,USER_NAME,Password) VALUES(%s,%s,%s)"
             b1=(self.a,self.b,self.c)
             cursor.execute(s,b1)
             mydb.commit()
             messagebox.showinfo("SPARK assosiation","You are successfully registered !")
         else:
             messagebox.showinfo("SPARK assosiation","You are Already registered !")
             
         self.rog.mainloop()
     def cap(self):
         import cv2
         cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
         cam.set(3, 640) 
         cam.set(4, 480) 
         detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
         face_id = self.e1.get()
         print("Taking samples, look at camera ....... ")
         count = 0
         while True:
              ret, img = cam.read() 
              converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
              faces = detector.detectMultiScale(converted_image, 1.3, 5)
              for (x,y,w,h) in faces:
                  cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                  count += 1
                  cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])
                  cv2.imshow('image', img)

              k = cv2.waitKey(100) & 0xff 
              if k == 27: 
                  break
              elif count >= 10:
                  break
         print("Samples taken now closing the program....")
         

     def train(self):
         import cv2
         import numpy as np
         from PIL import Image #pillow package
         import os
         path = 'samples' # Path for samples already taken
         recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
         detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
         def Images_And_Labels(path): # function to fetch the images and labels
             imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
             faceSamples=[]
             ids = []
             for imagePath in imagePaths: # to iterate particular image path
                 gray_img = Image.open(imagePath).convert('L') # convert it to grayscale
                 img_arr = np.array(gray_img,'uint8') #creating an array
                 id = int(os.path.split(imagePath)[-1].split(".")[1])
                 faces = detector.detectMultiScale(img_arr)
                 for (x,y,w,h) in faces:
                     faceSamples.append(img_arr[y:y+h,x:x+w])
                     ids.append(id)
             return faceSamples,ids
         print ("Training faces. It will take a few seconds. Wait ...")
         faces,ids = Images_And_Labels(path)
         recognizer.train(faces, np.array(ids))
         recognizer.write('trainer/trainer.yml')  # Save the trained model as trainer.yml
         print("Model trained, Now we can recognize your face.")

         
    

ob=maincode()
ob.code()
