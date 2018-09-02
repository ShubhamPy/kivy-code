import kivy
from kivy.app import App
from kivy.uix.button import Label

class kivy_proApp(App):
    def build(self):
        return Label()
kivy_proApp().run()