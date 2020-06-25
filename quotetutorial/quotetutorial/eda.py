import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy 
import sklearn
import seaborn as sns 

print('Numpy: {}'.format(np.__version__))
print('SKLearn: {}'.format(sklearn.__version__))

dataset = pd.read_csv(r"C:\Users\charan\Desktop\NewScraping\quotetutorial\quotetutorial\items.csv")
print(dataset.columns)
