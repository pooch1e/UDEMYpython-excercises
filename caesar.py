# caesar cypher in python
import string

alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
# creates dict where a = 1, b = 2 etc


# print(alphabet)

def caesarCypher(userInput, shiftNum):
  converted_number =[]
  # convert string to number 
  for letter in userInput:
    if letter in alphabet:
      shifted_index = (alphabet[letter] + shiftNum - 1) % 26 + 1
      # shift by num input
      converted_number.append(shifted_index)
  
  # convert back
   # Convert back to letters
    reverse_alphabet = {index: letter for letter, index in alphabet.items()}
    shifted_letters = [reverse_alphabet[num] for num in converted_number]
  return "".join(shifted_letters)
      
print(caesarCypher("hello", 1))

