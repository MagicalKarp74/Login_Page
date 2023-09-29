import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("QuizPage.kv")

class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class Question1Screen(Screen,BoxLayout):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "wrong"
    def move_screen(self):
        self.manager.current = "question2"

class Question2Screen(Screen,BoxLayout):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "wrong"


class WrongScreen(Screen,BoxLayout):
    def move_screen(self):
        self.manager.current = "question2"

class CorrectScreen(Screen,BoxLayout):
    def move_screen(self):
        self.manager.current = "question2"


QuizPageApp().run()
