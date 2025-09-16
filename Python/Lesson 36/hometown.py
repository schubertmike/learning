#we can use init to make setting classes within objects easier

#init initializes the object, then we can place our specific values within the variable that calls the object

class City:
  def __init__(self, name, country, population, landmarks, nickname, baseball):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.baseball = baseball

seattle = City('Seattle', 'USA', 781000, ['Space Needle', 'Pike Place Market', 'Mount Rainier'], 'Emerald City', 'Mariners')

print(vars(seattle))
