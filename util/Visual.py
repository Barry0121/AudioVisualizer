"""
Visual Processing Utility Package for Audio Visualizer

Last Updated: 07/06/2022

Made by: Barry Xue

Description:
A collection of utility functions for processing video and image
"""

from argparse import ArgumentError
import cv2
import os


def display_video_feed(source=0, gray=False):
    """
    This will create a window showing video feed. Press 'q' to terminate the process.

    Example:
    cv2.VideoCapture(0): Means first camera or webcam.
    cv2.VideoCapture(1):  Means second camera or webcam.
    cv2.VideoCapture("file name.mp4"): Means video file.

    :param source: int or str; integer indicates the input device (usually a webcam), string is assumed to be the path to a video file
    :param gray: bool; turns the video gray scale
    """

    if type(source)==int:
        cap = cv2.VideoCapture(source) # Takes in webcam input; this can be another video file as well
    elif type(source)==str:
        # check if the file path is valid
        if os.path.exists(source):
            cap = cv2.VideoCapture(source)
        else:
            raise FileNotFoundError()
    else:
        raise ArgumentError(source, message='Input format isn\'t recognized')

    # Write a loop to continuously take in webcam input frames until some input is taken
    while(True):
        # .read() will return the current frame
        # ret is a flag; it is true when there is an input, false otherwise
        ret, frame = cap.read()

        # Use imshow to display the current frame
        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        # Make 'q' key on keyboard the escape key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Make sure to release the cache and destroy all the image windows after while loop is done
    cap.release()
    cv2.destroyAllWindows()


def save_video_feed(filename='output.avi', source=0, gray=False):
    """
    TODO: Test this function

    This will create a window showing video feed and then save the feed. Press 'q' to terminate the process.

    Example:
    cv2.VideoCapture(0): Means first camera or webcam.
    cv2.VideoCapture(1):  Means second camera or webcam.
    cv2.VideoCapture("file name.mp4"): Means video file.

    :param source: int or str; integer indicates the input device (usually a webcam), string is assumed to be the path to a video file
    :param gray: bool; turns the video gray scale
    """

    if type(source)==int:
        cap = cv2.VideoCapture(source) # Takes in webcam input; this can be another video file as well
    elif type(source)==str:
        # check if the file path is valid
        if os.path.exists(source):
            cap = cv2.VideoCapture(source)
        else:
            raise FileNotFoundError()
    else:
        raise ArgumentError(source, message='Input format isn\'t recognized')

    # Get frame resolution from the caption stream
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)

    # Create a video writing stream
    result = cv2.VideoWriter(filename, fourcc=cv2.VideoWriter_fourcc(*'MJPG'), fps=10, frameSize=size)

    # Write a loop to continuously take in webcam input frames until some input is taken
    while(True):
        # .read() will return the current frame
        # ret is a flag; it is true when there is an input, false otherwise
        ret, frame = cap.read()

        if ret:
            # Use imshow to display the current frame
            if gray:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)

            # Then we store the frame
            result.write(frame)

        else:
            break

        # Make 'q' key on keyboard the escape key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Make sure to release the cache and destroy all the image windows after while loop is done
    cap.release()
    result.release()
    cv2.destroyAllWindows()

    print('Video Saved!')

