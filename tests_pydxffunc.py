
'''This module is to test pydxffunc.py module. It's my practice for 
test-driven development.
'''
import unittest

from dxfgrabber import readfile
from dxfgrabber import dxfentities
from pydxffunc import latdis, verdis, absdis
from pydxffunc import find_lateral_nearest_point
from pydxffunc import find_index_of_smallest_number
from pydxffunc import search_name_for_a_unnamed_point
from pydxffunc import match_point_with_name
import math



# Construct several Point instance for test purpose
P000 = dxfentities.Point()
P010 = dxfentities.Point()
P100 = dxfentities.Point()
P110 = dxfentities.Point()
P111 = dxfentities.Point()
P222 = dxfentities.Point()
P333 = dxfentities.Point()
P000.point = (0,0,0)
P010.point = (0,1,0)
P100.point = (1,0,0)
P110.point = (1,1,0)
P111.point = (1,1,1)
P222.point = (2,2,2)
P333.point = (3,3,3)
POINTS1 = [P000,P100,P110,P111,P222]
POINTS2 = [P010,P110,P222,P333]
POINTS3 = [P000,P100,P110,P111,P222]

# Construct several Text instance for test purpose
T000 = dxfentities.Text()
T010 = dxfentities.Text()
T100 = dxfentities.Text()
T000.insert = (0.1,0.1)
T000.text = "P000"
T010.insert = (0,1.1)
T010.text = "P010"
T100.insert = (1.1,0)
T100.text = "P100"
TEXTLIST = (T000,T010,T100)

class DistanceFunctionTests(unittest.TestCase):

    def test_latdis(self):
         self.assertEqual(latdis(P000,P010),1)
         self.assertEqual(latdis(P000,P100),1)
         self.assertEqual(latdis(P000,P110),math.sqrt(2))
         self.assertEqual(latdis(P000,P111),math.sqrt(2))
         self.assertEqual(latdis(P010,P100),math.sqrt(2))
         self.assertEqual(latdis(P010,P111),1)
         self.assertEqual(latdis(P110,P111),0)
    
    def test_verdis(self):
        self.assertEqual(verdis(P000,P000),0)
        self.assertEqual(verdis(P000,P010),0)
        self.assertEqual(verdis(P000,P111),-1)
        self.assertEqual(verdis(P111,P000),1)
    
    def test_absdis(self):
        self.assertEqual(absdis(P000,P000),0)
        self.assertEqual(absdis(P111,P111),0)
        self.assertEqual(absdis(P000,P010),1)
        self.assertEqual(absdis(P000,P100),1)
        self.assertEqual(absdis(P000,P110),math.sqrt(2))
        self.assertEqual(absdis(P000,P111),math.sqrt(3))
        self.assertEqual(absdis(P010,P111),math.sqrt(2))
        self.assertEqual(absdis(P110,P111),1)


class SearchNearestPointTests(unittest.TestCase):

    def test_find_lateral_nearest_point(self):
        self.assertEqual(find_lateral_nearest_point(P000,POINTS1),(P000,0))
        self.assertEqual(find_lateral_nearest_point(P000,POINTS2),(P010,0))
        self.assertEqual(find_lateral_nearest_point(P333,POINTS3),(P222,4))

    def test_search_name_for_a_unnamed_point(self):
        self.assertEqual(search_name_for_a_unnamed_point(P000,TEXTLIST).name,"P000")
        self.assertEqual(search_name_for_a_unnamed_point(P010,TEXTLIST).name,"P010")
        self.assertEqual(search_name_for_a_unnamed_point(P100,TEXTLIST).name,"P100")

# Loading Points from dxf4tests\dxf4test1.dxf
dxf = readfile('dxf4tests\dxf4test1.dxf')
POINTS_FROM_DXF4TEST1 = [entity for entity in dxf.entities if entity.dxftype == "POINT"]
TEXTS_FROM_DXF4TEST1 = [entity for entity in dxf.entities if entity.dxftype == "TEXT"]

class MatchFunctionTests(unittest.TestCase):

    def test_match_point_with_name(self):
        points = match_point_with_name(POINTS_FROM_DXF4TEST1,TEXTS_FROM_DXF4TEST1)
        for point in points:
            if point.point == (40.0, 30.0,0.0):
                self.assertEqual(point.name=="P01")
            elif point.point == (72.0,50.0,0.0):
                self.assertEqual(point.name, "P02")
            elif point.point == (52.0, 40.0, 0.0):
                self.assertEqual(point.name, "P03")
            elif point.point == (67.0, 38.0,0.0):
                self.assertEqual(point.name, "P04")
            elif point.point == (67.0, 30.0,0.0):
                self.assertEqual(point.name,"P05")
            elif point.point == (40.0,40.0,0.0):
                self.assertEqual(point.name, "P06")
            elif point.point == (40.0,50.0,0.0):
                self.assertEqual(point.name,"P07")
            elif point.point == (64.0,24.0,0.0):
                self.assertEqual(point.name,"P08")
            else:
                self.assertEqual(point.name,"P09")

if __name__ == "__main__":
    unittest.main()