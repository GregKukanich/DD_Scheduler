import csv

from Calculations import *


class csvExp:
     def fileStart(self):
          """Start csv file and add field headers for data.
          """
          # field names
          fields = ['Name', 'GPA', 'Year', 'Num Shifts', 'Days']
          filename = "Brothers.csv"
          with open(filename, 'w') as csvfile:
               # creating a csv writer object
               csvwriter = csv.writer(csvfile)

               # writing the fields
               csvwriter.writerow(fields)

     def fileFill(self, name, gpa, grade):
          filename = "Brothers.csv"
          #####Calling function to calc shifts######
          numShifts = Calc()
          e1 = name
          e2 = gpa
          e3 = grade
          e4 = numShifts.calcShifts(float(gpa))
          if grade == 'Freshman':
               e5 = numShifts.calcDays(1)
          elif grade == 'Sophomore':
               e5 = numShifts.calcDays(2)
          elif grade == 'Junior':
               e5 = numShifts.calcDays(3)
          elif grade == 'Senior':
               e5 = numShifts.calcDays(4)
          elif grade == '5th Year':
               e5 = numShifts.calcDays(5)
          elif grade == 'Old':
               e5 = numShifts.calcDays(6)

          rows = [[e1, e2, e3, e4, e5]]
          # writing to csv file
          with open(filename, 'a') as csvfile:
               # creating a csv writer object
               csvwriter = csv.writer(csvfile)
               # writing the data rows
               csvwriter.writerows(rows)
