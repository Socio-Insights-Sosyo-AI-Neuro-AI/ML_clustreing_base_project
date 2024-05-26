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
        
        
        self.show()
        
        
 
 

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
                            