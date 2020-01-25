from guiTest import *


def main():
     import sys
     app = QtWidgets.QApplication(sys.argv)
     Dialog = QtWidgets.QDialog()
     ui = Ui_Dialog()
     ui.setupUi(Dialog)
     Dialog.show()
     sys.exit(app.exec_())


main()
