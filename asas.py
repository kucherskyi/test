

import time
import random


def card_deck():
    signs = ['Spades','Hearts','Clubs','Diamonds']
    num = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    deck = [[i,j] for j in signs for i in num]
    asd = deck
    cardlist = {}
    b = {}
    for elemen in asd:
        cardlist.update(b)
        b = dict([elemen])
        #card = elemen
        #deck.remove(elemen)
        print elemen
        print b

#card_deck()

def cards():
    a = 0
    signs = ['Spades','Hearts','Clubs','Diamonds']
    num = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    deck = [[j+' of '+i] for j in num for i in signs]
    b = []
    while a < 52: 
        card = random.choice(deck)
        deck.remove(card)
        b.append(card)
        a = a + 1
        #print cardlist
    print random.choice(b)

cards()

def cardss():

    a = 0
    signs = ['Spades','Hearts','Clubs','Diamonds']
    num = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    deck = dict( [i,j] for j in num for i in signs )

    print deck

#cardss()
def deck():
    rank = random.choice( ('A','2','3','4','5','6','7','8','9','T','J','Q','K') )
    suit = random.choice( ('c','d','h','s') )
    carddeck = [[i,j] for j in rank for i in suit]
    print carddeck
    
#deck()
