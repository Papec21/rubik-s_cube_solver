import cv2
import numpy as np

# Need to make red and orange easier to distinguish
colors = {
    "white": ([0, 0, 150], [180, 50, 255]),
    "yellow": ([20, 100, 150], [35, 255, 255]),
    "green": ([40, 100, 150], [80, 255, 255]),
    "blue": ([100, 100, 150], [130, 255, 255]),
    "orange": ([10, 100, 150], [20, 255, 255]),
    "red": ([0, 100, 150], [9, 255, 255])
}

# Walls of rubik's cube
walls = ["chuj"]

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
    
    # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # print(f"Current Resolution: {width}x{height}")

    # Need a formula to make it scalable to every resolution
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

            for color_name, (lower, upper) in colors.items():
                lower_color = np.array(lower, dtype="uint8")
                upper_color = np.array(upper, dtype="uint8")

                mask = cv2.inRange(roi_hsv, lower_color, upper_color)

            # Counting every white enough pixel
                pixel_count = cv2.countNonZero(mask)
            
            # If it's white enough we add "W" to kociemba_notation
                if pixel_count > 3100:
                    cv2.putText(frame, color_name[:3], (x1 + 30, y1 + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
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