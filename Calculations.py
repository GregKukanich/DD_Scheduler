from datetime import date, timedelta
from Brothers import *

class Calc:
     dates = []
     usedDates = []
     def calcShifts(self, num):
          if num >= 3.0 and num <= 4.0:
               return 4

          elif num < 3.0 and num >= 2.5:
               return 5

          elif num < 2.5:
               return 6
          else:
               return "ERROR"

     def calcGrade(self, stringGrade):
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

     def calcDays(self, num):
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

     def calcWeekendDays(self):
          start_date = date(2020, 1, 13)
          end_date = date(2020, 4, 28)
          delta = timedelta(days=1)
          while start_date <= end_date:  # Looping through dates between start/end dates looking for Thrs,Fri,Sat within range
               if start_date.weekday() == 3:  # Thursday
                    Calc.dates.append(start_date)
               elif start_date.weekday() == 4:  # Friday
                    Calc.dates.append(start_date)
               elif start_date.weekday() == 5:  # Saturday
                    Calc.dates.append(start_date)
               # print(start_date.strftime("%Y-%m-%d")) Printing in formatted way
               start_date += delta
          print(Calc.dates.__len__()*4)

     # def assignShifts(self):
     #      for x in range(brothers.getTotShifts()):




