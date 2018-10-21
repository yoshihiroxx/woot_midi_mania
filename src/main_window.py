
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from widgets.config_widget import ConfigWidget

class WmmMainWindow(QMainWindow):
    def __init__(self, controller, model):
        super().__init__()
        self.controller =controller
        self.model = model
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300, 250,150)
        self.setWindowTitle('Woot Music Keyboard')
        self.setCentralWidget(ConfigWidget(self.controller, self.model['available_ports']))
