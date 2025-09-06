#we have different operators to use in our if statements
# equal: ==, does not equal: !=, greater than: >, less than: <, greater or equal: >=, less or equal: <=
#we also have elif, which says else if this condition is met, do this thing

#ph asks for input and assigns to an integer
ph = int(input('What is the ph level?'))

#logic to output basic, acidic, or neutral depending on the ph integer
if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')
