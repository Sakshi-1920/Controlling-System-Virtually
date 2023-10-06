from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
import HandTracking as ht
import autopy  
import pyautogui
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import numpy as np
from Virtual_Mouse import Virtual_Mouse
import os
from assistant import Virtual_Assistant


class Virtual_Controller:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1920x1080+0+0') 
        self.root.title('VIRTUAL SYSTEM CONTROLLER')
        
        # first image
        img=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\1.png')
        img=img.resize((650,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        flabel=Label(self.root,image=self.photoimg)
        flabel.place(x=-10,y=0,width=650,height=200)
        
        # Second image
        img1=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\2.jpg')
        img1=img1.resize((650,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        flabel=Label(self.root,image=self.photoimg1)
        flabel.place(x=630,y=0,width=650,height=200)
        
        # Third image
        img2=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\3.jpg')
        img2=img2.resize((650,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        flabel=Label(self.root,image=self.photoimg2)
        flabel.place(x=1270,y=0,width=650,height=200)
        
        # Background Image
        img3=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\569.jpg')
        img3=img3.resize((1920,800),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=180,width=1920,height=850)
        
        title_label=Label(bg_img,text="VIRTUAL SYSTEM CONTROLLER",font=("times new roman",35,"bold"),bg="orange",fg="black")
        title_label.place(x=-2,y=-2,width=1920,height=55)
        
        img_border=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\6.jpg')
        img_border=img_border.resize((1920,80),Image.ANTIALIAS)
        self.photoimg_border=ImageTk.PhotoImage(img_border)
        
        bg_img1=Label(self.root,image=self.photoimg_border)
        bg_img1.place(x=0,y=920,width=1920,height=80)
        
        #AI Virtual Mouse
        img4=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\4.jpg')
        img4=img4.resize((500,300),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.mouse,cursor="hand2")
        b1.place(x=60,y=250,width=500,height=300)
        
        title1_button=Button(bg_img,text="AI VIRTUAL MOUSE",command=self.mouse,cursor="hand2",font=("times new roman",16,"bold"),bg="white",fg="green")
        title1_button.place(x=60,y=550,width=500,height=35)
        
        #Virtual Assistant
        img5=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\5.jpg')
        img5=img5.resize((500,300),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img,image=self.photoimg5,command=self.assistant,cursor="hand2")
        b2.place(x=700,y=250,width=500,height=300)
        
        titlen_button=Button(bg_img,text="VIRTUAL ASSISTANT",command=self.assistant,cursor="hand2",font=("times new roman",16,"bold"),bg="white",fg="green")
        titlen_button.place(x=700,y=550,width=500,height=35)
        
        #AI Virtual Keyboard
        img6=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\7.png')
        img6=img6.resize((500,300),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img,image=self.photoimg6,command=self.keyboard,cursor="hand2")
        b3.place(x=1350,y=250,width=500,height=300)
        
        title2_button=Button(bg_img,text="AI VIRTUAL KEYBOARD",command=self.keyboard,cursor="hand2",font=("times new roman",16,"bold"),bg="white",fg="green")
        title2_button.place(x=1350,y=550,width=500,height=35)
        
    def mouse(self):
        self.new_window=Toplevel(self.root)
        self.app=Virtual_Mouse(self.new_window)
        
    def assistant(self):
        self.new_window=Toplevel(self.root)
        self.app=Virtual_Assistant(self.new_window)
        
    def keyboard(self):
        os.startfile('C:/Users/SAKSHI SONAR/Desktop/FINAL YEAR PROJECT/dist/vkeyboard/vkeyboard.exe')

if __name__ == '__main__':
    root=Tk()
    obj=Virtual_Controller(root)
    root.mainloop()
