from Modules.basemodules import Backend
from Modules.mainfeatures import Features

from random import randint
from time import ctime
import pandas
import time
import os
import subprocess

#from Pyt.project import PyQt5 kodu doğru yazdın #



yapankısı = ["seni kim yarattı","tasarımcın kim"]
nasilsincumeleleri = ["nasılsın","naber","ne haber","napıyorsun","nasıl gidiyor","naber","napıyon","nasıl","nabıyon","ne yapıyorsun"]
iltifat = ["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","çok","iyi","çok iyi"]
donus = ["iyiyim sen","çok iyiyim","biraz keyifsizim"]
donustesekkur = ["Çok teşekkürler","beni utandırıyorsun","utandım","teşekkürler","yardımcı olabildiysem ne mutlu bana"]
saat = ["saat","kaç","saat kaç","kaç saat","zaman"]
gun = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın"]
maps = ["nerede","nerededir","nerda","nerde","neresi"]
playyoutube = ["çal","oynat","aç","youtube aç","youtube","muzik dinlecem","müzik dinleyeceğim"]
search = ["nedir","kimdir","ne","nasıl"]
arama = ["google","google arama yap","interneti aç"]
tempature = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
note = ["not al","not alır mısın","not"]
noteread = ["notlarımı oku","notları oku","notlar"]
playlist = ["müzik listemi çal","müzik listem","müzik","playlist","listem","müzik listeleri"]
haber = ["haberler","haberleri","haber","gündem","gazete","oku","haberleri oku"]
stopsong = ["şarkıyı kapat","şarkıyı durdur","durdur","kapat"]
kapatma = ["sistemi kapat","uyu","kendini kapat"]
openasistan = ["hey kavi","hey","alo","kavi","açıl","açıl susam açıl","açın"]
animsatici = ["anımsatıcı oluştur","anımsatıcı kur","anımsatıcı başlat","anımsatıcı oluş"]
animsaticioku = ["anımsatıcılarım","anımsatıcımı oku","anımsatıcılar","anımsatıcılarımı oku","anımsatıcı oku","anımsatıcım"]



def soner(media, utility, data):
    if data in nasilsincumeleleri:
        
        media.speak(donus[randint(0, 2)])
    if data in iltifat:
        media.speak(donustesekkur[randint(0, 4)])
    if data in saat:
        media.speak(utility.timefunc(data))
    if data in gun:
        media.speak(utility.gunfunc(data))
    if data in maps:
        utility.mapfeature(data)
    if 'youtube' in data:
        global driver
        driver = utility.playyoutube(data)
    if data in stopsong:
        subprocess.call("taskkill /IM chrome.exe")
    if data.split() in search:
        utility.searchquestion(data)
    if data in tempature:
        utility.tempature(data)
    if data in note:
        utility.createnote(data)
    if data in noteread:
        utility.readnote(data)
    if data in playlist:
        utility.emotionplaylist(data)
    if data in haber:
        utility.news(data)
    if data in yapankısı:
        utility.yapank(data)
    if data in arama:
        utility.arama2(data)





if __name__ == '__main__':
    mediamodule = Backend()
    utilitymodule = Features(mediamodule)
    
    mediamodule.speak("Merhaba, Size nasıl yardımcı olabilirim?")
    while True:
        datax = mediamodule.recordAudio()
        soner(mediamodule, utilitymodule, datax)
        time.sleep(2)
        if datax in openasistan:
                mediamodule.playSound("hello.mp3")
                time.sleep(0.5)
                datax = mediamodule.recordAudio()
                if datax in kapatma:
                    mediamodule.speak("Görüşürüz")
                    break
                else:
                    soner(mediamodule, utilitymodule, datax)
