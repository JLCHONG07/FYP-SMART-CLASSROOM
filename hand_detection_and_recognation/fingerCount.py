from cv2 import cv2
import time
import os

from hand_detection_and_recognation import handTrackMod as htm
from module.answering.answeringClass import Answer



widthCam, heightCam = 640, 480

def rmStartMode2():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    cap.set(3, widthCam)
    cap.set(4, heightCam)
    totalFingers = 0
    detector = htm.handDetector(detectionCon=0.75)
    tipIds = [4, 8, 12, 16, 20]
    aCount = 0
    bCount = 0
    cCount = 0
    dCount = 0
    #highestCount=0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
       
        lmList = detector.findPosition(img, draw=False)
        leftOrRight=detector.findLeftOrRight()
        #print("LeftOrRight:",leftOrRight)
        #print(lmList)

        if len(lmList) != 0:
            fingers = []

            # For Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                

            # count total fingers
            #print(fingers)
            totalFingers = fingers.count(1)
           
            current_select=None
            selected_option=None
            #adding compare left to avoid the easily change of current selection and only count for left hand gestures only
            if leftOrRight =="Left" and fingers==[0,1,0,0,0]:
                    aCount+=1
                    current_select="1"
                    #print("A counter: ", aCount)
                    
            elif leftOrRight =="Left" and fingers==[0,1,1,0,0]:
                    bCount+=1
                    current_select = "2"
                    #print("B counter: ", bCount)
                    
            elif leftOrRight =="Left" and fingers==[0,0,1,1,1]:
                    cCount+=1
                    current_select="3"
                    #print("C counter: ", cCount)
                   
            elif leftOrRight =="Left"  and  fingers==[0,1,1,1,1]:
                    dCount+=1
                    current_select="4"
                    #print("D counter: ", dCount)
                    
            currentSelection(img,current_select)
 
            #Right hand is the gesture for confirm with rock gestures
            if leftOrRight =="Right" and totalFingers==0 :
                    if aCount > bCount and aCount > cCount and aCount> dCount:
                        selected_option="1"
                        #calOccurence(img,selected_option)
                    elif bCount > aCount and bCount > cCount and bCount > dCount:
                        selected_option="2"
                        #calOccurence(img,selected_option)
                    elif cCount > aCount and cCount >bCount and cCount>dCount:
                        selected_option="3"
                        #calOccurence(imgselected_option)
                    elif dCount > aCount and dCount >bCount and dCount>cCount:
                        selected_option="4"
                        #calOccurence(img,selected_option)
            calOccurence(img,selected_option)

            #print("selected_option is:",selected_option)
            #calOccurence(img,selected_option)
            #print(totalFingers)
            #Right hand for reset using paper gesture
            if leftOrRight =="Right" and fingers==[1,1,1,1,1]:
                    aCount = 0
                    bCount = 0
                    cCount = 0
                    dCount = 0
            calOccurence(img,selected_option)
            



        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, f'FPS:{int(fps)}', (10, 30),
                    cv2.FONT_HERSHEY_PLAIN, 3, (100, 255, 0), 3, cv2.LINE_AA)


        # cv2.putText(img,f'FPS:{int(fps)}',(50,50),
        # cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        webFrame=  cv2.imencode('.jpg', img)[1].tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + webFrame + b'\r\n'
        #cv2.imshow("Image", img)
        #cv2.waitKey(1)


def currentSelection(img,totalFingers):
    
    cv2.putText(img,"Current Selection: "+ str(totalFingers)+".", (45, 345),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


        
def calOccurence(img, totalFingers):

    cv2.putText(img,"Selected Option: "+ str(totalFingers)+".", (45, 375),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    if totalFingers is not None:
        Answer._answered=totalFingers
