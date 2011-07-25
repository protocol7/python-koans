#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

import math

def triangle(a, b, c):
  if a < 1 or b < 1 or c < 1:
    raise TriangleError, "Invalid triangle"

  k1, k2, h = sorted([a, b, c])

  if k1 + k2 <= h:
    raise TriangleError, "Invalid triangle"  
    
  # no of unique side lengths
  no_uniq = len(set([a, b, c]))

  return ["equilateral", "isosceles", "scalene"][no_uniq - 1]

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
