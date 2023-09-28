import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class LoginPageApp(App):
    pass

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen,BoxLayout):
    pass


LoginPageApp().run()
