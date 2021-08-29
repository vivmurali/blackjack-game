import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.value = values[number]

    def __str__(self):
        return f"{self.number} of {self.suit}"

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self):
        self.dealerdeck = []
        for suit in suits:
            for rank in ranks:
                self.dealerdeck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.dealerdeck)

    def deal(self):
        return self.dealerdeck.pop(0)


# Chips are like money for betting
class Chips:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"You currently hold ${self.balance}"


player_chips = Chips(2000)
game_state = True
while game_state:

    dealer_deck = Deck()
    dealer_deck.shuffle()
    dealerhand = []
    playerhand = []
    print(player_chips)
    playagain_loop = True
    while playagain_loop:

        player_bet = int(input("How much would you like to bet: "))
        print("The dealer will now deal your hand")
        dealerhand.append(dealer_deck.deal())
        dealerhand.append(dealer_deck.deal())
        playerhand.append(dealer_deck.deal())
        playerhand.append(dealer_deck.deal())
        print(f"""The dealer holds {dealerhand[0]} and an another card
You hold {playerhand[0]} and {playerhand[1]}
What would you like to do?  
    """)

        hit_loop = False
        hit_call_loop = True
        while hit_call_loop:
            player_decision = input("Hit or Call: ")
            if player_decision.upper() == "HIT":
                hit_loop = True
                while hit_loop:
                    playerhand.append(dealer_deck.deal())
                    print(f"""You chose hit
You got the {playerhand[-1]}
You currently hold {playerhand[0:]}""")
                    hit_again = input("Do You want to Hit again (Y/N): ")
                    if hit_again.upper() == "Y":
                        continue
                    else:
                        hit_loop = False
            elif player_decision.upper() == "CALL":
                sum_playerhand = 0
                sum_dealerhand = 0
                for card in playerhand:
                    if card.value == [1, 11]:
                        card.value = int(input("It seems like you have a Ace card.What value would you like to assign it- 1 or 11:"))
                    sum_playerhand = sum_playerhand + card.value
                print(f"The total sum of all your cards is {sum_playerhand}")
                if sum_playerhand > 21:
                    print("Sorry you lost the bet")
                    player_chips.balance = player_chips.balance - player_bet
                    playagain_loop = False
                    break

                dealer_hit_loop = True
                while dealer_hit_loop:
                    for card in dealerhand:
                        if card.value == [1, 11]:
                            card.value = 11
                        sum_dealerhand = sum_dealerhand + card.value
                    print(f"The dealer holds {dealerhand}")
                    print("The dealer decides to hit")
                    dealerhand.append(dealer_deck.deal())

                    if sum_dealerhand >= 17:
                        dealer_hit_loop = False
                print("The dealer calls his hand!!")
                print(f"The dealer currently holds {dealerhand}")
                print(f"The dealer's total sum of cards is {sum_dealerhand}")
                hit_call_loop = False
                if sum_dealerhand < sum_playerhand and sum_playerhand < 21:
                    print("The player wins!!!")
                    print(f"You win ${player_bet*2}")
                    player_chips.balance = player_chips.balance + (player_bet*2)

                elif sum_dealerhand > sum_playerhand and sum_dealerhand < 21:
                    print("The player loses")
                    player_chips.balance = player_chips.balance - player_bet
