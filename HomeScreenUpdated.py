import sys
import matplotlib.pyplot as plt
import uh_final
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QLabel, QPushButton, QLineEdit,QVBoxLayout, QComboBox

class HomeScreen(QMainWindow):
    def __init__(self):
        super(HomeScreen,self).__init__()
        loadUi("Home_Screen_QmainWindow_updated.ui",self)

        #Defining Widgets
        self.UH_label = self.findChild(QLabel, "UH_label")
        self.cloud_label_l = self.findChild(QLabel, "cloud_label_l")
        self.cloud_label_r = self.findChild(QLabel, "cloud_label_r")
        self.input_label_2 = self.findChild(QLabel, "input_label_2")
        self.drop_down_combobox = self.findChild(QComboBox, "drop_down_combobox")
        self.input_label = self.findChild(QLabel, "input_label")
        self.L_label = self.findChild(QLabel, "L_label")
        self.S_label = self.findChild(QLabel, "S_label")
        self.Lc_label = self.findChild(QLabel, "Lc_label")
        self.A_label = self.findChild(QLabel, "A_label")
        self.L_desc_label = self.findChild(QLabel, "L_label")
        self.S_desc_label = self.findChild(QLabel, "S_label")
        self.Lc_desc_label = self.findChild(QLabel, "Lc_label")
        self.A_desc_label = self.findChild(QLabel, "A_label")
        self.inputL_lineEdit = self.findChild(QLineEdit, "inputL_lineEdit")
        self.inputA_lineEdit = self.findChild(QLineEdit, "inputA_lineEdit")
        self.inputS_lineEdit = self.findChild(QLineEdit, "inputS_lineEdit")
        self.inputLc_lineEdit = self.findChild(QLineEdit, "inputLc_lineEdit")
        self.clear_button = self.findChild(QPushButton, "clear_button")
        self.done_button = self.findChild(QPushButton, "done_button")

        self.clear_button.clicked.connect(self.press_clear)
        self.done_button.clicked.connect(self.press_done)

    def press_clear(self):
        self.inputLc_lineEdit.setText("")
        self.inputL_lineEdit.setText("")       
        self.inputA_lineEdit.setText("")       
        self.inputS_lineEdit.setText("")       
    
    def press_done(self):
        widget.addWidget(GraphScreen())
        widget.setCurrentIndex(widget.currentIndex()+1)
        subzone = str(self.drop_down_combobox.currentText())
        L_float = float(self.inputL_lineEdit.displayText())   
        A_float = float(self.inputA_lineEdit.displayText())   
        S_float = float(self.inputS_lineEdit.displayText())
        if(self.inputLc_lineEdit.displayText() != ""):
            Lc_float = float(self.inputLc_lineEdit.displayText())
        else:
            Lc_float = 0
        print(subzone)   
        uh_final.calc(L_float,A_float,S_float,Lc_float,subzone)    

class GraphScreen(QDialog):
    def __init__(self):
        super(GraphScreen,self).__init__()
        loadUi("canvas.ui",self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.name_file = QLabel("Please enter the name of file:")
        self.name_file.setStyleSheet("font-family:Copperplate Gothic Bold; font-size:15px; font-weight:bold; background-color:white;")
        self.rename_lineEdit = QLineEdit()
        self.rename_lineEdit.setStyleSheet("font-family:Copperplate Gothic Bold; font-size:15px; font-weight:bold; background-color:white;")
        self.button = QPushButton('Export to Excel')
        self.button.clicked.connect(self.export_rename)
        self.button.setStyleSheet("font-family:Copperplate Gothic Bold; font-size:15px;font-weight:bold; background-color:white;")
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.name_file)
        layout.addWidget(self.rename_lineEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def export_rename(self):
        name = str(self.rename_lineEdit.displayText())
        uh_final.export_to_excel(uh_final.x10, name)
        sys.exit()
            


# main
app = QApplication(sys.argv)
home_screen = HomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(home_screen)
widget.setFixedHeight(800)
widget.setFixedWidth(1050) 
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

