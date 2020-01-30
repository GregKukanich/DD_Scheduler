from Calculations import *
import csv
from datetime import date, timedelta, datetime

class brothers:
     list1 = []

     def __init__(self):
          self.name = None
          self.gpa = None
          self.year = None
          self.shifts = None
          self.days = None
          self.time = None
          self.date = None
          self.ctr = 0

     def intake(self):
          with open('Brothers.csv') as file:
               reader = csv.reader(file, delimiter=',', quotechar='|')
               file.readline()
               for row in reader:
                    brothers1 = brothers()
                    brothers1.name = row[0]
                    brothers1.gpa = row[1]
                    brothers1.year = row[2]
                    brothers1.shifts = row[3]
                    brothers1.days = row[4]
                    brothers1.ctr = int(brothers1.shifts)
                    brothers.list1.append(brothers1)

               for x in range(len(brothers.list1)):
                    print(brothers.list1[x].name, brothers.list1[x].gpa, brothers.list1[x].year,
                          brothers.list1[x].shifts, brothers.list1[x].days)

     def getTotShifts():
          x=0
          while x != 1:
               ctr =0
               for i in range(len(brothers.list1)):
                    ctr += int(brothers.list1[i].shifts)
               x = x+1
          return ctr

     def display(self):
          for i in self.list1:
               print(i)

     def getDD(self, str_date):
          date_time_str = str(str_date)
          date_time_obj = datetime.strptime(date_time_str,"%Y-%m-%d")
          for z in range(len(brothers.list1)):
               if (brothers.list1[z].days == "Thrs" and date_time_obj.weekday() == 3):
                    if (int(brothers.list1[z].ctr) > 0):
                         brothers.list1[z].ctr -= 1
                         return brothers.list1[z].name
               elif (brothers.list1[z].days == "Thrs or Fri" and date_time_obj.weekday() == 4):
                    if (int(brothers.list1[z].ctr) > 0):
                         brothers.list1[z].ctr -= 1
                         return brothers.list1[z].name
               elif (brothers.list1[z].days == 'Fri or Sat' and date_time_obj.weekday() == 5):
                    if (int(brothers.list1[z].ctr) > 0):
                         brothers.list1[z].ctr -= 1
                         return brothers.list1[z].name