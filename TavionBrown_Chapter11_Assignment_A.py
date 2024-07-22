import random

class Deck:
    def __init__(self):
        # Initialize an empty list to hold the cards
        self.cards = []
        
        # Define the suits and values of the cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        # Create a card for each combination of suit and value
        for suit in suits:
            for value in values:
                self.cards.append(f'{value} of {suit}')

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.cards)

    def deal_hand(self, num_cards):
        # Deal a hand with a specified number of cards
        hand = random.sample(self.cards, num_cards)  # Select num_cards random cards from the deck
        for card in hand:
            self.cards.remove(card)  # Remove each card in the hand from the deck
        return hand  # Return the hand of cards

    def draw_cards(self, indices):
        # Draw cards from the deck based on the specified indices
        drawn_cards = []
        for index in indices:
            drawn_cards.append(self.cards[index])  # Add the card at the specified index to the drawn cards
            self.cards.pop(index)  # Remove the card from the deck
        return drawn_cards  # Return the drawn cards


def main():
    deck = Deck()
    deck.shuffle()
    
    # Deal initial poker hand
    hand = deck.deal_hand(5)
    print("Your poker hand:")
    for i, card in enumerate(hand):
        print(f"{i+1}: {card}")

    # Prompt user for cards to replace
    replace_indices = input("Enter the indices (1-5) of the cards to replace, separated by commas (e.g., 1, 3, 5): ")
    replace_indices = [int(index.strip()) - 1 for index in replace_indices.split(',')]

    # Draw new cards
    drawn_cards = deck.draw_cards(replace_indices)

    # Print new hand after drawing
    print("\nYour new poker hand:")
    for i, card in enumerate(hand):
        if i in replace_indices:
            print(f"{i+1}: {drawn_cards.pop(0)} (Replaced)")
        else:
            print(f"{i+1}: {card}")

if __name__ == "__main__":
    main()
