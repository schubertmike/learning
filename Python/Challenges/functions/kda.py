#calculating Kill, Death, Assist ratio
#k = how many players you defeated
#d = how many times you were defeated
#a = how many assists you had
def kda(k,d,a):
  #math to calculate kda
  return (k+a)/d

#print the function and assign the numbers to the params
print(kda(4,8,2))
