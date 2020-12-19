from datetime import date, timedelta
from Brothers import *
import random
from pytz import timezone


class Calc:
     dates = []
     usedDates = []
     def calcShifts(self, num):              #Calculates how many shifts a person should have
          if num >= 3.0 and num <= 4.0:
               return 4
          elif num < 3.0 and num >= 2.5:
               return 5
          elif num < 2.5:
               return 6
          else:
               return "ERROR"

     def calcGrade(self, stringGrade):       #Calculate number equivalent of grade level
          if stringGrade == 'Freshman':
               return 1
          elif stringGrade == 'Sophomore':
               return 2
          elif stringGrade == 'Junior':
               return 3
          elif stringGrade == 'Senior':
               return 4
          elif stringGrade == '5th Year':
               return 5
          elif stringGrade == 'Old':
               return 6

     def calcDays(self, num):                #Calculate which days of the week they should be DD
          if num >= 4 and num <= 6:
               return "Thrs"
          elif num == 3:
               return "Thrs or Fri"
          elif num == 2:
               return 'Fri or Sat'
          elif num == 1:
               return 'Fri or Sat'
          else:
               return "ERROR"

     def calcWeekendDays(self):              #Through the days in the semester all those that are not DD days are removed
          start_date = date(2021, 1, 19)
          end_date = date(2021, 4, 28)
          delta = timedelta(days=1)
          while start_date <= end_date:  # Looping through dates between start/end dates looking for Thrs,Fri,Sat within range
               if start_date.weekday() == 3:  # Thursday
                    Calc.dates.append(start_date)
               elif start_date.weekday() == 4:  # Friday
                    Calc.dates.append(start_date)
               elif start_date.weekday() == 5:  # Saturday
                    Calc.dates.append(start_date)
               start_date += delta

     def assignShifts(self, date):
          brothers1 = brothers()
          date_time_str = str(date)
          date_time_obj = datetime.strptime(date_time_str,"%Y-%m-%d")
          for x in range(len(brothers1.list1)):
               if brothers1.list1[x].days == "Thrs" and date_time_obj.weekday() == 3:
                    if int(brothers1.list1[x].ctr) > 0 and brothers1.list1[x].lastShift != x:
                         brothers1.list1[x].ctr -= 1
                         brothers1.list1[x].lastShift = x
                         return brothers1.list1[x].name
               elif brothers1.list1[x].days == "Thrs or Fri" and (date_time_obj.weekday() == 3 or date_time_obj.weekday() == 4):
                    if brothers.list1[x].ctr > 0 and brothers1.list1[x].lastShift != x:
                         brothers1.list1[x].ctr -= 1
                         brothers1.list1[x].lastShift = x
                         return brothers1.list1[x].name
                    else:
                         return
               elif brothers1.list1[x].days == "Fri or Sat" and (date_time_obj.weekday() == 4 or date_time_obj.weekday() == 5):
                    if int(brothers1.list1[x].ctr) > 0 and brothers1.list1[x].lastShift != x:
                         brothers1.list1[x].ctr -= 1
                         brothers1.list1[x].lastShift = x
                         return brothers1.list1[x].name