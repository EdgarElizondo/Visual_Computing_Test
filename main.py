import sys
from webcam import webcam
from ComboBox import combo_box
from button_double import button_double_text
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class box(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):

    cam = webcam(QSize(640, 360))

    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.cam.setup_camera(self.video, 
                              play = self.video_button, 
                              detection = self.detection_button,
                              color = self.color_qbox,
                              coord1 = self.text_corner1,
                              coord2 = self.text_corner2,
                              coord3 = self.text_corner3,
                              coord4 = self.text_corner4)

    def setup_ui(self):
        """Initialize widgets.
        """
        # Create Layout
        main_layout = QHBoxLayout()
        video_control_layout = QVBoxLayout()
        video_layout = QVBoxLayout()
        control_layout = QHBoxLayout()
        parameter_main_layout = QVBoxLayout()
        parameter1_layout = QVBoxLayout()
        parameter2_layout = QVBoxLayout()
        table_layout = QVBoxLayout()

        
        # Video Layout ______________________________________________________________________________________
        self.video = QLabel()
        self.video.setFixedSize(self.cam.video_size)
        video_layout.addWidget(self.video)
        video_control_layout.addLayout(video_layout)

        # Parameter 1 Layout ________________________________________________________________________________
        # Set Circule color
        self.text_set_color = QLabel("Set circule color detection")
        self.text_set_color.setFixedSize(QSize(180,15))
        # Option Button
        self.color_qbox = combo_box(["Red","Green","Blue","Yellow"])
        # Show rectangle coordinates
        self.text_coordinates = QLabel("Rectangle corners coordinates:")
        self.text_coordinates.setFixedSize(QSize(180,15))
        self.text_corner1 = QLabel("Corner 1:")
        self.text_corner1.setFixedSize(QSize(180,30))
        self.text_corner2 = QLabel("Corner 2:")
        self.text_corner2.setFixedSize(QSize(180,30))
        self.text_corner3 = QLabel("Corner 3:")
        self.text_corner3.setFixedSize(QSize(180,30))
        self.text_corner4 = QLabel("Corner 4:")
        self.text_corner4.setFixedSize(QSize(180,30))
        # Show positions
        self.table = QLabel()
        self.table.setFixedWidth(500)
        self.show_pos_button = button_double_text("Show Position","Hide Position","modified_layout",table_layout,self.table)
        # Add widgets to layout
        parameter1_layout.addWidget(self.text_set_color)
        parameter1_layout.addWidget(self.color_qbox)
        parameter1_layout.addWidget(self.text_coordinates)
        parameter1_layout.addWidget(self.text_corner1)
        parameter1_layout.addWidget(self.text_corner2)
        parameter1_layout.addWidget(self.text_corner3)
        parameter1_layout.addWidget(self.text_corner4)
        parameter1_layout.addWidget(QLabel())
        parameter1_layout.addWidget(self.show_pos_button)
        parameter_main_layout.addLayout(parameter1_layout)
        # Parameter 2 Layout ________________________________________________________________________________
        self.save_pos_button = QPushButton("Save Positions")
        parameter2_layout.addWidget(self.save_pos_button)
        parameter_main_layout.addLayout(parameter2_layout)
        
        # Control Layout ____________________________________________________________________________________
        self.video_button = button_double_text("Stop Video","Play Video")
        self.detection_button = button_double_text("Stop Detection","Start Detection")
        #print(self.detection_button.text())
        control_layout.addWidget(self.video_button)
        control_layout.addWidget(self.detection_button)
        video_control_layout.addLayout(control_layout)
        
        # Main Layout _______________________________________________________________________________________
        main_layout.addLayout(video_control_layout)
        main_layout.addLayout(parameter_main_layout)
        main_layout.addLayout(table_layout)

        # Set main layout
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
