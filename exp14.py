#To find the Euclidean distance between two points in a two dimensional spaceusing class and object
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def euclidean_distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Get user input for the coordinates of two points
x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))
point2 = Point(x2, y2)

# Calculate Euclidean distance
distance = euclidean_distance(point1, point2)

# Display the result
print(f"The Euclidean distance between the two points is: {distance}")