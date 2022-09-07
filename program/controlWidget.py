from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QSizePolicy, QSlider, QLabel, QCheckBox, QPushButton
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import Qt
from videoProcAmp import VideoProcAmp
from customWidgets import customSlider, customCheckBox
from globalVariables import VideoProcAmpFlags
class ControlWidget(QWidget):
    def __init__(self,mainWindow = None, *args, **kwargs):
        super(ControlWidget,self).__init__(*args,**kwargs)
        self._mainWindow = mainWindow
        self.cameraListWidget = None
        self.mediaDevices = QMediaDevices()
        self.currCamDesc = ""
        self.defaultValue = dict()
        self.videoProcAmp = VideoProcAmp()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setLayout(layout)
        self.addWidgets()
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

    def sliderWrapper(self,feature):
        def sliderFunc(value,state):
            self.videoProcAmp.setValue(feature, value, state)
        return sliderFunc

    def checkBoxWrapper(self, feature):
        def checkBoxFunc(value, state):
            self.videoProcAmp.setValue(feature, value, state)
        return checkBoxFunc

    def addsettingWidget(self, label = '', feature = ''):
        rangeValue = self.videoProcAmp.getRange(feature)
        settingWidget = None
        if(rangeValue):
            minValue, maxValue, pageStep, defaultVal, autoModeState = rangeValue
            currValue, autoMode = self.videoProcAmp.getValue(feature)
            self.defaultValue[feature] = defaultVal
            if(autoModeState & 0x1):
                autoModeState = True
            else:
                autoModeState = False
            autoValue = (autoMode == VideoProcAmpFlags['VideoProcAmp_Flags_Auto'])
            settingWidget = customSlider(parent = self, label = label, minVal = minValue, maxVal = maxValue, pageStep= pageStep, currValue = currValue, autoMode = autoModeState, autoValue = autoValue)
            settingWidget.addFunc(self.sliderWrapper(feature = feature))
            self.layout().addWidget(settingWidget)
        return settingWidget

    def addCheckBoxWidget(self, label, feature):
        rangeValue = self.videoProcAmp.getRange(feature)
        checkBoxWidget = None
        if(rangeValue):
            minValue, maxValue, pageStep, defaultVal, autoModeState = rangeValue
            self.defaultValue[feature] = defaultVal
            currValue, autoMode = self.videoProcAmp.getValue(feature)
            checkBoxWidget = customCheckBox(parent = self, label = label, feature = feature, state = currValue)
            checkBoxWidget.addFunc(self.checkBoxWrapper(feature=feature))
        return checkBoxWidget

    def addBrightness(self):
        label = "Brightness"
        feature = "VideoProcAmp_Brightness"
        self.brightnessWidget = self.addsettingWidget(label, feature)

    def addWhiteBalance(self):
        label = "White Balance"
        feature = "VideoProcAmp_WhiteBalance"
        self.whiteBalanceWidget = self.addsettingWidget(label = label, feature = feature)

    def addContrast(self):
        label = "Contrast"
        feature = "VideoProcAmp_Contrast"
        self.contrastWidget = self.addsettingWidget(label = label, feature = feature)

    def addHue(self):
        label = "Hue"
        feature = "VideoProcAmp_Hue"
        self.hueWidget = self.addsettingWidget(label = label, feature = feature)

    def addSaturation(self):
        label = "Saturation"
        feature = "VideoProcAmp_Saturation"
        self.saturationWidget = self.addsettingWidget(label = label, feature = feature)

    def addSharpness(self):
        label = "Sharpness"
        feature = "VideoProcAmp_Sharpness"
        self.sharpnessWidget = self.addsettingWidget(label = label, feature = feature)

    def addGamma(self):
        label = "Gamma"
        feature = "VideoProcAmp_Gamma"
        self.gammaWidget = self.addsettingWidget(label = label, feature = feature)

    def addBacklightComp(self):
        label = "Blacklight Comp"
        feature = "VideoProcAmp_BacklightCompensation"
        self.blacklightCompWidget = self.addsettingWidget(label = label, feature = feature)

    def addGain(self):
        label = "Gain"
        feature = "VideoProcAmp_Gain"
        self.gainWidget = self.addsettingWidget(label = label, feature = feature)

    def addColorEnable(self):
        label = "Color Enable"
        feature = "VideoProcAmp_ColorEnable"
        self.colorEnableWidget = self.addCheckBoxWidget(label = label, feature = feature)

    def addDefault(self):
        self.defaultWidget = QPushButton('default',self)
        self.layout().addWidget(self.defaultWidget)
        self.defaultWidget.pressed.connect(self.setDefaultValueAllWidget)

    def setDefaultValueOneWidget(self, widget, feature):
        if(widget):
            widget.setValue(self.defaultValue[feature],True)

    def setDefaultValueAllWidget(self):
        self.setDefaultValueOneWidget(self.brightnessWidget, 'VideoProcAmp_Brightness')
        self.setDefaultValueOneWidget(self.whiteBalanceWidget, 'VideoProcAmp_WhiteBalance')
        self.setDefaultValueOneWidget(self.contrastWidget, 'VideoProcAmp_Contrast')
        self.setDefaultValueOneWidget(self.hueWidget, 'VideoProcAmp_Hue')
        self.setDefaultValueOneWidget(self.saturationWidget, 'VideoProcAmp_Saturation')
        self.setDefaultValueOneWidget(self.sharpnessWidget, 'VideoProcAmp_Sharpness')
        self.setDefaultValueOneWidget(self.gammaWidget, 'VideoProcAmp_Gamma')
        self.setDefaultValueOneWidget(self.blacklightCompWidget, 'VideoProcAmp_BacklightCompensation')
        self.setDefaultValueOneWidget(self.gainWidget, 'VideoProcAmp_Gain')
        self.setDefaultValueOneWidget(self.colorEnableWidget, 'VideoProcAmp_ColorEnable')


    def addWidgets(self):
        self.addCameraList()
        self.addBrightness()
        self.addContrast()
        self.addHue()
        self.addSaturation()
        self.addSharpness()
        self.addGamma()
        self.addColorEnable()
        self.addWhiteBalance()
        self.addBacklightComp()
        self.addGain()
        self.addDefault()

    def changeCamera(self,index):
        self._mainWindow.addCamera(index)