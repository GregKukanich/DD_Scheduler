from ics import Calendar, Event
from Calculations import *
from datetime import datetime
from pytz import timezone
from Brothers import *
class cal:
     def createCal(self, name):
          c = Calendar()
          e = Event()
          e.name = name
          e.begin = '2020-01-30 22:30:00'
          e.end = '2020-02-21 23:59:00'
          c.events.add(e)
          c.events
          with open('DD_Calendar.ics', 'w') as my_file:
               my_file.writelines(c)

     def scheduler(self):
          c = Calendar()
          e = Event()
          for x in range(Calc.dates.__len__()):
               date = Calc.dates[x]
               time = " 21:30:00"
               date_time = str(date) + time
               datetime_obj_naive = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")     #Get date and time
               datetime_obj_eastern = timezone('US/Eastern').localize(datetime_obj_naive)      #Convert to EST
               print(datetime_obj_eastern.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
               e.begin = datetime_obj_eastern
               e.name = "Designated Drivers"
               e.duration = timedelta(hours=5)
               e.description  = " "
               test = brothers()
               for y in range(0,4):
                    e.description = e.description + str(test.getDD(Calc.dates[x]))
               c.events.add(e)
               with open('DD_Calendar.ics', 'a') as my_file:
                    my_file.writelines(c)
