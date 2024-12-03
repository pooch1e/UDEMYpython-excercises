# hangman game
import random
word_list = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop','engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power',
'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism',
'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 'uni',
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
  guess = input("Guess a letter: ").lower()
  if guess in guesses:
    print("You guessed that")
    return humanChoice()
  guesses.append(guess)
  
def is_guess_correct(hangman_word):
  if guesses[-1] in hangman_word:
    print("you win!")
  else:
    return

def playGame():
  hangman_word = computerChoice()
  attempts = 6
  
  while attempts > 0:
    # game loop
    humanChoice()
    printWord(hangman_word, guesses)
    
    if guesses[-1] in hangman_word:
      print(f"Good guess!")
    else:
      attempts -= 1  # Reduce attempts for wrong guess
      print(f"Wrong guess. You have {attempts} attempts left.")
    
  # Check if the word is completely guessed
      if all(letter in guesses for letter in hangman_word):
        is_guess_correct()
        break
      else:
        print(f"Game over! The word was: {hangman_word}")
        
playGame()