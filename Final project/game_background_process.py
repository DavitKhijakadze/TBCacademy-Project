import random
from tabulate import tabulate
import json

class Card:
    
    def __init__(self):
        pass
    
    def generate_cards(self):
        suits = ["♤", "♢", "♧", "♡"]
        values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6"]
        self.cards = [f"{value}{suit}" for suit in suits for value in values]
        self.cards.remove("6♤")
        self.cards.remove("6♧")
        self.cards.append("JOKER-1")
        self.cards.append("JOKER-2")

        return self.cards
    
    def dealing_card(self, players, deck: list):
        self.cards_in_game = {}
        self.player_names = players
        self.deck = deck

        for name in self.player_names:
            hand = []
            for _ in range(9):
                random_card = random.choice(deck)
                hand.append(random_card)
                deck.remove(random_card)
            self.cards_in_game[name] = hand 
        
        return self.cards_in_game

class Player:

    def __init__(self) -> None:
        pass

    def get_names(self, players):        
        names = []
        
        while True:
            player_count = len(names) + 1
            name = input(f"Player {player_count}, please enter your nickname (text only) ✍️  : ")
            if not name or name.isdigit():
                print("= " * 80)
                print("❌ Please enter a nickname ❌")
                print("= " * 80)
                continue
            if name not in names:
                names.append(name)
            else:
                print("That nickname is already taken. Try a different one 🔁")

            if len(names) == players:
                return names
        
    def last_person(self, names: list):

        random_player = random.choice(names)
        names.remove(random_player)
        names.append(random_player)

        return names

class Main_Process:

    def __init__(self) -> None:
        pass

    def choosing_trump_card(self):
        user_choice = None
        trump_list = {1:"♤", 2:"♢", 3: "♧", 4:"♡", 5: "N/A"}
        while user_choice not in range(1, 6):
            try:
                user_choice = int((input(f'Please enter trump card by index: || 1 = ♤, 2 = ♢, 3 = ♧, 4 = ♡, 5 = N/A ||: ')))
                if user_choice not in range(1, 6):
                    print("= " * 70)
                    print("❌ Invalid choice. Please enter a number 1, 2, 3, 4, or 5 ❌")
                    print("= " * 70)
            except ValueError:
                print("= " * 70)
                print("❌ Invalid choice. Please enter a number 1, 2, 3, 4, or 5 ❌")
                print("= " * 70)
        return trump_list[user_choice]

    def trump_statement(self, name, round_counter, dealing_cards):
        print("= " * 70)
        print(" " * 30, "❗️" * 15, f"ROUND {round_counter}", "❗️" * 15)
        print()
        print(f"{name}, your first three cards are || {' | '.join(dealing_cards[name][:3])} ||", end=" ")
        trump_card = self.choosing_trump_card()
        print()
        print("= " * 70)
        return trump_card 

    def player_word(self, player_index, players_words):

        while True:
            try:
                word = int(input(f"specify how many you want to take from 0 to 9 inclusive 🤔: "))
                if word < 0 or word > 9:
                    print("= " * 70)
                    print("❌ Enter a number between 0 and 9 inclusive ❌")
                    print("= " * 70)
                elif (sum(players_words.values()) + word == 9) and player_index == 3:
                    print("= " * 70)
                    print("❌ You cannot say this number, enter it again ❌")
                    print("= " * 70)
                else:
                    return word
            except ValueError:
                print("= " * 70)
                print("❌ Enter only numbers ❌")
                print("= " * 70)

    def ask_player_words(self, dealer, dealing_cards, trump_card):
        players_words = {}
        for player_words in dealer:
            print("👀", " | ".join(dealing_cards[player_words]), "👀")
            print()
            print(f"❗️ Trump card for this round  {trump_card} ❗️")
            print()
            print(f"{player_words},", end=" ")
            Player_index = dealer.index(player_words)
            word = self.player_word(Player_index, players_words)
            print("= " * 70)
            players_words[player_words] = word
        return players_words

    def choosing_move(self, player_name, players_cards: list):
        
        enumerate_player_cards = []
        for i, card in enumerate(players_cards, start=1):
            enumerate_player_cards.append(f"{i} - {card}")
            
        while True:          
            try:
                word = int(input(f"{player_name}, choose a move by index --> {', '.join(enumerate_player_cards)}: "))
                if word < 1 or word > len(enumerate_player_cards):
                    print("= " * 70)
                    print(f"❌ Enter a number between 1 and {len(enumerate_player_cards)} inclusive ❌")
                    print("= " * 70) 
                else:   
                    return players_cards[word-1]
            except ValueError:
                print("= " * 70)
                print("❌ Enter only numbers ❌")
                print("= " * 70) 

    def alternative_move(self, main_card, current_player_cards, trump_card):

        alternative_moves = [card for card in current_player_cards if card[-1] == main_card[-1]]
        joker = []
        trump_cards = []

        if "JOKER-1" in current_player_cards or "JOKER-2" in current_player_cards:
            for card in current_player_cards:
                if card == "JOKER-1" or card == "JOKER-2":
                    joker.append(card)
        
        if trump_card != "N/A":
            for card in current_player_cards:
                if card[-1] == trump_card:
                    trump_cards.append(card)
                
        if len(alternative_moves) > 0:
            print(" "* 10, f"cards in hand   👉    {" | ".join(current_player_cards)}   👈    cards in hand")
            print()
            print(" " * 35, f"❗️ Trump card for this round  {trump_card} ❗️")
            print()
            return alternative_moves + joker
        elif len(trump_cards) > 0:
            print(" "* 10, f"cards in hand   👉    {" | ".join(current_player_cards)}   👈    cards in hand")
            print()
            print(" " * 35, f"❗️ Trump card for this round  {trump_card} ❗️")
            print()
            return trump_cards + joker
        else:
            print(" "* 10, f"cards in hand   👉    {" | ".join(current_player_cards)}   👈    cards in hand")
            print()
            print(" " * 35, f"❗️ Trump card for this round  {trump_card} ❗️")
            print()
            return current_player_cards

    def joker_response(self, player_index):
    
        if player_index != 0:
            answer = None
            while True:
                answer = input("Do you want this card? 😈 Enter 'Y' for YES, or 'N' for NO: ")
                if answer in ["Y", "N"]:
                    break
                else:
                    print("❌ Enter correct answer ❌")

            return answer
        
        else:
            take_or_high = None
            while True:
                take_or_high = input("Input 'T' for take or 'H' for high card: ")
                if take_or_high in ["T", "H"]:
                    break
                else:
                    print("❌ Enter correct answer ❌")

            suits = {1: "♤", 2: "♢", 3: "♧", 4: "♡"}
            input_suit = None   
            while True:
                try:
                    input_suit = int(input("Enter what kind of suit you want: 1-♤, 2-♢, 3-♧, 4-♡: "))
                    if input_suit in suits:
                        break
                    else:
                        print("❌ Enter correct answer ❌")
                except ValueError:
                    print("❌ Enter only numbers ❌")
            
            return f"{take_or_high} {suits[input_suit]}"

    def joker_case(self, joker_answer, player_cards, trump_card):

        deck = {
                    "♤": {"A♤": 14, "K♤": 13, "Q♤": 12, "J♤": 11, "10♤": 10, "9♤": 9, "8♤": 8, "7♤": 7},
                    "♧": {"A♧": 14, "K♧": 13, "Q♧": 12, "J♧": 11, "10♧": 10, "9♧": 9, "8♧": 8, "7♧": 7},
                    "♢": {"A♢": 14, "K♢": 13, "Q♢": 12, "J♢": 11, "10♢": 10, "9♢": 9, "8♢": 8, "7♢": 7, "6♢": 6},
                    "♡": {"A♡": 14, "K♡": 13, "Q♡": 12, "J♡": 11, "10♡": 10, "9♡": 9, "8♡": 8, "7♡": 7, "6♡": 6}
                }

        joker = [card for card in player_cards if card[:5] == "JOKER"]
        alternative_moves = []
        trump_moves = []   
        joker_suit = joker_answer[-1]

        if joker_answer[0] == "H":
            max_value = 0
            suit = None
            for card in player_cards:
                if card in deck[joker_suit] and deck[joker_suit][card] > max_value:
                    max_value = deck[joker_suit][card]
                    suit = card
            if suit:
                alternative_moves.append(suit)

            if len(alternative_moves) == 0 and trump_card != "N/A":
                for card in player_cards:
                    if card[-1] == trump_card:
                        trump_moves.append(card)

            if len(alternative_moves) > 0:
                return alternative_moves + joker
            elif len(trump_moves) > 0:
                return trump_moves + joker
            else:
                return player_cards

        elif joker_answer[0] == "T":
            for card in player_cards:
                if card[-1] == joker_suit:
                    alternative_moves.append(card)

            if len(alternative_moves) == 0 and trump_card != "N/A":
                for card in player_cards:
                    if card[-1] == trump_card:
                        trump_moves.append(card)

            if len(alternative_moves) > 0:
                    return alternative_moves + joker
            elif len(trump_moves) > 0:
                    return trump_moves + joker
            else:
                return player_cards

    def card_anchor(self, card_list_for_define_card_owner, cards_on_table: list, trump_card, first_player_joker_answer):
        
        deck = {
                "♤": {"A♤": 14, "K♤": 13, "Q♤": 12, "J♤": 11, "10♤": 10, "9♤": 9, "8♤": 8, "7♤": 7},
                "♧": {"A♧": 14, "K♧": 13, "Q♧": 12, "J♧": 11, "10♧": 10, "9♧": 9, "8♧": 8, "7♧": 7},
                "♢": {"A♢": 14, "K♢": 13, "Q♢": 12, "J♢": 11, "10♢": 10, "9♢": 9, "8♢": 8, "7♢": 7, "6♢": 6},
                "♡": {"A♡": 14, "K♡": 13, "Q♡": 12, "J♡": 11, "10♡": 10, "9♡": 9, "8♡": 8, "7♡": 7, "6♡": 6}
                }

        main_card = cards_on_table[0]

        if "JOKER-1Y" in card_list_for_define_card_owner or "JOKER-2Y" in card_list_for_define_card_owner: # თუ ჯოკერს უნდა
            for card in card_list_for_define_card_owner:
                if card[-1] == "Y":
                    joker_player_index = card_list_for_define_card_owner.index(card)
            return joker_player_index
        
        elif main_card in ["JOKER-1", "JOKER-2"] and first_player_joker_answer[0] == "T" and first_player_joker_answer[-1] != trump_card and trump_card != "N/A": # როცა ნაცხადებია წაყვანა და ასევე კოზირიც ნაცხადებია
            trump_cards_on_table = [card for card in cards_on_table if card[-1] == trump_card]
            potential_cards = [card for card in cards_on_table if card[-1] == first_player_joker_answer[-1]]

            if len(trump_cards_on_table) > 0:
                max_point = 0
                player_index = None
                for card in cards_on_table:
                    if card[-1] == trump_card and deck[card[-1]][card] > max_point:
                        player_index = cards_on_table.index(card)
                        max_point = deck[card[-1]][card]
                return player_index       
            elif len(potential_cards) > 0:
                max_point = 0
                player_index = None
                for card in cards_on_table:
                    if card[-1] == first_player_joker_answer[-1] and deck[card[-1]][card] > max_point:
                        player_index = cards_on_table.index(card)
                        max_point = deck[card[-1]][card]
                return player_index
            else:
                return 0

        elif main_card in ["JOKER-1", "JOKER-2"] and first_player_joker_answer[0] == "H" and first_player_joker_answer[-1] != trump_card and trump_card != "N/A": # როცა მაღალი კარტია ნაცხადები და ასევე ნაცხადებია კოზირიც
            trump_cards_on_table = [card for card in cards_on_table if card[-1] == trump_card]
            if len(trump_cards_on_table) == 0:
                return 0
            else:
                max_point = 0
                player_index = None
                for card in cards_on_table:
                    if card[-1] == trump_card and deck[card[-1]][card] > max_point:
                        player_index = cards_on_table.index(card)
                        max_point = deck[card[-1]][card]
                return player_index

        elif main_card in ["JOKER-1", "JOKER-2"] and first_player_joker_answer[0] == "T" and trump_card == "N/A": # როცა ნაცხადებია წაყვანა და კოზირი არ გვაქვს
            potential_cards = [card for card in cards_on_table if card[-1] == first_player_joker_answer[-1]]
            if len(potential_cards) == 0:
                return 0
            else:
                max_point = 0
                player_index = None
                for card in cards_on_table[1:]:
                    if card in deck[card[-1]] and deck[card[-1]][card] > max_point:
                        player_index = cards_on_table.index(card)
                        max_point = deck[card[-1]][card]
                return player_index

        elif main_card in ["JOKER-1", "JOKER-2"] and first_player_joker_answer[0] == "H" and trump_card == "N/A": # როცა მაღალი კარტია ნაცხადები და კოზირი არ გვაქვს
            return 0

        elif main_card[-1] in deck.keys() and trump_card != "N/A": #თუ კოზირია ნაცხადები
            trump_cards_on_table = [card for card in cards_on_table if card[-1] == trump_card]
            potential_cards = [card for card in cards_on_table if card[-1] == main_card[-1]]

            if len(trump_cards_on_table) > 0:
                max_point = 0
                player_index = None
                for card in cards_on_table:
                    if card[-1] == trump_card and deck[card[-1]][card] > max_point:
                        player_index = cards_on_table.index(card)
                        max_point = deck[card[-1]][card]
                return player_index       
            elif len(potential_cards) > 0:
                max_point = 0
                player_index = None
                for card in cards_on_table:
                    if card[-1] == main_card[-1] and deck[card[-1]][card] > max_point:
                        player_index = cards_on_table.index(card)
                        max_point = deck[card[-1]][card]
                return player_index
            else:
                return 0
        
        elif main_card[-1] in deck.keys() and trump_card == "N/A":  # თუ კოზირი ბეზია
            max_point = 0
            player_index = None
            for card in cards_on_table:
                if card in deck[main_card[-1]] and deck[main_card[-1]][card] > max_point:
                    player_index = cards_on_table.index(card)
                    max_point = deck[main_card[-1]][card]
            return player_index             

    def count_round_scores(self, player_words, cards_taken):

        round_scores = {}
        joker_scores = {0: 50, 1: 100, 2: 150, 3: 200, 4: 250, 5: 300, 6: 350, 7: 400, 8: 450, 9: 900}

        for player, word in player_words.items():
            if word > 0 and cards_taken[player] == 0:
                round_scores[player] = [-500, False]
            elif word == cards_taken[player]:
                round_scores[player] = [joker_scores[player_words[player]], True]
            elif word < cards_taken[player] or word > cards_taken[player]:
                round_scores[player] = [cards_taken[player] * 10, False]

        return round_scores    
    
    def count_true_values(self, quarter_scores):

        true_counts = {}
        bonus_players = {}

        for round_data in quarter_scores.values():
            for player, points in round_data.items():
                if player not in true_counts:
                    true_counts[player] = 0
                if points[1]: 
                    true_counts[player] += 1
        
        for name, true in true_counts.items():
            if true == 4:
                max_dict = max(quarter_scores.values(), key=lambda x: x[name])
                highest_digit = max_dict[name][0]
                bonus_players[name] = highest_digit
        
        for name, bonus in bonus_players.items():
            quarter_scores[4][name][0] += bonus
   

        return quarter_scores

    def find_winner(self, points):
    
        sum_of_points = {}
        for hand, rounds in points.items():
            for name, points in rounds.items():
                if name in sum_of_points:
                    sum_of_points[name] += points[0]
                else:
                    sum_of_points[name] = points[0]
        
        winner = None
        max_point = 0
        for name, points in sum_of_points.items():
            if points > max_point:
                winner = name
                max_point = points
    
        return winner

class Print:

    def __init__(self) -> None:
        pass

    def print_table(self, round_scores, players_words, cards_taken):
        table_data = []
        for name, word_score in players_words.items():
            taken_cards = str(cards_taken[name])
            score = round_scores[name][0]
            table_data.append([name, word_score, taken_cards, score])
        headers = ["Name", "Word", "Taken Cards", "Score"]
        alignments = ["left", "center", "center", "right"]

        print(tabulate(table_data, headers=headers, tablefmt="grid", numalign="right", stralign=alignments))

    def print_total_scores(self, total_scores, player_names):

        headers = ['Round'] + player_names
        table = []
        total_points = {player: 0 for player in player_names}  # Initialize with all player names

        for round_num, scores in total_scores.items():
            row = [round_num] + [scores.get(player, [0, False])[0] for player in player_names]
            table.append(row)

        for player in player_names:
            total_points[player] = sum(total_scores[round_num].get(player, [0, False])[0] for round_num in total_scores)

        print(tabulate(table, headers=headers, tablefmt='grid'))
        print("\nTotal Points After All Rounds:")
        for player, points in total_points.items():
            print(player, ":", points)

    def print_names_and_cards(self, names, cards):

        combined_data = [names, cards]

        print(tabulate(combined_data, tablefmt="psql", headers="firstrow"))

class Joker(Player, Main_Process, Print):

    def __init__(self):
        super().__init__()

    def game_process(self, dealer_per_round, dealing_cards, trump_card):      
                cards_on_table = []
                card_list_for_define_card_owner = []
                main_card = None
                first_player_joker_answer = None

                for player in dealer_per_round:
                    if player == dealer_per_round[0]:
                        print(" "* 10, f"cards in hand   👉    {" | ".join(dealing_cards[player])}   👈    cards in hand")
                        print()
                        print(" " * 35, f"❗️ Trump card for this round  {trump_card} ❗️")
                        print()
                        player_move = self.choosing_move(player, dealing_cards[player])
                        if player_move in ["JOKER-1", "JOKER-2"]:
                            first_player_joker_answer = self.joker_response(dealer_per_round.index(player))
                        cards_on_table.append(player_move)
                        card_list_for_define_card_owner.append(player_move)
                        main_card = cards_on_table[0]
                        print("= " * 70)
                        print(" " * 45, "cards on table")
                        print()
                        self.print_names_and_cards(dealer_per_round, cards_on_table)
                        print("= " * 70)
                        dealing_cards[player].remove(player_move)              
        
                    else:
                        if cards_on_table[0] in ["JOKER-1", "JOKER-2"]:
                            print(" "* 10, f"cards in hand   👉    {" | ".join(dealing_cards[player])}   👈    cards in hand")
                            print()
                            print(" " * 35, f"❗️ Trump card for this round  {trump_card} ❗️")
                            print()
                            moves_when_joker_is_main_card = self.joker_case(first_player_joker_answer, dealing_cards[player], trump_card)
                            chosen_move_validation = self.choosing_move(player, moves_when_joker_is_main_card)
                            cards_on_table.append(chosen_move_validation)
                            card_list_for_define_card_owner.append(chosen_move_validation)
                            dealing_cards[player].remove(chosen_move_validation)                   
                        else:
                            next_move = self.alternative_move(main_card, dealing_cards[player], trump_card)
                            chosen_move_validation = self.choosing_move(player, next_move)
                            cards_on_table.append(chosen_move_validation)
                            card_list_for_define_card_owner.append(chosen_move_validation)
                            dealing_cards[player].remove(chosen_move_validation)
                        
                        if chosen_move_validation in ["JOKER-1", "JOKER-2"]:
                            need_or_not = self.joker_response(dealer_per_round.index(player))
                            card_list_for_define_card_owner.remove(card_list_for_define_card_owner[-1])
                            card_list_for_define_card_owner.append(chosen_move_validation + need_or_not)
                
                                                                
                        print("= " * 70)
                        print(" " * 45, "cards on table")
                        print()
                        self.print_names_and_cards(dealer_per_round, cards_on_table)          
                        print("= " * 70) 

                return card_list_for_define_card_owner, cards_on_table, first_player_joker_answer

def start_game():
        
        NUMBER_OF_PLAYERS = 4
        card_deck = Card()  
        main_process = Joker()
        player_names = main_process.get_names(NUMBER_OF_PLAYERS) 
        dealer = main_process.last_person(player_names)
        quarter_scores = {}
        total_scores = {}

        round_counter = 1
        for _ in range(4):
            
            for name in dealer:
                
                all_card = card_deck.generate_cards()   
                dealing_cards = card_deck.dealing_card(dealer, all_card)
                dealer_per_round = dealer
                players_words = {}
                cards_taken = {name: 0 for name in player_names}
                trump_card = main_process.trump_statement(name, round_counter, dealing_cards)
                player_index = dealer.index(name)
                list_for_asking_words = dealer[player_index:] + dealer[:player_index]
                word = main_process.ask_player_words(list_for_asking_words, dealing_cards, trump_card)
                players_words = word

                per_hand = 0
                while per_hand != 9:

                    card_list_for_define_card_owner, cards_on_table, first_player_joker_answer = main_process.game_process(dealer_per_round, dealing_cards, trump_card)           
                    card_taker = main_process.card_anchor(card_list_for_define_card_owner, cards_on_table, trump_card, first_player_joker_answer)
                    dealer_per_round = dealer_per_round[card_taker:] + dealer_per_round[:card_taker]
                    cards_taken[dealer_per_round[0]] += 1
                    round_scores = main_process.count_round_scores(players_words, cards_taken)
                    quarter_scores[round_counter] = round_scores
                    with open(r"C:\Users\user\Desktop\TBCacademy-Project\Final project\quarter_points.json", 'w') as json_file:
                        json.dump(quarter_scores, json_file, indent=4)                                
                    print(" " * 40, f"🔴🔴🔴  {dealer_per_round[0]} took the card   🔴🔴🔴")
                    print("= " * 70)
                    per_hand += 1

                main_process.print_table(round_scores, players_words, cards_taken)
                print()
                main_process.print_total_scores(quarter_scores, dealer)
                print("= " * 70)
                round_counter += 1

            bonus_points = main_process.count_true_values(quarter_scores)
            total_scores.update(bonus_points)
            with open(r"C:\Users\user\Desktop\TBCacademy-Project\Final project\total_points.json", 'w') as json_file:
                json.dump(total_scores, json_file, indent=4)
            main_process.print_total_scores(total_scores, dealer)  
            quarter_scores.clear()
            print("= " * 70)
        
        winner = main_process.find_winner(total_scores)
        print(" " * 30, f"🏆🏆🏆  The winner is {winner}  🏆🏆🏆")

