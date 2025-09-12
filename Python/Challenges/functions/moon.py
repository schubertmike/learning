def moon_phase(phase):
  if phase == 'New Moon':
    return '🌑'
  elif phase == 'Waxing Crescent':
    return '🌒'
  elif phase == 'Waxing Gibbous':
    return '🌓'
  elif phase == 'Full Moon':
    return '🌕'
  elif phase == 'Waning Gibbous':
    return '🌖'
  elif phase == 'Last Quarter':
    return '🌗'
  elif phase == 'Waning Crescent':
    return '🌘'
  else:
    return 'Invalid moon phase'

answer = moon_phase('New Moon')
print(answer)

#here's how I'd really do it if I didn't have to stick to the answer parameters and I wanted to do it based on an input.
#if I wanted to make it even more complicated, I could factor in each way people would respond (caps, no caps, caps on first letter)
#I could also change the input to an integer
'''
phase = input('What moon phase are we in? ')

def moon_phase(phase):
  if phase == 'New Moon':
    return '🌑'
  elif phase == 'Waxing Crescent':
    return '🌒'
  elif phase == 'Waxing Gibbous':
    return '🌓'
  elif phase == 'Full Moon':
    return '🌕'
  elif phase == 'Waning Gibbous':
    return '🌖'
  elif phase == 'Last Quarter':
    return '🌗'
  elif phase == 'Waning Crescent':
    return '🌘'
  else:
    return 'Invalid moon phase'

print(moon_phase(phase))'''
