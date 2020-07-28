import random

money = 100

#Write your game of chance functions here

def flipping_coin(betting_amount, player_decision):
    #Make sure the betting_amount is above 0.
    if betting_amount == 0:
        print(f"It is impossible for you to play, no enough money!")
        return 0
    #The game starts and flips the coin.
    print(f"Ready?, Let's flip a coin")
    print(f"You guessed {player_decision}")
    #Says which is the result of the flipping coin.
    result = random.choice(["Heads","Tails"])
    print(result)
    #Determines if player won or lost (+/- betting amount)
    if player_decision == result:
        print(f"You won ${betting_amount}")
        return betting_amount
    else:
        print(f"You lost ${betting_amount}")
        return -betting_amount

# result = random.randint(1,2)
#     #Says which is the result of the flipping coin.
#     if result == 1:
#         print("Heads")
#         result = "Heads"
#     elif result == 2:
#         print("Tails")
#         result = "Tails"
#     #Determines if player won or lost (adding or substracting the betting amount)
#     if player_decision == result:
#         print(f"You won ${betting_amount}")
#         return betting_amount
#     else:
#         print(f"You lost ${betting_amount}")
#         return -betting_amount"""

def sum_dice(betting_amount, player_decision):
    #Make sure the betting_amount is above 0.
    if betting_amount == 0:
        print(f"It is impossible for you to play, no enough money!")
        return 0
    #The game starts, the dices roll.
    print(f"Let's play Cho-Han!")
    random_chohan_one = random.randint(1,6)
    random_chohan_two = random.randint(1,6)
    sum_chohan = random_chohan_one + random_chohan_two
    print(f"The sum of the two dice is {sum_chohan}")
    #Determines if player won or lost (+/- betting amount)
    if player_decision == "Even" and sum_chohan % 2 == 0:
        print(f"You win ${betting_amount}")
        return betting_amount
    elif player_decision == "Odd" and sum_chohan % 2 != 0:
        print(f"You win ${betting_amount}")
        return betting_amount
    else:
        print(f"You lost ${betting_amount}")
        return -betting_amount

def card_draw(betting_amount_player1,betting_amount_player2):
    #Make sure the betting_amount is above 0.
    if (betting_amount_player1 == 0) or (betting_amount_player2 == 0):
        print(f"It is impossible for you to play, no enough money!")
        return 0
    #A card from a deck is draw.
    print(f"Let's play a game of cards!")
    cards = list(range(1,14))*4
    player_1_card = random.choice(cards)
    cards.remove(player_1_card)
    player_2_card = random.choice(cards)
    print(f"Player 1 card is {player_1_card}")
    print(f"Player 2 card is {player_2_card}")
    #Determines who won or lost (+/- betting amount returned ONLY for player 1)
    if player_1_card > player_2_card:
        print(f"Player 1 win ${betting_amount_player1} and Player 2 lost ${betting_amount_player2}")
        return betting_amount_player1
    elif player_2_card > player_1_card:
        print (f"Player 2 win ${betting_amount_player1} and Player 1 lost ${betting_amount_player2}")
        return -betting_amount_player1
    else:
        print (f"There is a tie")
        return 0

def roulette(betting_amount, odd_even_number_decision):
    #Make sure the betting_amount is above 0.
    if betting_amount == 0:
        print(f"It is impossible for you to play, no enough money!")
        return 0
    #The roulette turns.
    print("Let's play roulette!")
    roulette_numbers = ["00"]
    for num in range(0,37):
        roulette_numbers.append(str(num))
    winner_number_selection = random.choice(roulette_numbers)
    winner_number = int(winner_number_selection)
    print(f"And the winner number is ... {winner_number}!")
    #Determines if player won or lost (+/- betting amount)
        #If the winner_number was 0, the player shouldn't win.
    if winner_number == 0:
        print(f"You lost ${betting_amount}")
        return -betting_amount
        #If guessed number and result are the same, player wins 35 times bet.
    elif type(odd_even_number_decision) == int:
        if odd_even_number_decision == winner_number:
                print(f"You win ${betting_amount}")
                return betting_amount * 35
        #Checks to see if guessed number and the result was even.
    elif winner_number % 2 == 0 and odd_even_number_decision == "Even":
        print(f"You win ${betting_amount}")
        return betting_amount
        #Checks to see if guessed number and the result was odd.
    elif winner_number % 2 != 0 and odd_even_number_decision == "Odd":
        print(f"You win ${betting_amount}")
        return betting_amount
        # If none of the above are true, player lost.
    else:
        print(f"You lost ${betting_amount}")
        return -betting_amount

money += flipping_coin(int(money/4),"Heads")
money += sum_dice(int(money/4),10)
money += card_draw(int(money/4),200)
money += roulette(int(money/4), "Even")
print(f"Your total amount of money is ${money}!")
