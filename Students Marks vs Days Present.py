import csv
import numpy as np
from numpy.lib.function_base import corrcoef

def getSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
           marks_in_percentage.append(float(row["Marks In Percentage"]))
           days_present.append(float(row["Days Present"]))
        
    return {"x":marks_in_percentage,"y":days_present}

def calculateCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("THE CORRELATION OF THE DATA IS :-  \n---> ",correlation[0,1])

def setup():
  data_path = "Student Marks vs Days Present.csv"

  dataSource = getSource(data_path)
  calculateCorrelation(dataSource)

setup()
    

