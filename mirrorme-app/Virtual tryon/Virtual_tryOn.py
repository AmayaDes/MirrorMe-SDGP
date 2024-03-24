import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

def Tryon():

    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    shirtfolderPath = "Shirts"
    listShirts = os.listdir(shirtfolderPath)
    imageNumber = 0
    imgButtonRight = cv2.imread('button.png', cv2.IMREAD_UNCHANGED)
    imgButtonLeft = cv2.flip(imgButtonRight, 1)
    counterRight = 0
    counterLeft = 0

    while cap.isOpened():
        # Capture each frame from the webcam
        success, img = cap.read()
        if not success:
            break
        else:
            fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint 11 to 12
            shirtRatioHeightWidth = 581 / 440
            selectionSpeed = 30
        # Find the human pose in the frame
        img = detector.findPose(img)
        # img = cv2.flip(img,1)
        # Find the landmarks, bounding box, and center of the body in the frame
        # Set draw=True to draw the landmarks and bounding box on the image
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
        # Check if anybody landmarks are detected
        if lmList:
            lm11 = lmList[11][1:3]
            lm12 = lmList[12][1:3]
            lmOther= lmList[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]
            imgShirt = cv2.imread(os.path.join(shirtfolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
            widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
            print(widthOfShirt)
            imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
            currentScale = (lm11[0] - lm12[0]) / 190
            offset = int(44 * currentScale), int(48 * currentScale)

            try:
                img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
            except:
                pass

            img = cvzone.overlayPNG(img, imgButtonRight, (1600, 500))
            img = cvzone.overlayPNG(img, imgButtonLeft, (160, 500))

            if lmList[16][1] < 400:
                counterRight += 1
                cv2.ellipse(img, (220, 565), (66, 66), 0, 0,
                            counterRight * selectionSpeed, (0, 255, 0), 20)
                if counterRight * selectionSpeed > 360:
                    counterRight = 0
                    if imageNumber < len(listShirts) - 1:
                        imageNumber += 1
            elif lmList[15][1] > 1400:
                counterLeft += 1
                cv2.ellipse(img, (1660, 565), (66, 66), 0, 0,
                            counterLeft * selectionSpeed, (0, 255, 0), 20)
                if counterLeft * selectionSpeed > 360:
                    counterLeft = 0
                    if imageNumber > 0:
                        imageNumber -= 1
            else:
                counterRight = 0
                counterLeft = 0

        _, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
    cap.release()