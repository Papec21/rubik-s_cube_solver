import cv2

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

    cv2.rectangle(frame, (180, 100), (460, 380), (255, 255, 255), 3)
    cv2.imshow("Robot Eye - press 'q' to quit", frame)

    # Stop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the windows
cap.release()
cv2.destroyAllWindows()