import cv2
import numpy as np

# Storage for notation
kociemba_scramble = []

# Use my default built-in webcam
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Camera is running Press 'q' to quit.")

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not receive frame.")
        break

    # Convert BGR to HSV color code
    # hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Gotta add all colors :(((
    # Colors (Gotta move them to config later)
    white_lower = np.array([0, 0, 150], np.uint8)
    white_upper = np.array([180, 50, 255], np.uint8)

    yellow_lower = np.array([20, 100, 150], np.uint8)
    yellow_upper = np.array([35, 255, 255], np.uint8)

    green_lower = np.array([40, 100, 150], np.uint8)
    green_upper = np.array([80, 255, 255], np.uint8)

    blue_lower = np.array([100, 100, 150], np.uint8)
    blue_upper = np.array([130, 255, 255], np.uint8)

    orange_lower = np.array([10, 100, 150], np.uint8)
    orange_upper = np.array([20, 255, 255], np.uint8)

    red_lower = np.array([0, 100, 150], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    # white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)

    # Reduce color noise
    kernal = np.ones((5, 5), "uint8")

    # white_mask = cv2.dilate(white_mask, kernal)
    # res_white = cv2.bitwise_and(frame, frame, mask=white_mask)  
    
    # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # print(f"Current Resolution: {width}x{height}")

    # Need a formula to make it scalable to every resolution
    # cv2.rectangle(frame, (185, 105), (455, 375), (252, 3, 211), 1)
    for row in range(3):
        for col in range(3):
            x1 = col * 90 + 185
            y1 = row * 90 + 105
            x2 = (col + 1) * 90 + 185
            y2 = (row + 1) * 90 + 105
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (252, 3, 211), 1)

            # Frames inside rectangles
            roi = frame[y1:y2, x1:x2]
            roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(roi_hsv, white_lower, white_upper)
            mask = cv2.dilate(mask, kernal)

            # Counting every white enough pixel
            pixel_count = cv2.countNonZero(mask)
            
            # If it's white enough we add "W" to kociemba_notation
            if pixel_count > 4100:
                cv2.putText(frame, "W", (x1 + 30, y1 + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                # kociemba_scramble.append("W")

    cv2.putText(frame, "Press 'q' to quit", (29, 31), cv2.FONT_HERSHEY_SIMPLEX, 1.01, (0, 0, 0), 5)
    cv2.putText(frame, "Press 'q' to quit", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("HAI HAI HAI!!! OMG :3333", frame)
      
    # Stop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the windows
cap.release()
cv2.destroyAllWindows()