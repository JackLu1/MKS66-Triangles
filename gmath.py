import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(v0, v1):
    v = [
            v0[1]*v1[2] - v0[2]*v1[1],
            v0[2]*v1[0] - v0[0]*v1[2],
            v0[0]*v1[1] - v0[1]*v1[0]
            ]
    return v

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    return None
