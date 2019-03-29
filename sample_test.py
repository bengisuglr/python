import numpy as np
import pandas as pd

def process_data(filename):
    df = pd.read_csv("sciphol.txt", delim_whitespace=True)
    temparray = np.asarray(df["Temperature"])
    return temparray

def Calculate_points(temp):
    hotpoints = 0
    coldpoints = 0
    if temp < 8.0:
        cold = 8.0 - temp
        coldpoints = coldpoints + cold
    elif temp > 16.0:
        hot = temp - 16.0
        hotpoints = hotpoints + hot
            
    return hotpoints, coldpoints

def Calculate_average(tarray, nyears):
    totalcoldpoints= 0
    totalhotpoints= 0
    for temp in tarray:
        hot, cold = Calculate_points(temp)
        totalcoldpoints= totalcoldpoints + cold
        totalhotpoints= totalhotpoints + hot
    avghot = totalhotpoints / nyears
    avgcold = totalcoldpoints / nyears
    return avghot, avgcold

tarray = process_data("sciphol.txt")
avghot, avgcold = Calculate_average(tarray, 68)
print("average for 68 years hotpoints:", avghot, "coldpoints:", avgcold)
    