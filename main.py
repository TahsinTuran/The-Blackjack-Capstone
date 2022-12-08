import random 

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_cards(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    elif 11 in card and sum(card) > 21:
        card.remove([11])
        card.append([1])    
    return sum(card)

computer_card = []
user_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card()) 
while not is_game_over:
    user_score = calculate_cards(user_card)
    computer_score = calculate_cards(computer_card)

    print(f" You total cards:{user_card}, current score is: {user_score}")
    print(f" Computer's first card is: {computer_card[0]}, current score is: {computer_score}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_wanna_deal = input("Type 'y' to get another card, type 'n' to pass:  ")
        if user_wanna_deal == "y":
            user_card.append(deal_card())
        else:
            is_game_over = True           
while computer_score != 0 or computer_score < 21:
    computer_card.append(deal_card())
    computer_score = calculate_cards(computer_card)