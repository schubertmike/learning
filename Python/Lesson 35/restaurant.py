#objects are the instance of the class (which is the template for the object)
#we can check the attributes within the class for a specific object if we print vars
#but it looks like we need to create a variable to store the class

#now we are filling out our restaurant class, how do we make it dynamic though?

class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs = Restaurant()

bobs.name = 'Bob\'s Burgers'
bobs.category = 'American Diner'
bobs.rating = 4.7
bobs.delivery = False

dak = Restaurant()

dak.name = 'Zip Dak'
dak.category = 'Korean Fried Chicken'
dak.rating = 5.0
dak.delivery = True

cake_meet_me = Restaurant()

cake_meet_me.name = 'Cake Meet Me Patisserie'
cake_meet_me.category = 'Bakery'
cake_meet_me.rating = 5.0
cake_meet_me.delivery = False

print(vars(bobs))
print(vars(dak))
print(vars(cake_meet_me))
