#calculating other worldly weight from earth weight

print('Let\'s convert your earth weight to other worlds!')
print('1 - Mercury')
print('2 - Venus')
print('3 - Mars')
print('4 - Jupiter')
print('5 - Saturn')
print('6 - Uranus')
print('7 - Neptune')
print('RIP planet Pluto :(')
earth_weight = float(input('What\'s your weight on earth (in lbs)? '))

planet = int(input('What planet are you on? (please use the planet number from above) '))

if planet == 1:
  destination_weight = earth_weight * 0.38
  print('Your weight is:', destination_weight,'lbs')
elif planet == 2:
  destination_weight = earth_weight * 0.91
  print('Your weight is:', destination_weight,'lbs')
elif planet == 3:
  destination_weight = earth_weight * 0.38
  print('Your weight is:', destination_weight,'lbs')
elif planet == 4:
  destination_weight = earth_weight * 2.53
  print('Your weight is:', destination_weight,'lbs')
elif planet == 5:
  destination_weight = earth_weight * 1.07
  print('Your weight is:', destination_weight,'lbs')
elif planet == 6:
  destination_weight = earth_weight * 0.89
  print('Your weight is:', destination_weight,'lbs')
elif planet == 7:
  destination_weight = earth_weight * 1.14
  print('Your weight is:', destination_weight,'lbs')
else: 
  print('invalid planet number')
