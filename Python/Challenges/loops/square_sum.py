
#summing squares
#input a number and convert string to integer
number = int(input('Can I have an integer please? '))
#set total variable to 0
total = 0
#loop i from 1 to the number + 1 in order to iterate the proper amount of times. For example, if I just did number and it was 5, then it would only iterate 4 times.
for i in range(1, (number+1)):
  #sets total to i squared and adds each iteration square together
  total += i ** 2

#prints the output
print(total)  
