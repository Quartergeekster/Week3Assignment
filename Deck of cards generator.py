##Card game program
##Written By R Roe: 150409241
##For SEF034: Assignment 1

import os
import random
import sys


def main():
    menu()
    Continue = PlayOrQuit()
    while(Continue):
        deck = GenerateAndShuffle();
        print("\n\n")
        Player1Name = str(input("Enter Player 1 name: "))
        Player2Name = str(input("Enter Player 2 name: "))
        player1Cards, deck = GetPlayerCards(deck)
        for(i in len(player1Cards)):
            print(player1Cards[i].value + player1Cards.suit)
        player2Cards, deck = GetPlayerCards(deck)
        Player1Highest = FindHighestCardInHand(player1Cards)
        Player2Highest = FindHighestCardInHand(player2Cards)
        print(Player1Name +"'s Highest card: " + Player1Highest.value + Player1Highest.suit)
        print(Player2Name +"'s Highest card: " + Player2Highest.value + Player2Highest.suit)
        Draw = CheckForDraw(Player1Highest, Player2Highest)
        if(not Draw):
            Player1Win = CompareHighestCards(Player1Highest,Player2Highest)
            if(Player1Win):
                print(Player1Name + " WINS!")
            else:
                print(Player2Name + " WINS!")
        else:
            print("It's a draw!")
        Continue = PlayOrQuit()
    sys.exit()
    
def menu(): ##Initial Menu for player
    print("\t\tRandom card game")
    print("""\n\tCards Will be displayed with value first, then suit.\n\tI.E: A Jack of spades would be written as "JS"\n\tAces are low\n""") 

def PlayOrQuit(): ##Determines whether player wants to keep playing
    print("""\n\tSelect an option\n\n1. Play Game\n2.Quit""")
    choice = int(input("\nOption: "))
    ValidChoice = False
    while(not ValidChoice):
        if(choice==1):
            ValidChoice = True
            return True
        elif(choice == 2):
            ValidChoice = True
            return False
        else:
            print("Choice not valid")



def GenerateAndShuffle(): ##Generates and Shuffles deck
    suits = ["D", "H", "S", "C"]
    values  = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    numericValues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = GenerateCards(suits, values, numericValues)
    ShuffledDeck = ShuffleCards(deck)
    deck = ShuffledDeck
    return deck
                       
def GenerateCards(suits, values, numericValues): ##Generates cards for deck and adds to list
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
    return deck
        
##This method prevents duplicates of cards occurring
def GetPlayerCards(deck):
    PlayerCards = [] ##Declares empty array
    for i in range (0,3): ##For 3 cards
        PlayerCards.append(deck[i]) ##Copy card to player hand
        deck.pop(i) ##Remove card from deck
    return PlayerCards, deck

def FindHighestCardInHand(PlayerCards): ##Finds Highest card in player's hand
    HighestCard = PlayerCards[0]
    for i in range(1,2):
        if PlayerCards[i].numeric > HighestCard.numeric:
            HighestCard = PlayerCards[i]
        else:
            pass
    return HighestCard

def CheckForDraw(Player1, Player2): ##Returns Boolean based on whether it's a draw
    if(Player1.numeric == Player2.numeric):
        return True
    else:
        return False 

def CompareHighestCards(Player1, Player2): ##Returns boolean based on winning card
    if(Player1.numeric > Player2.numeric):
        return True
    else:
        return False 
    
    
class Card: ##Class for each card
    def __init__(self, value, suit, numeric):
        self.value = value
        self.suit = suit
        self.numeric = numeric
    
if __name__ == "__main__": ##Runs main function on start
    main()