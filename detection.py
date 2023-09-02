import cv2
import numpy as np

def detection(img,color):

    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # First blur to reduce noise prior to color space conversion
    img_blur = cv2.medianBlur(img_bgr, 3)
    # Convert to Lab color space, we only need to check one channel (a-channel) for red here
    img_lab = cv2.cvtColor(img_blur, cv2.COLOR_BGR2Lab)
    
    if color == "Red":
        img_lab_red = cv2.inRange(img_lab, np.array([20, 150, 150]), np.array([190, 255, 255]))
    elif color == "Green":
        img_lab_red = cv2.inRange(img_lab, np.array([20, 0, 160]), np.array([150, 90, 255]))
    elif color == "Blue":
        img_lab_red = cv2.inRange(img_lab, np.array([20, 0, 0]), np.array([255, 140, 100]))
    elif color == "Yellow":
        img_lab_red = cv2.inRange(img_lab, np.array([20, 60, 120]), np.array([255, 100, 255]))
    
    # Second blur to reduce more noise, easier circle detection
    img_lab_red = cv2.GaussianBlur(img_lab_red, (5, 5), 2, 2)
    # Use the Hough transform to detect circles in the image
    detected_circles = cv2.HoughCircles(img_lab_red, cv2.HOUGH_GRADIENT, 1, img_lab_red.shape[0] / 8, 
                               param1 = 100, param2 = 18, minRadius=5, maxRadius=1000)

    # Draw circles that are detected.
    if detected_circles is not None: 
        # Convert the circle parameters a, b and r to integers.
        pt = np.round(detected_circles[0, :]).astype("int")
        xcorner = np.array([pt[0, 0] - pt[0, 2], pt[0, 0] + pt[0, 2], pt[0, 0] - pt[0, 2], pt[0, 0] + pt[0, 2]])
        ycorner = np.array([pt[0, 1] - pt[0, 2], pt[0, 1] - pt[0, 2], pt[0, 1] + pt[0, 2], pt[0, 1] + pt[0, 2]])
        cv2.rectangle(img, (xcorner[0], ycorner[0]), (xcorner[3], ycorner[3]),
                color = (0, 255, 0), thickness = 2)
    else:
        xcorner = [np.nan, np.nan, np.nan, np.nan]
        ycorner = [np.nan, np.nan, np.nan, np.nan]
        
    return xcorner, ycorner, img