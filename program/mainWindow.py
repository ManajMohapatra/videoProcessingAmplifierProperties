from PySide6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout)
from PySide6.QtMultimedia import QMediaDevices, QMediaCaptureSession, QCamera
from PySide6.QtMultimediaWidgets import QVideoWidget
from cameraWidget import CameraWidget
from controlWidget import ControlWidget
from logDefs import critical, error, warning, info, debug, info

class MainWindow(QMainWindow):
    def __init__(self, title = "",*args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self._camera = None
        self.setTitle(title)
        self.addCentralWidget()
        self.addCameraWidget()
        self.addControlWidget()
        self.show()

    def setTitle(self,title):
        """ title of the main window """
        if(title == ""):
            title = "Camera Window"
        self.setWindowTitle(title)

    def addCentralWidget(self):
        """ create central widget """
        # set layout of main window
        layout = QHBoxLayout()

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)

    def removeCamera(self):
        if self._camera and self._camera.isActive():
            self._camera.stop()
            del self._camera
        self._camera = None

    def addCamera(self, index = 0):
        if(self._camera is not None):
            self.removeCamera()
        cameras = QMediaDevices.videoInputs()
        if(index >= len(cameras) and len(cameras) > 0):
            self._camera = CameraWidget(cameras[0])
        elif(index <= len(cameras)):
            self._camera = CameraWidget(cameras[index])
        else:
            self._camera = None
        if(self._camera is None):
            warning("Camera not found")
            return
        self._camera.errorOccurred.connect(self.cameraError)
        self._camera.start()
        self._capture_session.setCamera(self._camera)


    def addCameraWidget(self):
        """ Add camera widget """

        # create camera finder
        self._camera_viewfinder = QVideoWidget()

        # create camera session
        self._capture_session = QMediaCaptureSession()
        self._capture_session.setVideoOutput(self._camera_viewfinder)
        self.centralWidget.layout().addWidget(self._camera_viewfinder)


    def cameraError(self, error, error_string):
        error("CAMERA ERROR: ",error_string)

    def addControlWidget(self):
        self.controlWidget = ControlWidget(mainWindow=self)
        self.centralWidget.layout().addWidget(self.controlWidget)

    def closeEvent(self, event):
        if self._camera and self._camera.isActive():
            self._camera.stop()
        event.accept()