import random
import collections

SUIT = ['diamonds', 'clubs', 'hearts', 'spades']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_deck():
    deck = []
    for suit in SUIT:
        for value in VALUES:
            deck.append((suit, value))
    
    return deck

def get_hand(deck, hand_size):
    hand = random.sample(deck, hand_size)
    return hand

def main(hand_size, attempts):
    deck = create_deck()
    hands = []
    
    for _ in range(attempts):
        hand = get_hand(deck, hand_size)
        hands.append(hand)
    
    even = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])
        
        counter = dict(collections.Counter(values))
        for val in counter.values():
            if val == 2: # Strictly 2
                even += 1
    
    p_of_even = even / attempts
    print('P(even) in a hand of {h:=0d} cards in {a:=0d} attempts is: {m:=0.2f}%'.format(h=hand_size, a=attempts, m=p_of_even * 100))

if __name__ == '__main__':
    hand_size = int(input('Hand\'s size: '))
    attempts = int(input('Number of attempts: '))
    main(hand_size, attempts)