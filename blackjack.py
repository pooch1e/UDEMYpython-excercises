# blackjack project
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

player = []
dealer = []


def firstDeal():
  randCard = random.sample(cards, 4)
  
  player.append(randCard[0])
  player.append(randCard[1])
  total = sum(player)
  print(f"your hand is {player}, totalling {total}")
  dealer.append(randCard[2])
  dealer.append(randCard[3])
  dtotal = sum(dealer)
  print(f"the dealer drew: {dealer}, totalling {dtotal}")


def deal1Card():
  newCard = random.choice(cards)
  player.append(newCard)
  

firstDeal()

def round1():
  print("would you like to hit or stay? ")
  action = input(" ")
  if action == "hit":
    deal1Card()
    total = sum(player)
    dtotal = sum(dealer)
    print(f"your hand is {player}, totalling {total}")
    print(f"the dealer is: {dealer}, totalling {dtotal}")
  elif action == "stay":
    return

round1()
  

