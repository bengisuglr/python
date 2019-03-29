#coordinates = [(1,1), (1,5), (2,6), (4,6), (5,3) ]
#
##index = 0
##
##while index < len(coordinates):
##    print('x'+str(index+1), coordinates[index][0])
##    print('y'+str(index+1), coordinates[index][1])
##    index += 1
##    
##    if index == 3:
##        break
##    
##print('after break ', index)
#
#
#for coor in coordinates[0:4]:
#    print(coor)
#
#
#coordinates = [(1,1), (1,5), (2,6), (4,6), (5,3) ]
#sum = 0
#print (coordinates[0])
#print (coordinates[1])
## index from 0 to 4 (inclusive)
## index from 0 and always less than 5 (length of list)
## idea: distance between coordinates[index] and coordinates[index + 1]
## coordinates[0] and coordinates[1]
#
#squared_coordinates=[]
#for point in coordinates:
#    square_value = (point[0]**2, point[1]**2)
#    squared_coordinates.append(square_value)
#print(squared_coordinates)


#def my_function(end):
#    for i in range(0, end):
#        print('In function for ' + str(i) + 'time')
#
#def average(list):
#    return sum(list) / len(list)
#    
#phlevels = [7.1, 7.5, 7.3, 6.9, 7.2, 7.4, 7.2, 7.4, 6.9, 6.8, 5.0, 5.1, 5.9]
#mid = int(len(phlevels)/2)
#olddata= phlevels[:mid]
#print(olddata)
#avgolddata= average(olddata)
#latestdata= phlevels[mid:]
#print(latestdata)
#avglatestdata= average(latestdata)
#deviation= abs(avglatestdata - avgolddata)
#devpercent= deviation / avgolddata
#
#if devpercent > 0.10:
#    print("alarm!")
#else:
#    print("ok!")

import pandas as pd
import numpy as np
df = pd.read_csv("dataset.txt") # reads into a dataframe

#print(df)
#print(df.axes)
#print(df.index)
#print(df.columns)

print ("The name column.")
print(df["Name"])
print("Has size:", df.Name.size, " , has objects of type", df.Name.dtype )
print("Unique names:", df.Name.unique())

print("The coffee consumption")
print("Average:", df.Coffee.mean())

print("The first two lines have data:")
print(df.Coffee.head(2))
print(df.Coffee.tail(2))

coffeearray = np.asarray(df.Coffee)
print(coffeearray)
       
print( df.groupby("Name")["Coffee"].mean() )
    
    