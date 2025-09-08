#splitting the meal between 4 people (not dynamically)
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

#initializing total and my_share to 0
total = 0
my_share = 0

#iterating through bill list
for i in bill:
#on each iteration, add the bill index to total
  total += i
#split by 4 because there are 4 people
my_share = total / 4
#print my share of the bill
print(my_share)
