from gtts import gTTS

import PyQt5
from time import ctime
from gtts import gTTS
import os
import pickle
import speech_recognition as sr
import PyQt5.QtCore as coremodule
import PyQt5.QtMultimedia as multimedia
import sys
import pyaudio


class Backend:

    def __init__(self):
        self.app = coremodule.QCoreApplication(sys.argv)

    def playSound(self, audioPath):
        url = coremodule.QUrl.fromLocalFile(audioPath)
        content = multimedia.QMediaContent(url)
        player = multimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(self.app.quit)
        self.app.exec()

    def speak(self, audioString):
        tts = gTTS(text=audioString, lang='tr')
        tts.save("audio.mp3")
        self.playSound("audio.mp3")

    def recordAudio(self):
        # Record Audio
        r = sr.Recognizer()
        r.energy_threshold = 3500  
        r.dynamic_energy_threshold = True          
        with sr.Microphone() as source:
            print("Dinliyorum :)")

            audio = r.listen(source)
            audio.energy_threshold = 3500  
            audio.dynamic_energy_threshold = True          
        data = ""
        try:
            data = r.recognize_google(audio, language='tr-tr')
            data = data.lower()
            print("Bunu Söylediniz:" + data ), print(":)")
        except sr.UnknownValueError:
            print("Ne dediğini anlamadım")
        except sr.RequestError as e:
            print("Hizmet verilmemektedir {0}".format(e))

        return data
