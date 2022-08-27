import sys
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	cameraMainWindow = MainWindow(title = "My Camera Window")
	sys.exit(app.exec())