cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards=[]
# from art import logo
# from replit import clear
import random
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
def deal_card(setOfCards,numOfCards):
  i=1
  while i<=numOfCards:
    setOfCards.append(random.choice(cards))
    i=i+1
  return setOfCards
def calculateScore(setOfCards):
  for items in setOfCards:
    sumOfCards=sum(items)
  return(sumOfCards)
play='y'
while play=='y':
  shouldContinue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if shouldContinue=='y':
    (deal_card(user_cards,2))
    (deal_card(computer_cards,2))
    print(f"Your cards: {user_cards}, current score: {calculateScore(user_cards)}")
    print(f"Computer's first card: {computer_cards[0][0]}")