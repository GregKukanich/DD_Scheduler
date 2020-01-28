from Calculations import *
import csv

class csvExp:
     def fileStart(self):
          """Start csv file and add field headers for data.
          """
          # field names
          fields = ['Name', 'GPA', 'Year', 'NumShifts', 'Days']
          filename = "Brothers.csv"
          with open(filename, 'w+') as csvfile:
               # creating a csv writer object
               csvwriter = csv.writer(csvfile, lineterminator='\n')

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
          e5 = numShifts.calcDays(numShifts.calcGrade(grade))

          rows = [[e1, e2, e3, e4, e5]]
          # writing to csv file
          with open(filename, 'a') as csvfile:
               # creating a csv writer object
               csvwriter = csv.writer(csvfile, lineterminator='\n')
               # writing the data rows
               csvwriter.writerows(rows)
