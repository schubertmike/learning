#this loops through and asks "are we there yet" until the answer is yes
#when the answer is yes, it prints yay and breaks so we don't infinitely print yay

answer = input('Are we there yet? ')

while answer != 'Yes' or answer != 'yes':
  if answer == 'Yes' or answer == 'yes':
    print('Yay!')
    break
  else:
    answer = input('Are we there yet? ')
