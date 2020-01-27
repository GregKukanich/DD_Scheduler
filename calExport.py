from ics import Calendar, Event
import datetime
from Brothers import *

class cal:
     def createCal(self,name):
          c = Calendar()
          e = Event()
          e.name = name
          e.begin = '2020-01-27 22:30:00'
          e.end = '2020-01-28 23:59:00'
          c.events.add(e)
          c.events
          with open('DD_Calendar.ics', 'w') as my_file:
               my_file.writelines(c)

     #def addCal(self):
          #


