from game_background_process import *
import json


def main():

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
            word = main_process.ask_player_words(dealer, dealing_cards)
            players_words = word

            per_hand = 0
            while per_hand != 1:

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
            main_process.print_total_scores(quarter_scores)
            print("= " * 70)
            round_counter += 1

        bonus_points = main_process.count_true_values(quarter_scores)
        total_scores.update(bonus_points)
        with open(r"C:\Users\user\Desktop\TBCacademy-Project\Final project\total_points.json", 'w') as json_file:
            json.dump(total_scores, json_file, indent=4)
        main_process.print_total_scores(total_scores)  
        quarter_scores.clear()
        print("= " * 70)
            

if __name__ == "__main__":
    main()
