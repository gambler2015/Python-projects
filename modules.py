import math #math is an module which im using here
import calendar
cal= calendar.month(2020, 1)
print(cal)
leap=calendar.isleap(2020)
print(leap)

#importing hand-made module
import area_function  #this module must be in the same directory otherwise need to give path
a=area_function.area_of_rectangle(5 ,2)
print(a)
b=area_function.area_of_triangle(5,2)
print(b)