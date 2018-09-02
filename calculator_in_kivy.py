import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
class CalcGridLayout(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except Exception:
                self.display.text="Error in calculator"
class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()
CalculatorApp().run()