import random

suites = ['\u2665', '\u2666', '\u2663', '\u2660']
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

class Deck:    
    """
    It will be used to make a deck from suites and ranks.
    This deck will be shuffled and divided into minor decks with
    equal number of cards among the players.
    """
    
    def __init__(self):
        print("Init ordered deck!")
        self.deck = [(rank, suite) for suite in suites for rank in ranks]
        # print(self.deck)
        
    def shuffle_deck(self):
        print("Shuffling deck...")
        random.shuffle(self.deck)
        return self.deck
        
    def split_deck(self, deck, hands = {}):        
        while len(deck):
            for hand in hands.values():
                hand.append(deck.pop())
        return hands
        
class Hand:
    """
    Each player has a Hand and can add or remove cards from that hand.
    So we will perform the add and pop cards here.
    """
    
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        return str(self.cards)
    
    def __len__(self):
        return len(self.cards)
        
    def add_cards(self, added_cards):
        return self.cards.extend(added_cards)
        
    def pop_card(self):
        return self.cards.pop()
    
class Player:
    """
    This class will have the name of the player.
    It will also have the instance of Hand class object.
    """
    
    def __init__(self, name, hand = []):
        self.name = name
        self.hand = hand
        
    def __repr__(self):
        return '{}: '.format(str(self.name)) + str(self.hand)  
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) > 3:
            for i in range(3): 
                war_cards.append(self.hand.cards.pop())
        else:
            print("Player {} does not have enough cards and loses this round.".format(self.name))
            war_cards.extend(self.hand.cards)
            self.hand.cards.clear()
        return war_cards
        
    def still_has_cards(self):
        return len(self.hand.cards)


def main():
    deck = Deck()
    players = {}
    num = input("Please enter the number of players: ")
    for i in range(int(num)):
        name = input("Please enter player's name: ")
        players[name] = []
    deck.split_deck(deck.shuffle_deck(), players)
    # for player in players.items():
    #     print(player)
        
    ### Player in the game
    names = list(players.keys())
    play_1 = Player(names[0], Hand(players[names[0]]))
    play_2 = Player(names[1], Hand(players[names[1]]))
    
    ### Play
    table_cards = []
    game_count = 0
    war_count = 0
    
    while play_1.still_has_cards() and play_2.still_has_cards():
        game_count += 1
        print("Round {}: ".format(game_count))
        p1_card = play_1.hand.pop_card()
        print("Player {} shows card: {} ".format(play_1.name, p1_card))
        p2_card = play_2.hand.pop_card()
        print("Player {} shows card: {} ".format(play_2.name, p2_card))
        table_cards.append(p1_card)
        table_cards.append(p2_card)

        if ranks.index(p1_card[0]) == ranks.index(p2_card[0]):
            print("A WAR!!! Two players need to remove 3 war cards!")
            war_count += 1
            table_cards.extend(play_1.remove_war_cards())
            table_cards.extend(play_2.remove_war_cards())
            
        elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
            print("Player {} loses this round".format(play_1.name))
            play_2.hand.add_cards(table_cards)
            table_cards.clear()
        else:
            print("Player {} loses this round".format(play_2.name))
            play_1.hand.add_cards(table_cards)
            table_cards.clear()
        
    if play_1.still_has_cards():
        print("Player {} wins this game! Congratulate!!!".format(play_1.name))
        play_1.hand.add_cards(table_cards)
    else: 
        print("Player {} wins this game! Congratulate!!!".format(play_2.name))
        play_2.hand.add_cards(table_cards)
        
    print("The game ends after {} rounds with {} wars.".format(game_count, war_count))
    print("{} has {} cards and {} has {} cards.".format(play_1.name, len(play_1.hand), play_2.name, len(play_2.hand)))
        
if __name__ == '__main__': main()
