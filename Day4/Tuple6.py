from collections import namedtuple
import math

#Define a named Tuple for Coordinates

point=namedtuple('point',['x','y'])

#create 2 points

point1=point(1,2)
point2=point(4,6)

#calculate Distance between 2 points

distance=math.sqrt((point2.x-point1.x)**2+(point2.y-point1.y)**2)
print("Distance between point1 and Point1:",distance)