from main import Telegram_Start
from qt_design import * 
import sys

def Start_Clicked():
    whatsDirect.destroy()
    Telegram_Start(ui.ExcelSheetName.text())

def Cancel_clicked():
    sys.exit(app.exec_())


 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    whatsDirect = QtWidgets.QDialog()
    ui = Ui_whatsDirect()
    ui.setupUi(whatsDirect)
    ui.StartButton.clicked.connect(Start_Clicked)
    ui.CancelButton.clicked.connect(Cancel_clicked)

    whatsDirect.show()

    sys.exit(app.exec_())
