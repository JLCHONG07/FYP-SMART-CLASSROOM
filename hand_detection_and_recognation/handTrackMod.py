from cv2 import cv2
import mediapipe as mp
from hand_detection_and_recognation import hand_detection


class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.75, trackCon=0.75):
        self.mode = mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    
    def findHands(self, img, draw=True):
        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        imgRGB = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        imgRGB.flags.writeable = False
        #imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # Draw the hand annotations on the image.
        imgRGB.flags.writeable = True
        img = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms,handedness in zip(self.results.multi_hand_landmarks,self.results.multi_handedness):               
                if draw:
                    #left hand coordinate
                    cx,cy=hand_detection.hand_coordinate(img,handLms,handedness)
                    #right hand coordinate
                    cx2,cy2=hand_detection.hand_coordinate2(img,handLms,handedness)
                    img=cv2.putText(img, f'Left : {str(cx)}  {str(cy)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (100, 255, 0), 3)
                    img=cv2.putText(img, f'Right : {str(cx2)}  {str(cy2)}', (10, 110), cv2.FONT_HERSHEY_PLAIN, 3, (100, 255, 0), 3)
                    #image=cv2.putText(image, f'{str(cy)}', (50, 80), font, 3, (100, 255, 0), 3)
                    #calculation of box surrounded hand
                    brect = hand_detection.calc_bounding_rect(img, handLms)
                    #draw box surrounded hand
                    img = hand_detection.draw_bounding_rect(True, img, brect)
                    #words of left and right
                    img = hand_detection.draw_info_text(
                        img,
                        brect,
                        handedness
                    )
                    self.mpDraw.draw_landmarks(
                    img, handLms,self.mpHands.HAND_CONNECTIONS)
        return img        
                #for id, lm in enumerate(handLms.landmark):
                    #print(id, lm)
                    #h,w,c = img.shape
                    #cx, cy = int(lm.x*w), int(lm.y*h)
                    #print(cx,cy)
                    #if id==0:
                    #cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

    def findPosition(self, img, handNo=0, draw=True):
        
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print id,lm
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id,cx,cy)
                lmList.append([id, cx, cy])
                #if draw:    
                #if id ==4:
                    #cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return lmList
    
    def findLeftOrRight(self):

        if self.results.multi_hand_landmarks:
            for handness in self.results.multi_handedness:
                leftOrRight= handness.classification[0].label[0:]
            return leftOrRight
            






def main():

    cap = cv2.VideoCapture(0)
    detector = handDetector()
    
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) !=0:
            print(lmList[4])


        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()

