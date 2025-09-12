#combining strings and integers within a function and simple conversion of dog years to human years
def dog_years(name, age):
  human_age = age * 7
  return f'{name} is {human_age} years old in human years.'

print(dog_years('Landon', 3))
print(dog_years('Red Bean', 6))
print(dog_years('Cooper', 2))
