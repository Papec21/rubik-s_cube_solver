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

    # Need a formula to make it scalable to every resolution
    cv2.rectangle(frame, (185, 105), (455, 375), (255, 255, 255), 1)
    for row in range(3):
        for col in range(3):
            x1 = col * 90 + 185
            y1 = row * 90 + 105
            x2 = (col + 1) * 90 + 185
            y2 = (row + 1) * 90 + 105
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 1)

    cv2.putText(frame, "Press 'q' to quit", (29, 31), cv2.FONT_HERSHEY_SIMPLEX, 1.01, (0, 0, 0), 5)
    cv2.putText(frame, "Press 'q' to quit", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("HAI HAI HAI!!! OMG :3333", frame)

    # Stop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the windows
cap.release()
cv2.destroyAllWindows()