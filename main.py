from guiTest import *
from csvExport import *

def main():
       #*****DIALOG STARTUP*****#
       import sys
       app = QtWidgets.QApplication(sys.argv)
       Dialog = QtWidgets.QDialog()
       ui = Ui_Dialog()
       ui.setupUi(Dialog)
       Dialog.show()

       csv = csvExp()
       csv.fileStart() #Start .csv file for members entered into gui dialog




       sys.exit(app.exec_())





main()
