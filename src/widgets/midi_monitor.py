from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from components.combo_box import WmmComboBox

class ConfigWidget(QWidget):
    def __init__(self, controller, model):
        super().__init__()
        self.model = model
        self.controller = controller

        list = QListView()
        list.setWindowTitle('MIDI')
        list.setMinimumSize(600, 400)
        list.setModel(model)

        self.setLayout(vbox)
        # self.setStyleSheet("background-color: lightblue")

    def handlePort(self, previous_id, current_id):
        self.controller.changePort(current_id)
        print('changed port ', current_id)
        # midiout.open_port( id)

    def handleChannel(self, id):
        self.controller.updateChannel(id)
