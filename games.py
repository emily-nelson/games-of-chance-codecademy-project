import random

money = 100

#Write your game of chance functions here
def coin_flip(bet, guess):
    if bet > money:
        print("Insufficient funds!")
        print("\n")
        return 0
    
    result = ['heads', 'tails']
    if random.choice(result) == guess:
        print("HEADS")
        print("You win!")
        print("Money: " + str(money + bet))
        return bet
    else:
        print("TAILS")
        print("You lose!")
        print("Money: " + str(money - bet))
        return 0 - bet

def cho_han(bet, guess):
    if bet > money:
        print("Insufficient funds!")
        print("\n")
        return 0
    print("\n")
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    result = roll_1 + roll_2
    print("The result is " + str(result))
    if result % 2 == 0 and guess == "even":
        print("You guessed correctly!")
        print("Money: " + str(money+bet))
        return bet
    elif result % 2 != 0 and guess == "odd":
        print("You guessed correctly!")
        print("Money: " + str(money + bet))
        return bet
    else:
        print("You guessed incorrectly! You lost: ")
        print("Money: " + str(money-bet))
        return 0 - bet

def higher_card(bet):
    if bet > money:
        print("Insufficient funds!")
        return 0
    print("\n")
    card_1 = random.randint(0, 14)
    card_2 = random.randint(0, 14)

    if card_1 > card_2:
        print("You win!")
        print("Money: " + str(money+bet))
        return bet 
    elif card_1 == card_2:
        print("Draw!")
        print("Money: " + str(money))
        return 0
    else:
        print("You lose!")
        print("Money: " + str(money - bet))
        return 0 - bet
    


#Call your game of chance functions here

money += (coin_flip(50, "heads"))
money += (cho_han(50, "odd"))
money += (higher_card(50))