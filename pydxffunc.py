
'''This module adds some additional functions to manipulate data from
dxfgrabber.
'''

__version__ = '1.0.0'
__author__ = 'Tian'

import math
from dxfgrabber import dxfentities

# this variable is for test.
# p000 = dxfentities.Point()
# p010 = dxfentities.Point()
# p100 = dxfentities.Point()
# p110 = dxfentities.Point()
# p111 = dxfentities.Point()
# p000.point = (0,0,0)
# p010.point = (0,1,0)
# p100.point = (1,0,0)
# p110.point = (1,1,0)
# p111.point = (1,1,1)

# t000 = dxfentities.Text()
# t010 = dxfentities.Text()
# t100 = dxfentities.Text()
# t000.insert = (0.1,0.1)
# t000.text = "P000"
# t010.insert = (0,1.1)
# t010.text = "P010"
# t100.insert = (1.1,0)
# t100.text = "P100"
# textlist = (t000,t010,t100)

class PointNamed(dxfentities.Point):
    '''A point with name, inherited from dxfgrabber.dxfentities.Point.
    '''

    def __init__(self):
        super(PointNamed,self).__init__()
        self.name = ""

# q000 = PointNamed()
# q000.point = (0,0,0)
# q000.name = "Q000"

# q111 = PointNamed()
# q111.point = (1,1,1)
# q111.name = "Q111"

def latdis(pointa, pointb):
    '''Calculate the lateral distance between two points.
    the argument shall be dxfgrabber.dxfentities.Point object.
    '''

    xa = pointa.point[0]
    ya = pointa.point[1]
    xb = pointb.point[0]
    yb = pointb.point[1]

    return math.sqrt(math.pow((xa-xb),2)+math.pow((ya-yb),2))

def verdis(pointa, pointb):
    '''Calculate the vertical distance (elevation) between two
    points. the argument shall be dxfgrabber.dxfentities.Point 
    object. If the return value is minus, it means point b is
    higher than point a. Vice verse.
    '''

    return pointa.point[2] - pointb.point[2]

def absdis(pointa, pointb):
    '''Calculate the absolute distance between two points. the 
    argument shall be dxfgrabber.dxfentities.Point object.
    '''

    xa = pointa.point[0]
    ya = pointa.point[1]
    za = pointa.point[2]
    xb = pointb.point[0]
    yb = pointb.point[1]
    zb = pointb.point[2]

    return math.sqrt(math.pow((xa-xb),2)+math.pow((ya-yb),2)+math.pow((za-zb),2))

def find_lateral_nearest_point(pointa,points):
    '''Find the laterally nearest point in a set of points to a specific
    point.
    '''

    all_dis = [latdis(pointa, pointb) for pointb in points]
    index = find_index_of_smallest_number(all_dis)

    return (points[index],index)

def find_index_of_smallest_number(lst):
    '''Find index of the smallest number in a list
    '''

    return lst.index(min(lst))

def search_name_for_a_unnamed_point(pointa,texts):
    '''Find the nearest dxfgrabber.dxfentities.Text object to a certain 
    point, and assign the text of Text as the name of the point.
    '''

    pointan = PointNamed()
    pointan.point = pointa.point
    pointan.name = ""

    points = []

    for text in texts:
        p = PointNamed()
        p.name=text.text
        x, y, z= text.insert
        p.point = (x,y,z)
        points.append(p)
    
    index = find_lateral_nearest_point(pointa, points)[1]
    pointan.name = points[index].name
    
    return pointan

def match_point_with_name(points,texts):
    '''Match the point with the correct name!
    '''

    results = []
    
    for point in points:
        result = search_name_for_a_unnamed_point(point,texts)
        results.append(result)
    
    return results