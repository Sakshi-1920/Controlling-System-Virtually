

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

class Virtual_Mouse:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1920x1080+0+0') 
        self.root.title('VIRTUAL SYSTEM CONTROLLER')
        
        title_label=Label(self.root,text="AI VIRTUAL MOUSE",font=("times new roman",25,"bold"),bg="#FFD700",fg="black")
        title_label.place(x=0,y=0,width=1920,height=55)
        
        img=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\9.png')
        img=img.resize((1920,760),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        flabel=Label(self.root,image=self.photoimg)
        flabel.place(x=0,y=65,width=1920,height=920)
        
        title1_button=Button(self.root,text="AI VIRTUAL MOUSE",command=self.mouse,cursor="hand2",font=("times new roman",15,"bold"),bg="#AAFF00",fg="black")
        title1_button.place(x=800,y=930,width=300,height=45)
    
    def mouse(self):
        width = 640             # Width of Camera
        height = 480            # Height of Camera
        frameR = 100            # Frame Rate
        smoothening = 8         # Smoothening Factor
        prev_x, prev_y = 0, 0   # Previous coordinates
        curr_x, curr_y = 0, 0   # Current coordinates

        cap = cv2.VideoCapture(0)   # Getting video feed from the webcam
        cap.set(3, width)           # Adjusting size
        cap.set(4, height)

        detector = ht.handDetector(maxHands=1)                  # Detecting one hand at max
        screen_width, screen_height = autopy.screen.size()      # Getting the screen size
        while True:
            success, img = cap.read()
            img = detector.findHands(img)                       # Finding the hand
            lmlist, bbox = detector.findPosition(img)           # Getting position of hand

            if len(lmlist)!=0:
                x1, y1 = lmlist[8][1:]
                x2, y2 = lmlist[12][1:]

                fingers = detector.fingersUp()      # Checking if fingers are upwards
                cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)   # Creating boundary box
                if fingers[1] == 1 and fingers[2] == 0:     # If fore finger is up and middle finger is down
                    x3 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
                    y3 = np.interp(y1, (frameR, height-frameR), (0, screen_height))

                    curr_x = prev_x + (x3 - prev_x)/smoothening
                    curr_y = prev_y + (y3 - prev_y) / smoothening

                    autopy.mouse.move(screen_width - curr_x, curr_y)    # Moving the cursor
                    cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                    prev_x, prev_y = curr_x, curr_y

                if fingers[1] == 1 and fingers[2] == 1:     # If fore finger & middle finger both are up
                    length, img, lineInfo = detector.findDistance(8, 12, img)

                    if length < 40:     # If both fingers are really close to each other
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                        #autopy.mouse.click(RIGHT_BUTTON)
                        pyautogui.click(button="right")
                        time.sleep(0)
                        # Perform Click
                if fingers[0] == 1 and fingers[1] == 1:
                        length, img, lineInfo = detector.findDistance(8, 12, img)
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                        pyautogui.click(button="left")
                        time.sleep(0)
                if fingers[0]==1:
                    pyautogui.scroll(-50)
                if fingers[4]==1:
                    pyautogui.scroll(10)
                if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                    break

            cTime = time.time()
            pTime =0
            fps = 1/(cTime-pTime)
        
            
            
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        
if __name__ == '__main__':
    root=Tk()
    obj=Virtual_Mouse(root)
    root.mainloop()  
