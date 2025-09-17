#intro to modules, we've used them before, but we have only scratched the surface
#modules can do a whole lot of things. Python comes with over 200 built-in modules
#and... we can create our own
#we can import multiple, either using multiple lines or with one import statement and separating them by commas

import random

symbols = ['🍒','🍇','🍉','7️⃣']
results = random.choices(symbols, k=3)

def play():
    results = random.choices(symbols, k=3)
    print(results[0] + ' | ' + results[1] + ' | ' + results[2])
    if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
      print('Jackpot! 💰')
    else:
      print('Better luck next time!')

play_again = 'Y'

while play_again == "Y":
    play()
    play_again = input("Do you want to play again? (Y/N): ").upper()


