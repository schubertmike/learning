'''list iterations: we can iterate through a list with a for-in loop, we can also use for-in with range and len'''
# 💿 Theme: Indie Travel Songs

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]
#this sets the playlist to it's index numbers, then loops through and prints each index i
for i in range(len(playlist)):
  print(playlist[i])
