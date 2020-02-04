import random
from player import Player

def draw_and_update(p1,o1,current_player):
    card = random.randint(1,10)
    if current_player:
        o1.choice(p1)
        if not o1.stand:
            o1.update_field(card)
            return 1 #return 1 so that next player is player
        else:
            return 1
    else:
        p1.update_field(card)
        return 0 #return 0 so that next player is opponent
    

def run_game():
    game_running = True
    player_name_choice = input("Input player name: ")
    p1 = Player("standard", player_name_choice)
    o1 = Player("standard", player_name="opponent 1")
    current_player = random.randint(0,1) # 0=player 1=opponent
    while game_running:
        if p1.score > 20 or o1.score > 20:
            run_game = False
        #draw and update
        current_player = draw_and_update(p1,o1,current_player)
        #display


if __name__ == "__main__":
    run_game()