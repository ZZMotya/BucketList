from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.clock import Clock
Window.size = (300, 600)

class Test(MDScreenManager):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
    def add_card(self):
        card = Card()
        card = card.create_card(self)
        self.ids['cards'].add_widget(card)
        self.manager.current = 'Home'

class AddScreen(Screen):
    def __init__(self, **kwargs):
        super(AddScreen, self).__init__(**kwargs)

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
    def about_us(self):
        self.ids['us'].text = 'Мы :)'

class Card(MDCard):
    def create_card(self, screen):
        card = MDCard(orientation='vertical', size = (158,158),size_hint = (None,None),elevation = 0,
                      padding='15dp',spacing='15dp',radius='10dp', ripple_behavior=True, style='filled')
        card.add_widget(MDLabel(text = screen.manager.get_screen('Add').ids['title'].text))
        return card

class MyApp(MDApp):
    def build(self):
        return Test()

if __name__ == '__main__':
    MyApp().run()