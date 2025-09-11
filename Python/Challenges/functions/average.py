def average(num1, num2):
  avg = (num1 + num2)/2
  return avg

print(average(5,10))

#you can also do it like this, and remove the step of setting the local variable
def avg(num1, num2):
  return (num1 + num2)/2

print(avg(5,10))
