import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class customwidget(Widget):
    pass
class customwidgetApp(App):
    def build(self):
        return customwidget()
h1=customwidgetApp()
h1.run()