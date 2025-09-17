class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name, self.name,'!')

  def display_details(self):
    print('Entry Number: '+ str(self.entry))
    print('Name: ' + self.name)
    print('Type: ' + self.types)
    print('Description: ' + self.description)
    if self.is_caught == True:
      print('You already have a ' + self.name)
    else:
      print(self.is_caught)
pika = Pokemon(1,'Pikachu','Electric','It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.',True)
snor = Pokemon(2, 'Snorlax','Normal','This gluttonous Pokémon eats constantly, apart from when it’s asleep. It devours nearly 900 pounds of food per day.',False)
dig = Pokemon(3, 'Diglett','Ground','It lives about one yard underground, where it feeds on plant roots. It sometimes appears aboveground.', True)

pika.speak()
pika.display_details()
print('')
snor.speak()
snor.display_details()
print('')
dig.speak()
dig.display_details()
