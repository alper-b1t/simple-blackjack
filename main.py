import random

print("Blackjack Oyununa Hoşgeldiniz")
game="y"
while game=="y":    

    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def get_card_value(card):
        if card=="J" or card=="Q" or card=="K":
            return 10
        elif card=="A":
            return 11
        else:
            return int(card)

    def calculate_hand_value(card_list):
        total=0
        aces_count=0
        for card in card_list:
            card_value=get_card_value(card)
            total = total + card_value
            if card =="A":
                aces_count=aces_count+1
        while total >21 and aces_count>0:
            total=total-10
            aces_count=aces_count-1
        return total


    player_cards=[]
    dealer_cards=[]

    for user_card in range(2):
        user_first_card=random.choice(cards)
        player_cards.append(user_first_card)

    for case_card in range(2):
        case_first_card=random.choice(cards)
        dealer_cards.append(case_first_card)

    player_score=calculate_hand_value(player_cards)
    dealer_score=calculate_hand_value(dealer_cards)


    print("Kartlarınız=",player_cards,"kartlarınız degeri",player_score)
    print("Kurpiyerin kartları=",dealer_cards[0],"kapalı")

    alr=input("Tamam mı devam mı?[y/n]").lower()
    while alr!="y" and alr!="n":
        print("Lütfen y veya n giriniz")
        alr=input("Tamam mı devam mı?[y/n]").lower()

    if alr == "y":
        keep_drawing = "y"

        while keep_drawing == "y":
            new_card = random.choice(cards)
            player_cards.append(new_card)

            player_score = calculate_hand_value(player_cards)
            print("Kartlarınız =", player_cards, "Kart değeriniz =", player_score)

            if player_score >= 21:
                break

            keep_drawing = input("Devam mı? [y/n]: ").lower()

            while keep_drawing != "y" and keep_drawing != "n":
                print("Lütfen y veya n giriniz.")
                keep_drawing = input("Devam mı? [y/n]: ").lower()

    elif alr=="n":
        print("Kartlarınız=", player_cards)
        print("Kasa kart çekiyor...")

    while dealer_score < 17 and player_score <=21:
        case_new_card = random.choice(cards)
        dealer_cards.append(case_new_card)
        dealer_score=calculate_hand_value(dealer_cards)

    player_score=calculate_hand_value(player_cards)

    print("Kartlarınız =",player_cards, "kartlarınızın değeri", player_score)
    print("Kasa kartları= ",dealer_cards,"Kasa degeri=",dealer_score)
    if player_score > 21:
        print("Kasa kazandı, 21'i geçtiniz")
    elif player_score == 21:
        if dealer_score==21:
            print("berabere")
        else:
            print("tebrikler blackjack")
    elif dealer_score>21:
        print("Kasa patladı,kazandınız")
    elif dealer_score<player_score:
        print("Kazandınız")
    elif dealer_score>player_score :
        print("Kaybettiniz")
    else:
        print("Berabere")
    game=input("Tekrar oynamak ister misiniz?[y/n]").lower().strip()
    while game not in ["y", "n"]:
        print("Lütfen 'y' veya 'n' giriniz.")
        game = input("Tekrar oynamak ister misiniz? [y/n]: ").lower().strip()
