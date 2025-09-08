#this will calculate the area of the following shapes:
#square, rectangle, triangle, circle
import math

shape = 0
print('===============')
print('Area Calculator')
print('===============')

print('1 - Triangle')
print('2 - Square')
print('3 - Rectangle')
print('4 - Circle')
print('5 - I\'m finished')

while shape != 5:

  shape = int(input('Which shape would you like to find the area for? Please pick a number from above '))


  if shape == 1:
    base = int(input('What is the base of the triangle? '))
    height = int(input('What is the height of the triangle? '))
    area = (base*height)/2
    print('The area of the your triangle is', area)
      
  elif shape == 2:
    side = int(input('What\'s the length of one of the sides of the square? '))
    area = side**2
    print('The area of your square is', area)
      
  elif shape == 3: 
    length = int(input('What is the length of the rectangle? (the longer side) '))
    width = int(input('What is the width of the rectangle? (the shorter side) '))
    area = length * width
    print('The area of the rectangle is ', area)
      
  elif shape == 4:
    radius = int(input('What is the radius of the circle? (take diameter, aka the measurement from end end to the opposite end, and divide by 2) '))
    area = (math.pi * radius)**2
    print('The area of the circle is ', area)

  else:
    print('That wasn\'t one of the options. Please pick 1-5')
  
print('Let me know if you need any more area calculations!')
