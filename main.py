import warnings
warnings.filterwarnings("ignore")

from PyQt6.QtWidgets import *

import numpy as np
import pandas as pd
from matplotlib.backends.backends_qt6agg import FigureCanvasQTAgg as FigureCnavas 
from matplotlib.figure import Figure



class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.left = 50
        self.top = 50
        self.width = 1080
        self.height = 460
        self.title = "Clustering"
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.width, self.height,self.top,self.left)
        
        self.widgets()
        self.tabWidgets()
        self.show()
    
    def tabWidgets(self)  
        self.tabs = QTabWidget()
        self.setCentralWidgets(self.tabs)
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1,"Main")
        
        
    def widgets(self): 
        
        #plot 
        self.p = PlotCanvas(self,width=5,height=5)       
        # q label 
        self.k_number_text = QLabel( "choose k :")
        #spin box
        self.k_number_text = QSpinBox(self)
        self.k_number_text.setMinimum(1)
        self.k_number_text.setMinimum(9)
        self.k_number_text.setSingleStep(1)
        self.k_number_text.valueChanged.connect(self.k_numberFunction)
        
        self.radio_button = QRadioButton("save text",self)
        self.plot_save = QRadioButton("save plot",self)
        self.text_plot_save = QRadioButton("save text and plot",self)
        self.text_plot_save.setChecked(True)
        
        #button 
        self.cluster = QPushButton( "cluster", self)
        self.cluster.clicked.connect(self.clusterFunction)
        
        #list 
        self.result_list = QListWidget(self)
        
        
   def clusterFunction(self):
       pass    
                
    def k_numberFunction(self):
        pass    


        

#####plot class methods

class PlotCanvas(FigureCanvas):
    def 
    def __init__(self,parent = None, width= 5, height=5,dpi = 100):
        self.fig =  Figure(figsize=(width,height),dpi=dpi)
        
        FigureCanvas.__init__(self,self.fig)
        
    
    def plot(self,x,y,c,s, m="."):
        self.ax = self.figure.add_subplot(111)
        self.ax.scatter(x,y,c = c, s = s, marker = m)
        self.ax.set_title(  "k means ")
        self.ax.set_xlabel("Income")
        self.ax.set_ylabel("-number od transaction")
        self.draw()
        
        

    
            
    def clear(self):
        self.fig.clf()   
        
        
w = Window()                
                            