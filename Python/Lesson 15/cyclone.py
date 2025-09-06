#we are adding in logical operators of and, or, and not. 
#This allows us to add multiple parameters in a single if statement

height = int(input('What is your height in centimeters? '))
credits = int(input('How many credits do you have? '))

#logic to determine if they can ride the ride
if height >= 137 and credits >= 10:
  print('Enjoy the ride')
elif height < 137 and credits >= 10:
  print('You aren\'t tall enough to ride')
elif height >= 137 and credits < 10:
#just learned I can use a backslash to add in apostrophes to my strings
  print('You don\'t have enough credits')
else:
  print('You haven\'t met either requirement')
