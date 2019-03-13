x = 1
y = 3
point = (x,y)
print ("my first point is;", point)
print ("0th in the tuple is:", point[0])
print ("1st item in the tuple is:", point[1])
id = ("Bengisu", "Güler", 2076347, "bengisu.guler@metu.edu.tr")
coordinates =( (0,0) , (1,1) )
pointDimension = len(point)
print("our point is", pointDimension, "dimensioned.")

point2 = [x,y]
print( "second point as a list is:", point2)
converted = list (point)
print("converted from tuple to list:", converted)

emptyList = []
emptyList.append(point)
emptyList.append( (2,5) )
emptyList.append( (6,9) )
emptyList.extend( [ (5,9),(9,5) ] )
copy = emptyList.copy()
print("Empty list is not so empty now: ", emptyList)
print("The copy is: ", copy)