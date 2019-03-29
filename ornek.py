import random
import numpy as np
import pandas as pd

def get_random_in_range(min=0.0, max=100.0, size=10):
    randoms=[]
    for count in range(0,size):
        rand = random.uniform(min,max)
        randoms.append(rand)
    return randoms

list1 = [] #list of numbers to be extracted from dataframe
list2 = [] #list of random numbers to be created

dataframe = pd.read_csv("C:\\Users\\CASPERNB\\MicrosoftEdgeBackups\\Desktop\\işletme\\4. sınıf\\python")
print(dataframe.axes)