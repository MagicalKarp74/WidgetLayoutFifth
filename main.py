import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout

class LayoutAssignment(BoxLayout):
    pass

class GridLayoutExample(GridLayout):
    pass
class StackLayoutExample(StackLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for letter in "abcdefghijklmnopqrstuvwxyz1234567890":
            b = Button(text = "Button "+letter, size_hint=(.5,.5))
            self.add_widget(b)
class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

WidgetLayoutApp().run()
