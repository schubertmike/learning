#fizz buzz problem
#needed to loop through the range from 1 to 100, iterating by 1
#needed to check for multiples of 3, or 5, and, 3 and 5
#needed to check for multiples of 3 and 5 first, otherwise they would have received the other prints
for i in range(1,100,1):
  #check for multiples of 3 and 5 by checking that the remainder of i/3 and i/5 is 0
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
    #check for multiples of 3
  elif i % 3 == 0:
    print('Fizz')
    #check for multiples of 5
  elif i % 5 == 0:
    print('Buzz')
    #if not a multiple of 3 or 5, print the number i
  else:
    print(i)
