import sys

from PyQt5.QtWidgets import QLabel, QComboBox, QVBoxLayout
from PyQt5.QtCore import *

class WmmComboBox(QComboBox):
    new_signal = pyqtSignal('int', 'int')

    def __init__(self, parent=None):

        super(WmmComboBox, self).__init__(parent)
        self.lastSelectedId = 0
        self.activated.connect(self.onActivated)

    def onActivated(self, id):
        self.new_signal.emit(self.lastSelectedId, id)
        self.lastSelectedId = id
