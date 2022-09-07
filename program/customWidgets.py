from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel, QSizePolicy, QCheckBox
from PySide6.QtCore import Qt

class customSlider(QWidget):
	def __init__(self, parent = None, label = '',minVal = 0, maxVal = 100, pageStep= 1, currValue = -1, autoMode = False, autoValue = True, *args, **kwargs):
		super(customSlider, self).__init__(parent = parent, *args, **kwargs)
		if(currValue == -1):
			currValue == minVal
		self.pageStep = pageStep
		self.maxVal = maxVal
		self.minVal = minVal
		layout = QHBoxLayout()
		self.setLayout(layout)
		self.addLabel(label)
		self.addSlider(currValue)
		self.addValueLabel(currValue)
		self.autoModeWidget = None
		if(autoMode):
			self.addAutoMode(autoValue)
		self.connFuncList = list()
		self.makeConnections()

	def addLabel(self, label):
		self.labelWidget = QLabel(label)
		self.layout().addWidget(self.labelWidget)

	def setLabel(self, label=''):
		self.labelWidget.setText(label)

	def addSlider(self, currValue):
		self.sliderWidget = QSlider(Qt.Orientation.Horizontal, self)
		self.sliderWidget.setRange(self.minVal, self.maxVal)
		self.sliderWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.sliderWidget.setValue(currValue)
		self.sliderWidget.setSingleStep(self.pageStep)
		self.sliderWidget.setPageStep(self.pageStep)
		self.layout().addWidget(self.sliderWidget)

	def addValueLabel(self,currValue):
		self.currValueWidget = QLabel(str(currValue))
		self.currValueWidget.setFixedSize(50, 10)
		self.layout().addWidget(self.currValueWidget)

	def addAutoMode(self, state):
		self.autoModeWidget = QCheckBox("Auto", self)
		self.autoModeWidget.setChecked(state)
		self.layout().addWidget(self.autoModeWidget)

	def validateValue(self, val):
		val -= (val % self.pageStep)
		if(val > self.maxVal):
			val = self.maxVal
		elif(val < self.minVal):
			val = self.minVal
		return val

	def setValue(self, val, state=None):
		if(self.autoModeWidget is not None and state is None):
			state = self.autoModeWidget.isChecked()
		if(state is None):
			state = False
		self.setSliderValue(val)
		val = self.validateValue(val)
		if(self.autoModeWidget):
			self.autoModeWidget.setChecked(state)
		for func in self.connFuncList:
			func(val,state)

	def setAutoMode(self, state):
		val = self.sliderWidget.value()
		self.setValue(val = val, state = state)

	def makeConnections(self):
		self.sliderWidget.valueChanged.connect(self.setCurrentValue)
		self.sliderWidget.valueChanged.connect(self.setValue)
		if(self.autoModeWidget):
			self.autoModeWidget.stateChanged.connect(self.setAutoMode)

	def setSliderValue(self, val):
		self.sliderWidget.setValue(val)
		self.setCurrentValue(val)

	def setCurrentValue(self,val):
		self.currValueWidget.setText(str(val))

	def addFunc(self,func):
		self.connFuncList.append(func)

class customCheckBox(QWidget):
	def __init__(self, parent, label = '', feature = '', state = False, *args, **kwargs):
		super(customCheckBox, self).__init__(parent=parent, *args, **kwargs)
		self.feature = feature
		layout = QHBoxLayout()
		self.setLayout(layout)
		self.addLabel(label)
		self.addCheckBox(state)
		self.connFuncList = list()
		self.makeConnections()

	def addLabel(self, label):
		self.labelWidget = QLabel(label)
		self.layout().addWidget(self.labelWidget)

	def addCheckBox(self,state):
		self.checkBoxWidget = QCheckBox(self)
		self.setCheckState(state)
		self.layout().addWidget(self.checkBoxWidget)

	def addFunc(self,func):
		self.connFuncList.append(func)

	def makeConnections(self):
		self.checkBoxWidget.valueChanged.connect(self.setValue)

	def setValue(self, val):
		for func in self.connFuncList:
			func(val,False)
