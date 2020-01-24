from tkinter import *
import csv
from brother import *

class gui:
    def runGUI(self):
        def show_entry_fields():                                                    #Takes input from user and adds to .csv file
            print("Name: %s\nGPA: %s\nGrade Level: %s" % (e1.get(), e2.get(), e3.get()))
            ###CREATING EXCEL FILE FOR MANUAL ENTRY###
            # data rows of csv file
            e4 = None

            # name of csv file
            filename = "Brothers.csv"

            #####Calling function to calc shifts######
            numShifts = Calc()
            e4 = numShifts.calcShifts(float(e2.get()))
            e5 = numShifts.calcDays(float(e3.get()))

            rows = [[e1.get(), e2.get(), e3.get(), e4,e5]]
            # writing to csv file
            with open(filename, 'a') as csvfile:
                # creating a csv writer object
                csvwriter = csv.writer(csvfile)
                # writing the data rows
                csvwriter.writerows(rows)


            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e1.focus_set()
        #******************************************#
        master = Tk()
        master.geometry("350x350")
        wraplength = master.winfo_width()
        master.resizable(FALSE,FALSE)

        Label(master, text="Name", justify = LEFT).grid(row=0)
        Label(master, text="GPA").grid(row=1)
        Label(master, text="Grade Level").grid(row=2)

        e1 = Entry(master)
        e1.focus_set()
        e2 = Entry(master)
        e3 = Entry(master)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        # field names
        fields = ['Name', 'GPA', 'Year', 'Num Shifts', 'Days']
        filename = "Brothers.csv"
        with open(filename, 'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

             # writing the fields
            csvwriter.writerow(fields)

        def close_window(event):
            master.destroy()
        def close_windowButton():
            master.destroy()

        def submit_window(event):
            show_entry_fields()


        quit = Button(master, text='Quit', command=close_windowButton)
        quit.grid(row=3, column=0, sticky=W, pady=4)
        master.bind('<Escape>', close_window)
        submit = Button(master, text='Submit', command=show_entry_fields)
        submit.grid(row=3, column=1, sticky=W, pady=4)
        master.bind('<Return>', submit_window)

        master.mainloop()
