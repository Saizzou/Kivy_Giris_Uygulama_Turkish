import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import  ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.graphics import *
from kivy.core.image import Image
from kivy.core.window import Window

from veritabani import VeriTabani

class GirisPenceresi(Screen):
    
    def girisBtn(self):
        if vt.onaylama(self.email.text, self.sifre.text):
            OturumPenceresi.current = self.email.text
            self.sifirla()
            sm.current="oturum"

        else:
            hataliForm()
            self.sifre.text=""
    
    def kayitBtn(self):
        sm.current="kayit"
    
    def cikisBtn(self):
        App.get_running_app().stop()

    def sifirla(self):
        self.email.text=""
        self.sifre.text=""

    
class KayitPenceresi(Screen):

    isimk = ObjectProperty(None)
    emailk = ObjectProperty(None)
    sifrek = ObjectProperty(None)

    def onayBtn(self):
        if self.isimk.text != "" and self.emailk.text != "" and self.emailk.text.count(
                "@") == 1 and self.emailk.text.count(".") > 0:
            if self.sifrek != "":
                vt.add_kullanici(self.emailk.text, self.sifrek.text, self.isimk.text)

                self.sifirla()

                sm.current = "giris"
            else:
                hataliForm()
        else:
            hataliForm()
    
    def geriBtn(self):
        sm.current="giris"

    def sifirla(self):
        self.emailk.text=""
        self.isimk.text=""
        self.sifrek.text=""


class OturumPenceresi(Screen):

    isimo = ObjectProperty(None)
    tariho = ObjectProperty(None)
    emailo = ObjectProperty(None)
    basliko = ObjectProperty(None)
    current = ""

    def geriBtn(self):
        sm.current="giris"

    def on_enter(self, *args):
        if self.current.count("@") == 1:
            sifre, isim, tarih = vt.get_kullanici(self.current)
            self.isimo.text = "Kullanici: " + isim
            self.emailo.text = "Email: " + self.current
            self.tariho.text = "Katilim: " + tarih
            self.basliko.text = "Mail ile Giris"
        else:
            #self.kullanicilar[isim] = (sifre, email, tarih)
            sifre, email, tarih = vt.get_kullanici2(self.current)
            self.isimo.text = "Kullanici: " + self.current
            self.emailo.text = "Email: " + email
            self.tariho.text = "Katilim: " + tarih
            self.basliko.text = "Kullanici ile Giris"


    def cikisBtn(self):
        App.get_running_app().stop()

class WindowManager(ScreenManager):
    pass

def hataliForm():
    pop = Popup(title="Hatali Form",
                content=Label(text="Lütfen tüm bilgileri dogru girdiginizden emin olun!"),
                size_hint=(None,None), size=(400, 400))
    pop.open()


kv = Builder.load_file("tasari.kv")

sm=WindowManager()
vt = VeriTabani("kullanicilar.txt")
screens = [GirisPenceresi(name="giris"), KayitPenceresi(name="kayit"), OturumPenceresi(name="oturum")]
for screen in screens:
    sm.add_widget(screen)


class Uygulamam(App):
    def build(self):
        return sm

if __name__=="__main__":
    Uygulamam().run()