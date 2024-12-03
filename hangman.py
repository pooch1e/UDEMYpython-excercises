# hangman game
import random
word_list = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop','engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power',
'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism',
'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 'uni'
'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen']

guesses = []

# pick a random word
def computerChoice():
  hangman_word = random.choice(word_list)
  return hangman_word

# print current word status
def printWord(hangman_word, guesses):
  for letter in hangman_word:
    if letter in guesses:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print()
  
def humanChoice():
  guess = input("Guess a letter: ".lower)
  if guess in guesses:
    print("You guessed that")
    return humanChoice()
  guesses.append(guess)
  
def is_guess_correct(hangman_word):
  