#PRZESUWANIE STRON RĘKĄ

import cv2
import numpy as np
import pyautogui

# Ładujemy model do wykrywania ręki
hand_cascade = cv2.CascadeClassifier("C:/Users/Damian/Documents/Projekty_szkoleniowe_Python/Hand.xml")

# Uruchamiamy kamerę
cap = cv2.VideoCapture(0)

while True:
    # Pobieramy klatkę z kamery
    ret, frame = cap.read()

    # Konwertujemy obraz na odcienie szarości
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Wykrywamy ręce na obrazie
    hands = hand_cascade.detectMultiScale(gray,minSize = (50,50))
    
    # Dla każdej wykrytej ręki rysujemy prostokąt
    for (x,y,w,h) in hands:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # Jeśli ręka jest w lewej części obrazu, wykonujemy przewijanie w górę
        if x < frame.shape[1] / 2:
            pyautogui.scroll(-50)
        # J eśli ręka jest w prawej części obrazu, wykonujemy przewijanie w dół
        elif x > frame.shape[1] / 2:
            pyautogui.scroll(50)

    # Wyświetlamy obraz z rękami
    cv2.imshow('frame',frame)
    key = cv2.waitKey(50)
    if key == 27: 
        break


# Zwalniamy kamerę i zamykamy okno
cap.release()
cv2.destroyAllWindows()