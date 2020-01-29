from ics import Calendar, Event
from Calculations import *
import datetime

class cal:
     def createCal(self, name):
          c = Calendar()
          e = Event()
          e.name = name
          e.begin = '2020-01-27 22:30:00'
          e.end = '2020-01-28 23:59:00'
          c.events.add(e)
          c.events
          with open('DD_Calendar.ics', 'w') as my_file:
               my_file.writelines(c)

     def scheduler(self):
          c = Calendar()
          e = Event()
          begin = "21:30:00"
          for x in range(Calc.dates.__len__()):
               datetime.date = Calc.dates[x]
               datetime.datetime.combine(Calc.dates[x],) Calc.dates[x]
               print("test")
               e.begin = begin + beg
               print(e.begin)
               e.name = Calc.dates[x]
               e.duration = datetime.timedelta(hours=5)
               c.events.add(e)
               c.events
               with open('DD_Calendar.ics', 'w') as my_file:
                    my_file.writelines(c)