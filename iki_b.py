coordinates = [ (1,1), (1,5), (2,6), (4,6), (5,3)  ]
sum = 0
print (coordinates[0])
print (coordinates[1])
#index from 0 to 4(inclusive)
#index from 0 and always less than 5 (length of list)
# idea: distance between coordinates [index] and cooridnates [index +1]
# coordinates[0] and coordinates[1]
index = 0
length = len(coordinates)
while index < length - 1:
    # do the math
    start =  coordinates [index]
    end = coordinates [index + 1] # careful with the indexes at the end
    
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    distance = abs(x2 - x1) + abs(y2 - y1)
    print("distance between", start, " and ", end, "is", distance)
    sum = sum + distance
    #move on to the next index
    index = index + 1
#out of indentation = out of while
print("forward distance is,", sum)
#calculate return trip individually and add

end = coordinates[0]
# start = coordinates[-1] #last
start = coordinates[length - 1] #last

x1 = start[0]
x2 = end[0]
y1 = start[1]
y2 = end[1]
distance = abs(x2 - x1) + abs(y2 - y1)
sum = sum + distance
print("Total distance is,", sum)
