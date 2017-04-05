# -*- coding: cp936 -*-

import turtle
import math 

def square(t,length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t,n,length,angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle=360.0/n
    polyline(t,n,length,angle)
    
def circle_ref(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    length=circumference/n
    polygon(t,n,length)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t,r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)
    arc(t,r,360)

def petal(t,r,angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """

    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)

def flower(t,n,r,angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t,r,angle)
        t.lt(360.0/n)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

def polypie(t, n, length):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    length: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, length, angle/2)
        t.lt(angle)

bob=turtle.Turtle()
square(bob, 40)
polygon(bob,6,40)


