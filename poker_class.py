

class Cards:

    created_cards = 0

    def __init__(self, c_value, c_color):
        print("Création d'une carte...")
        self.value = c_value
        self.color = c_color
        Cards.created_cards += 1



print("lancement du programme...")

cards1 = Cards(2, "\u2660")
print("Valeur de cards1 : {}".format(cards1.value))
print("Couleur de cards1 : {}".format(cards1.color))
print("Cartes créées : {}".format(Cards.created_cards))

cards2 = Cards(3, "\u2663")
print("Valeur de cards1 : {}".format(cards2.value))
print("Couleur de cards1 : {}".format(cards2.color))
print("Cartes créées : {}".format(Cards.created_cards))



