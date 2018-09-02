import kivy
from kivy.uix.stacklayout import StackLayout
from kivy.app import App
class StackLayoutApp(App):
    def build(self):
        return StackLayout()
StackLayoutApp().run()