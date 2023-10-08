import cv2
import mediapipe as mp
import pyautogui
from math import hypot

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
scroll_active = False
scroll_counter = 0


while True:
    _, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []

    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

    if lmList != []:
        palec2 = x2, y2 = lmList[8][1], lmList[8][2]  # Palec wskazujący
        palec1 = x1, y1 = lmList[12][1],lmList[12][2]  # Palec Środkowy
        cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
        thumb = lmList[4]  # Opuszek kciuka
        index_finger = lmList[8]  # Opuszek palca wskazującego
        middle_finger = lmList[12]  # Opuszek palca środkowego
        ring_finger = lmList[16]  # Opuszek palca serdecznego
        pinky_finger = lmList[20]  # Opuszek małego palca
        index_finger_tip = index_finger[1], index_finger[2]
        middle_finger_tip = middle_finger[1], middle_finger[2]
            # Sprawdzenie, czy wszystkie opuszki palców są powyżej opuszku kciuka
        
        
        
        if all(lm[2] > thumb[2] for lm in [index_finger, middle_finger, ring_finger, pinky_finger]):
            pyautogui.scroll(0,0)
        elif hypot(index_finger_tip[0] - middle_finger_tip[0], index_finger_tip[1] - middle_finger_tip[1]) < 40:
                pyautogui.scroll(50, 20)  # Przesuwanie strony do góry
        elif y1 < img.shape[1] / 2 and y2 < img.shape[1] / 2:
            pyautogui.scroll(-50)  # Przewijanie w górę
    
        elif y1 > img.shape[1] / 2 and y2 > img.shape[1] / 2:
            pyautogui.scroll(50)  # Przewijanie w dół
        
       
    cv2.imshow("Webcam", img)
    key = cv2.waitKey(50)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
