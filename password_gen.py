import random
letters = ["A", "B", "C", "D", "a", "b", "c", "d"]
numbers = ["0", "1", "2", "3", "4"]
symbols = ["$", "%", "^", "@", "3"]

# create random password generator

def passwordGen(rand):
  # random num generator that will become the index positions of the lists
  # check if rand is longer than list and greater than 0
  if rand <= 0:
    print("password must be more than one character")
    return
  fullPword = letters + numbers + symbols
  randPword = "".join(random.choices(fullPword, k=rand))
  
  print(f"Generated password is: {randPword}")
passwordGen(10)