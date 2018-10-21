import sys
from main_window import WmmMainWindow
from components.combo_box import WmmComboBox
from controller import Controller

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import rtmidi

midiout = rtmidi.MidiOut()
channel = 0


def main():
    app = QApplication(sys.argv)

    available_ports = midiout.get_ports()
    model = {}
    model['available_ports'] = QStringListModel()
    model['available_ports'].setStringList( available_ports )

    # models['channel'] =  QStandardItemModel()


    controller = Controller(model)
    controller.start()


    mainwindow = WmmMainWindow(controller, model)
    mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
