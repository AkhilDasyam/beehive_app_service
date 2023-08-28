import cv2

def capture_image():
    # Open the default camera (usually the built-in webcam)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Failed to open camera.")
        return None

    # Capture a single frame
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        camera.release()
        return None

    # Release the camera
    camera.release()

    return frame
