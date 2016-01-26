##Generate a deck of cards

import os
import random


def main():
    menu()
    suits = ["D", "H", "S", "C"]
    values  = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    numericValues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = GenerateCards(suits, values, numericValues)
    ShuffledDeck = ShuffleCards(deck)
    deck = ShuffledDeck
    print("\n\n")
    Player1Name = str(input("Enter Player 1 name: "))
    Player2Name = str(input("Enter Player 2 name: "))
    player1Cards, deck = GetPlayerCards(deck)
    player2Cards, deck = GetPlayerCards(deck)
    
    
##    ChoiceMade=False
##    players = 0
##    while players <= 0:
##        try:
##            players = int(input("Input number of players: "))
##        except ValueError:
##            print("That is not a valid number")
    
    
    
def menu():
    print("\t\tRandom card game")
    print("""\n\tCards Will be displayed with value first, then suit.\n\tI.E: A Jack of spades would be written as "JS"\n """)

                   
def GenerateCards(suits, values, numericValues):  ##Generates deck of cards
    deck = [] 
    for i in range(0, len(values)): ##For each value
        for j in range(0, len(suits)): ##For each suit
                       card = Card(values[i], suits[j], numericValues[i]) ##Create a card that fits both
                       deck.append(card) ##Add card to deck
    print("Deck generated")
    return deck

def ShuffleCards(deck): ##Random Shuffle
    NotShuffled = deck
    deck = []
    NoOfCards = len(NotShuffled)
    for x in range(0, NoOfCards): ##This section uses random.randrange to shuffle the cards, making the pick of top cards random
        value = random.randrange(len(NotShuffled))
        deck.append(NotShuffled[value]) ##Adds card to shuffled array
        NotShuffled.pop(value) ##Removes card from to be shuffled array
    print("Deck shuffled")
    ##print(len(deck))
    return deck
        
def GetPlayerCards(deck):
    PlayerCards = [] ##Declares empty array
    for i in range (0,3): ##For 3 cards
        PlayerCards.append(deck[i]) ##Copy card to player hand
        deck.pop(i) ##Remove card from deck
    return PlayerCards, deck
    
class Card:
    def __init__(self, value, suit, numeric):
        self.value = value
        self.suit = suit
        self.numeric = numeric
    
if __name__ == "__main__":
    main()

