import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import polyfit
from scipy import optimize

csv = pd.read_csv('jj.csv')
print(csv)
data = csv[['x','y']]
x =data['x']
y = data['y']


parameter = np.polyfit(x, y, 2)
print(parameter)



