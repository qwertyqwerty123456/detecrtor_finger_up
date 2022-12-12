import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while True:
    success, img = cap.read()
    hand, img = detector.findHands(img)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [1, 0, 0, 0, 0] or fingerup == [0, 1, 0, 0, 0] \
                    or fingerup == [0, 0, 1, 0, 0] or fingerup == [0, 0, 0, 1, 0] or fingerup == [0, 0, 0, 0, 1]:
                print("1")
            if fingerup == [1, 1, 0, 0, 0] or fingerup == [0, 1, 1, 0, 0] or fingerup == [0, 0, 1, 1, 0] \
                    or fingerup == [0, 0, 0, 1, 1] or fingerup == [1, 0, 0, 0, 1] \
                    or fingerup == [1, 0, 1, 0, 0] or fingerup == [1, 0, 0, 1, 0] or fingerup == [0, 1, 0, 1, 0]\
                    or fingerup == [0, 1, 0, 0, 1] or fingerup == [0, 0, 1, 0, 1] :
                print("2")
            if fingerup == [0, 1, 1, 1, 0] or fingerup == [1, 1, 1, 0, 0] or fingerup == [0, 0, 1, 1, 1] or fingerup == [1, 0, 0, 1, 1] \
                    or fingerup == [1, 1, 0, 0, 1] or fingerup == [1, 0, 1, 1, 0] or fingerup == [0, 1, 0, 1, 1] \
                    or fingerup == [1, 0, 0, 0, 0] or fingerup == [0, 1, 1, 0, 1]:
                print("3")
            if fingerup == [0, 1, 1, 1, 1] or fingerup == [1, 1, 1, 1, 0] or fingerup == [1, 0, 1, 1, 1] or fingerup == [1, 1, 0, 1, 1] \
                    or fingerup == [1, 1, 1, 0, 1]:
                print("4")
            if fingerup == [1, 1, 1, 1, 1]:
                print("5")
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
