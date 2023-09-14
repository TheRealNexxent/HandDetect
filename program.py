import cv2 as cv #IMPORTING ALL FILES
import pyautogui
import mediapipe as mp

capture = cv.VideoCapture(0)

mhand = mp.solutions.hand
hand = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                      min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

gesture = 'other'
while True:
    ret, frame = capture.read()
    if not ret:
        break
    result = hand.process(frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger_y = hand_landmarks.landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmarks[mp_hands.HandLandmark.THUMB_TIP].y
            middle_finger_y = hand_landmarks.landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
            ring_finger_y = hand_landmarks.landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
            pinky_finger_y = hand_landmarks.landmarks[mp_hands.HandLandmark.PINKY_TIP].y
            # Initializing  gesture variable.
            gesture = 'other'
            # Here we are Updating the gesture based on the various finger positions.
            if index_finger_y > thumb_y:
                gesture = 'pointing up'
            if middle_finger_y > thumb_y:
                gesture = 'pointing down'
            if ring_finger_y > thumb_y:
                gesture = 'stop'
    if gesture == 'pointing up':
        pyautogui.press('volumeup')
    elif gesture == 'pointing down':
        pyautogui.press('volumedown')
    if gesture == 'stop':
        pyautogui.press('playpause')
    cv.imshow('Hand gesture', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()

#End of Program.