'''time for list methods. we have append, insert, remove, pop as the core 4
append adds item to the end of the list
insert adds item in the list at a specified location
pop removes an item from a specified location
remove removes an item from the list based on the value of the item
there are many more including:
clear
copy
count
extend
index
reverse
and sort'''

#now we are going to put these in action
books = ['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']

#we have finished reading 1984 and the fault in our stars so we want to remove them
books.remove('1984')
#we need to remember that we alread removed 1984, so it changed the index value of TFIOS to 1 instead of 2
books.pop(1)
print(books)
