import random

name = str(raw_input('Name: '))
print('Hello {}! Welcome to my Random Number Guessing Game.'.format(name))


def guessMethod():
  print('Guess a number between 1 and 100.')
  try:
    answer = random.randint(1,100)
    while True:
      guess = int(input())
      if guess > answer:
        print('Guess lower')
      elif guess < answer:
        print('Guess higher')
      elif guess == answer:
        print('You guessed it!')
        break
  except:
    print('Invalid input. Try again.')
    guessMethod()
guessMethod()
print('Press 1 to play again, or press 2 to quit!')

def playAgain():
  response = int(input())
  if response == 1:
    print('Guess a number between 1 and 100')
    guessMethod()
  elif response == 2:
    print('Goodbye {}!'.format(name))
  else:
    print('Unknown command')
    playAgain()
playAgain()
  


