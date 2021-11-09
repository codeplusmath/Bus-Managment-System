from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from datetime import date  # Import date class from datetime module
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.core.window import Window

from main import *

today = date.today()


class Home(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')
    
    def gostation(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'station'
        self.manager.get_screen('station')
    
    def goemployee(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'employee'
        self.manager.get_screen('employee')
        
    def goticketcounter(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ticketcounter'
        self.manager.get_screen('ticketcounter')
    
    def gobusdetails(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'busdetails'
        self.manager.get_screen('busdetails')


class Station(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')
    
    def viewstation(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewstations'
        self.manager.get_screen('viewstations')

    def addstation(self, code, name, location):
        try:
            sql = "INSERT INTO station (scode, sname, slocation) VALUES (%s, %s, %s)"
            val = (code, name, location, )
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'home'
        self.manager.get_screen('home')
        

class ViewStations(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def on_enter(self):
        data = ''
        mycursor.execute('select * from station')
        for x in mycursor:
            for i in x:
                data += str(i)
        self.ids.stations.text = data

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'station'
        self.manager.get_screen('station')
        
             
class Employee(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')
    
    def viewemployee(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewemployees'
        self.manager.get_screen('viewemployees')

    def addemployee(self, eid, employeename, stationcode, employeetype, salary, bid):
        try:
            sql = "INSERT INTO employee (eid, name , designation, bid, scode , salary) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (eid, employeename, stationcode, employeetype, salary, bid)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'home'
        self.manager.get_screen('home')
        

class ViewEmployees(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def on_enter(self):
        data = ''
        mycursor.execute('select * from employee')
        for x in mycursor:
            data += str(x)
        self.ids.viewemployees.text = data

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'employee'
        self.manager.get_screen('employee')
        

class TicketCounter(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')
    
    def viewpassanger(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewpassangers'
        self.manager.get_screen('viewpassangers')
        
    def viewhistory(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewhistory'
        self.manager.get_screen('viewhistory')
    
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'home'
        self.manager.get_screen('home')


class ViewPassangers(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def on_enter(self):
        data = ''
        mycursor.execute('select * from employee')
        for x in mycursor:
            data += str(x)
        self.ids.busdata.text = data

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ticketcounter'
        self.manager.get_screen('ticketcounter')
        

class ViewHistory(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def on_enter(self):
        data = ''
        mycursor.execute('select * from employee')
        for x in mycursor:
            data += str(x)
        self.ids.viewemployees.text = data

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ticketcounter'
        self.manager.get_screen('ticketcounter')
        

class BusDetails(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def addbus(self, busid, busname, numberplate, bustype, model, noofseats, routeid, scode,):
        try:
            sql = "INSERT INTO bus (bid, name, numplate, type, model, seats, rid, scode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (busid, busname, numberplate, bustype, model, noofseats, routeid, scode,)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def addroute(self, routeid, startstation, endstation, distance, departtime, routename):
        try:
            sql = "INSERT INTO route (rid, start_scode , dest_scode, distance, depart_time, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (routeid, startstation, endstation, distance, departtime, routename)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def viewallroute(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewallroutes'
        self.manager.get_screen('viewallroutes')
    
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'home'
        self.manager.get_screen('home')
       

class BusHaults(Screen):
    pass


class ViewAllRoutes(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def on_enter(self):
        data = ''
        mycursor.execute('select * from route')
        for x in mycursor:
            data += str(x)
        self.ids.route.text = data

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'busdetails'
        self.manager.get_screen('busdetails')
