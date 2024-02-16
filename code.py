import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Could not open camera")
    exit()
else:
    print("Opened")
# Capture a frame
ret, frame = cap.read()

# Check if the frame is captured successfully
if not ret:
    print("Could not capture frame")
    exit()

# Save the frame to a file
cv2.imwrite('capture.jpg', frame)

# Release the camera
cap.release()
