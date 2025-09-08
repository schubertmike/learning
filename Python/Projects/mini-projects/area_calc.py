#this will calculate the area of the following shapes:
#square, rectangle, triangle, circle


import math #importing math module for the math.pi constant

shape = 0 #setting shape to 0 for our loop
print('===============')
print('Area Calculator')
print('===============')

print('1 - Triangle')
print('2 - Square')
print('3 - Rectangle')
print('4 - Circle')
print('5 - I\'m finished')

while shape != 5: #loop until shape = 5

  shape = int(input('Which shape would you like to find the area for? Please pick a number from above ')) #ask the initial question, convert string to integer, and set shape to that integer

#opening logic
  if shape == 1: #if shape = 1 ask for base, ask for height, do math in area, and print the area
    base = int(input('What is the base of the triangle? '))
    height = int(input('What is the height of the triangle? '))
    area = (base*height)/2
    print('The area of the your triangle is', area)
      
  elif shape == 2: #if shape = 2, ask for side, do math in area and print area
    side = int(input('What\'s the length of one of the sides of the square? '))
    area = side**2
    print('The area of your square is', area)
      
  elif shape == 3: #if shape = 3 perform the same types of actions as above, but ask for length and width, and perform different math
    length = int(input('What is the length of the rectangle? (the longer side) '))
    width = int(input('What is the width of the rectangle? (the shorter side) '))
    area = length * width
    print('The area of the rectangle is ', area)
      
  elif shape == 4: #same as the previous, but asking for different inputs and using different math
    radius = int(input('What is the radius of the circle? (take diameter, aka the measurement from end end to the opposite end, and divide by 2) '))
    area = (math.pi * radius)**2
    print('The area of the circle is ', area)

  else: #if it's anything other than 1-5, print the following
    print('That wasn\'t one of the options. Please pick 1-5')
  
print('Let me know if you need any more area calculations!') #once they input 5, print this
