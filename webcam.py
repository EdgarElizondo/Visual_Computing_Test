import cv2
import detection
import numpy as np
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class webcam():
    
    def __init__(self,qSize):
        self.video_size = qSize
        self.width = self.video_size.width()
        self.height = self.video_size.height()

    def setup_camera(self,video,play,detection,color,coord1,coord2,coord3,coord4):
        """Initialize camera.
        """
        # UI Parameters
        self.video = video
        self.play = play
        self.detection = detection
        self.color = color
        self.coord1 = coord1
        self.coord2 = coord2
        self.coord3 = coord3
        self.coord4 = coord4
        # Video Capture
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(10)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        pt1 = np.array([np.nan,np.nan,np.nan,np.nan,])
        pt2 = np.array([np.nan,np.nan,np.nan,np.nan,])
        if self.play.value:
            _, frame = self.capture.read()
            frame = cv2.resize(frame[::,::-1,::-1],(self.width,self.height))
            if self.detection.value:
                pt1, pt2, frame = detection.detection(frame,self.color.textValue)
            self.image = QImage(frame, frame.shape[1], frame.shape[0], 
                        frame.strides[0], QImage.Format_RGB888)
            
        # Conection with UI
        self.video.setPixmap(QPixmap.fromImage(self.image))

        self.coord1.setText(f"Corner 1:\n({pt1[0]}, {pt2[0]})")
        self.coord2.setText(f"Corner 2:\n({pt1[1]}, {pt2[1]})")
        self.coord3.setText(f"Corner 3:\n({pt1[2]}, {pt2[2]})")
        self.coord4.setText(f"Corner 4:\n({pt1[3]}, {pt2[3]})")
