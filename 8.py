'''Program to find the area and circumference of a circle, when the radius is entered by the user.
However, the user can input radius in integer or float.
'''
r = eval(input('Enter the radius of circle: '))
area = 3.14*r**2
circumference = 2*3.14*r
print('area of circle is ',area,'\n circumference of circle is ',circumference)