from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from components.combo_box import WmmComboBox

class ConfigWidget(QWidget):
    def __init__(self, controller, model):
        super().__init__()
        self.model = model
        self.controller = controller
        vbox = QHBoxLayout(self)
        vbox.addWidget(QLabel('port'))

        self.cb = WmmComboBox()
        self.cb.setModel(self.model)
        self.cb.new_signal.connect(self.handlePort)
        vbox.addWidget(self.cb)


        vbox.addWidget(QLabel('channel'))
        self.channel_selector = QComboBox()
        self.channel_selector.addItems(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        self.channel_selector.currentIndexChanged.connect(self.handleChannel)
        vbox.addWidget(self.channel_selector)

        self.setLayout(vbox)
        # self.setStyleSheet("background-color: lightblue")

    def handlePort(self, previous_id, current_id):
        self.controller.changePort(current_id)
        print('changed port ', current_id)
        # midiout.open_port( id)

    def handleChannel(self, id):
        self.controller.updateChannel(id)
