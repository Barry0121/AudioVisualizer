"""
Video Capturing Script using CV2

Last Updated: 07/06/2022

Made by: Barry Xue

Description:
This is a boiler plate that can be used on any machine with python3.9 to capture webcam or video file stream.
"""

import cv2

cap = cv2.VideoCapture(0) # Takes in webcam input; this can be another video file as well

# Write a loop to continuously take in webcam input frames until some input is taken
while(True):
    # .read() will return the current frame
    # ret is a flag; it is true when there is an input, false otherwise
    ret, frame = cap.read()

    """If you want to process the video frames, do it here"""

    # Use imshow to display the current frame
    cv2.imshow('frame', frame)

    # Make 'q' key on keyboard the escape key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Make sure to release the cache and destroy all the image windows after while loop is done
cap.release()
cv2.destroyAllWindows()