import rtmidi
import sys, os
base_path = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(base_path, '..\\woot_music_keyboard\\src')
sys.path.append(src_path)
from PyQt5.QtCore import *

from woot_music_keyboard import WootMusicKeyboard


class Controller( QThread ):
    def __init__(self, model):
        super().__init__()
        self.midiout = rtmidi.MidiOut()
        self.model = model
        self.use_channel = 0
        self.woot_music_keyboard = WootMusicKeyboard()

        self.woot_music_keyboard.on('noteOn', self.noteOnHandler)
        self.woot_music_keyboard.on('noteOff', self.noteOffHandler)

    def noteOnHandler(self, note, vel):
        msg = 0x90 + self.use_channel
        note_on = [msg, note, vel]
        self.midiout.send_message(note_on)
        print(note, vel)

    def noteOffHandler(self, note, vel):
        msg = 0x80 + self.use_channel
        note_off = [msg, note, vel]
        self.midiout.send_message(note_off)


    def changePort( self,  id ):
        self.midiout.close_port()
        print( id )
        if id > 0 :
            self.midiout.open_port(id -1)

    def updateChannel( self, id ):
        self.use_channel = 0

    def getChannel( self, note, vel):
        return self.use_channel

    def sendNoteOn(self, note, vel):
        msg = 0x90 + self.use_channel
        midiout.send_message([msg, note, vel])

    def sendNoteOff(self, note, vel):
        msg = 0x80 + self.use_channel
        midiout.send_message([msg, note, vel])

    def run(self):
        while 1:
            self.woot_music_keyboard.update()
