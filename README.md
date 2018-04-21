# pyCAD

## Description

This is a simple application based on the package [dxfgrabber 1.0.0](https://github.com/mozman/dxfgrabber/blob/master/docs/index.rst). When drawing in AutoCAD, we often need to draw a lot of points with a number or name attached besides it. So pyCAD is to find the coordinates of those points and assign the nearest text to those points as their number or name. So finally, we will get the output as follow:

P01 (x01,y01,z01)

P02 (x02,y02,z02)

......

## Typical Usage
There are mainly two functions:
<pre>
search_name_for_a_unnamed_point(pointa,texts)
arguments:
pointa - a single point
texts - a list of texts
return:
a single named point (PointNamed).
</pre>
<pre>
match_point_with_name(points, texts)
arguments:
points - a list of Point
texts  - a list of texts
return:
a list of named points (PointNamed).
</pre>
