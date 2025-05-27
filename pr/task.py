import cv2
import numpy as np

# Камераны қосу
cap = cv2.VideoCapture(0)

# Адамның бетін анықтау үшін классификатор
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Сұр түсті сурет (бет табу үшін)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # --- 1) Бетті табу ---
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Adam', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # --- 2) Ручканы табу ---
    # Сұр түске айналдырамыз
    gray_pen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Шумен тазалау
    blurred = cv2.GaussianBlur(gray_pen, (5, 5), 0)

    # Шекараларды табу (Canny edge detection)
    edged = cv2.Canny(blurred, 30, 100)

    # Контурларды табу
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:  # Кішкене контурларды өткізіп жібереміз
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = max(w, h) / float(min(w, h))

            if aspect_ratio > 2:  # Бұрын 2 еді, енді 1.7 қылып қатты жуандау ручкаларды да өткіземіз
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, 'Ruchka', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Нәтижені көрсету
    cv2.imshow('Camera', frame)

    # 'q' басқанда тоқтау
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
