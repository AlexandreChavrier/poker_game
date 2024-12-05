import random
import os
import rich


def create_deck():
    deck = ['2\u2660', '3\u2660', '4\u2660', '5\u2660', '6\u2660', '7\u2660', '8\u2660', '9\u2660', '10\u2660', 'J\u2660', 'Q\u2660', 'K\u2660', '1\u2660',
            '2\u2665', '3\u2665', '4\u2665', '5\u2665', '6\u2665', '7\u2665', '8\u2665', '9\u2665', '10\u2665', 'J\u2665', 'Q\u2665', 'K\u2665', '1\u2665',
            '2\u2666', '3\u2666', '4\u2666', '5\u2666', '6\u2666', '7\u2666', '8\u2666', '9\u2666', '10\u2666', 'J\u2666', 'Q\u2666', 'K\u2666', '1\u2666',
            '2\u2663', '3\u2663', '4\u2663', '5\u2663', '6\u2663', '7\u2663', '8\u2663', '9\u2663', '10\u2663', 'J\u2663', 'Q\u2663', 'K\u2663', '1\u2663']
    random.shuffle(deck)
    return deck

def nombre_joueurs():
    joueurs = int(input("Veuillez printentrer le nombre de joueur(s) : "))
    return list(range(joueurs))
    
def deal(deck, nbr_cards):
    drawn_cards = set(random.sample(deck[:], min(nbr_cards, len(deck))))
    for cards in drawn_cards:
        deck.remove(cards)
    return list(drawn_cards)


def flop(deck, nbr):
    deck.pop()
    cards = deal(deck, nbr)
    print(cards)

def game_state():
    new_deck = create_deck()
    joueurs = nombre_joueurs()
    board = [1, 2, 3]
    
    for i in joueurs:
       joueurs[i] = input("Joueur {}, tapez Yes ou No pour voir votre main (Y/N) : ".format(i + 1))
       if joueurs[i] == "Y" or joueurs[i] == "Yes":
           print(deal(new_deck, 2))
           hide_hand = input("tapez Y pour cacher votre main : ")
           if hide_hand == "Y":
               os.system("clear")
    
    for i in board:
        board[i] = print("Tour {} : {}" .format((i), flop(new_deck, 3)))


game_state()







