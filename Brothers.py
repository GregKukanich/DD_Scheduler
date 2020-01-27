from Calculations import *
import csv

class brothers:
     def __init__(self):
          self.list1 = []
     def intake(self):
          with open('Brothers.csv',newline='') as file:
               reader = csv.reader(file, delimiter=' ',quotechar='|')
               for row in reader:
                    print(row)
                    # self.name = row['Name']
                    # self.gpa = row['GPA']
                    # self.year = row['Year']
                    # self.shifts = row['Shifts']
                    # self.shifts = row['Days']

          # #
          # num = brothers()
          # shiftsCalc = Calc()
          # num.name = name
          # num.gpa = gpa
          # num.year = grade
          # num.shifts = shiftsCalc.calcShifts(float(gpa))
          # num.days =  shiftsCalc.calcDays(grade)
          # self.list1.append(num)

     def display(self):
          for i in self.list1:
               print(i)