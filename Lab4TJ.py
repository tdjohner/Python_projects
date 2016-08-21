#--------------------------
#   Lab2TJ.py             -
#--------------------------
#   Teagan Johner         -
#--------------------------

import random

def make_deck():
    suits = 'DCHS'
    pips = 'A23456789TJQK'
    deck = []
    for i in range(len(suits)):
        for c in range(len(pips)):
            deck.append( pips[c] + suits[i] )
    random.shuffle(deck)
    return deck
            
            

def deal_blackjack(deck, num_of_players):
    table = []
    for c in range(num_of_players):
        hands = [] 
        for i in range(2):
            hands.append(deck.pop(0))
        table.append(hands)
    return table


def print_blackjack(hands):
    for c in range(len(hands[0])):
        print()
        for i in range(len(hands)):
            print(hands[i][c], '     ', end = '')
            
            
            
#def get_max(hands):
            
        
        
        
    





        
    