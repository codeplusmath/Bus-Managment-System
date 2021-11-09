from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
# from kivymd.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivymd.toast import toast
import requests
from connected import *
import os


LabelBase.register(name='DelaGothic', fn_regular='.\Assest\DelaGothicOne-Regular.ttf')
LabelBase.register(name='Mukta-Medium', fn_regular='.\Assest\Mukta-Medium.ttf')
LabelBase.register(name='Mukta-SemiBold', fn_regular='.\Assest\Mukta-SemiBold.ttf')
LabelBase.register(name='VarelaRound', fn_regular='.\Assest\VarelaRound-Regular.ttf')
Window.clearcolor = (1,1,1,1)


class Login(Screen):
    Window.size = (400, 300)
    def do_login(self, loginText, passwordText):
        app = MDApp.get_running_app()
        
        app.username = loginText
        app.password = passwordText
        if app.username == 'usr':
            if app.password == 'pass':
                self.ids.loginerror.text = ""
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'home'
                Window.size = (800, 600)
                
        else:
            self.ids.loginerror.text = "incorrect username or password"
                

    def resetForm(self):
        self.ids['password'].text = ""


class BusManagment(MDApp):
    username = StringProperty(None)
    password = StringProperty(None)
    dialog = None

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        self.theme_cls.primary_palette = 'Indigo'
        
        
        manager.add_widget(Home(name='home'))
        manager.add_widget(Station(name='station'))
        manager.add_widget(Employee(name='employee'))
        manager.add_widget(TicketCounter(name='ticketcounter'))
        manager.add_widget(BusDetails(name='busdetails'))
        manager.add_widget(ViewStations(name='viewstations'))
        manager.add_widget(ViewEmployees(name='viewemployees'))
        manager.add_widget(ViewHistory(name='viewhistory'))
        manager.add_widget(ViewPassangers(name='viewpassangers'))
        manager.add_widget(ViewAllRoutes(name='viewallroutes'))
        
        
        return manager

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    BusManagment().run()
