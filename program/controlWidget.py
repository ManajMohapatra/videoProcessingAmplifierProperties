from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QSizePolicy, QSlider, QLabel, QCheckBox
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import Qt

class ControlWidget(QWidget):
    def __init__(self,mainWindow = None, *args, **kwargs):
        super(ControlWidget,self).__init__(*args,**kwargs)
        self._mainWindow = mainWindow
        self.cameraListWidget = None
        self.mediaDevices = QMediaDevices()
        self.currCamDesc = ""
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.addWidgets()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.mediaDevices.videoInputsChanged.connect(self.updateCameraList)

    def updateCameraList(self):
        self.cameraListWidget.clear()
        cameras = self.mediaDevices.videoInputs()
        selectIndex = 0
        for index, cameraDevice in enumerate(cameras):
            desc = cameraDevice.description()
            self.cameraListWidget.addItem(desc)
            if(self.currCamDesc == desc):
                selectIndex = index
        self.cameraListWidget.setCurrentIndex(selectIndex)
        if(self.currCamDesc != self.cameraListWidget.currentText()):
            self.changeCamera(selectIndex)
            self.currCamDesc = self.cameraListWidget.currentText()

    def addCameraList(self):
        self.cameraListWidget = QComboBox()
        self.cameraListWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        cameras = self.mediaDevices.videoInputs()
        for cameraDevice in cameras:
            self.cameraListWidget.addItem(cameraDevice.description())
        self.layout().addWidget(self.cameraListWidget)
        self.cameraListWidget.currentIndexChanged.connect(self.changeCamera)
        self.changeCamera(self.cameraListWidget.currentIndex())
        self.currCamDesc = self.cameraListWidget.currentText()

    def addWidgets(self):
        self.addCameraList()

    def changeCamera(self,index):
        self._mainWindow.addCamera(index)