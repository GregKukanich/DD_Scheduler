from Calculations import *
import csv

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
          self.ctr = None

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
                    brothers1.ctr = brothers1.shifts
                    brothers.list1.append(brothers1)

               for x in range(len(brothers.list1)):
                    print(brothers.list1[x].name, brothers.list1[x].gpa, brothers.list1[x].year,
                          brothers.list1[x].shifts, brothers.list1[x].days)

          # #
          # num = brothers()
          # shiftsCalc = Calc()
          # num.name = name
          # num.gpa = gpa
          # num.year = grade
          # num.shifts = shiftsCalc.calcShifts(float(gpa))
          # num.days =  shiftsCalc.calcDays(grade)
          # self.list1.append(num)

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
