import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
class BoxLayoutApp(App):
    def build(self):
        return BoxLayout()
BoxLayoutApp().run()