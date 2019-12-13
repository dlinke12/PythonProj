# This is a guess the number game.
import random
print('Hello! What is your name?')
name=input()
secretNumber=random.randint(1,20)
print('Well, ' + name + ', I am thinkg of a number between 1 and 20')

# Ask the playet to guess 6 times
for guessesTaken in range (1,7):
      print('Take a guess.')
      guess = int(input())
      if guess < secretNumber:
          print('Your guess is too low.')
      elif guess > secretNumber:
          print('Your guess is too high')
      else:
          break

if guess == secretNumber:
    print('You guessed the correct number which is: ' + str(secretNumber))
else:
    print('Could not guess the number, the secret number is: ' + str(secretNumber))


        
          
