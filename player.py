from resources import *
import random

class Player():
    def __init__(self,deck_type="standard",player_name="Player1"):
        if deck_type == "standard":
            self.side_deck = standard_deck()
        self.player_name = player_name
        self.score = 0
        self.hand = self.select_hand_from_deck(self.deck)
        self.player_field = []
        player.stand = False

    def display_hand():
        #implement displaying hand and current number
        pass
    
    def select_hand_from_deck(self, deck):
        hand = []
        for _ in range(1,5):
            choice = random.randint(0,len(self.side_deck)-1)
            hand.append(self.side_deck.pop(choice))
        return hand

    def update_field(card):
        self.player_field.append(card)

    def choice(player):
        """
        AI to make a choice based on current hand
        """
        if self.score == 20:
            self.stand = True
        if self.score > 20:
            pass

