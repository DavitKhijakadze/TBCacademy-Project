# TBCacademy-Project

#ინფორმაცია თამაშზე
თამაში აწყობილია ყველასთვის კარგად ნაცნობი ჯოკრის პრინციპების იდენტურად
(წესები, პირობები და ა.შ.) ე.წ. 9-იანები.

პ.ს. ყველაფერი მაქსიმალურად სხვა ფაილში იმიტომ გავიტანე, რომ მომხმარებელი არაფერში უნდა ჩაერიოს, რომ რამე არ წაშალოს ან ა.შ.
მისი მოვალეობა მხოლოდ თამაშია.

#ფუნქციების განმარტებები game_background_process - ში

1. class Card:
    1) generate_cards - აგენერირებს 36 კარტს ჯოკრის სათამაშოდ. ასე ვთქვათ მაქვს დასტა ამ კლასში.
    2) dealing_cards - გადაეცემა მოთამაშეების რაოდენობა და დასტა. აბრუნებს თითოეული მოთამაშისთვის შემთხვევით აღებულ 9 კარტს

2. class Player:
    1) get_names - გადაეცემა მოთამაშეების რაოდენობა და შემოყავს მომხმარებლის სახელები
    2) last_person - შემთხვევითობის პრინციპით არჩევს ბოლო მოთამაშე და აბრუნებს
    გადალაგებულ სიას

3. class Main_Process:
    1) choosing_trump_card - ატარებს ვალიდაციას მომხმარებლის მიერ არჩეულ კოზირს
    2) trump_statement - მომხმარებელს აჩვენებს პირველ 3 კარტს და სთხოვს კოზირის არჩევას და 
    ამავე ფუნქციაში ვიძახებ კოზირის ვალიდაციის ფუნქციას
    3) player_word - მომხმარებლის მიერ ნათქვამ სიტყვას ატარებს ვალიდაციას
    4) ask_player_words - ეკითხება მომხმარებელს რამდენი კარტი სურს და ამავე ფუნქციაში ვატარებ ვალიდაციას
    5) choosing_move - ახდენს არჩეული სვლის ვალიდაციას
    6) alternative_move - ნატარები კარტის მიხედვით შემდეგი მოთამაშის კარტებში ეძებს მხოლოდ საჭირო ვარიანტებს, რომ სხვა სვლის უფლება არ ჰქონდეს
    7) joker_response - ფუნქცია ემსახურება პირველი მოთამაშის შემთვევაში ჯოკრის ტარების დროს სვლის ვალიდაციას
    9) joker_case - თუ პირველი კარტი ჯოკერია ნატარები ფუნქცია მუშაობს მის ლოგიკაზე. თუ მაღალი კარტია ნაცხადები მომხმარებელს მხოლოდ იმ კარტს და ჯოკერს გამოუტანს შესაძლო ვარიანტებში. იგივე ლოგიკით მუშაობს ცხადების დროს. ამ უკანასკნელში გამოაქვს ყველა შესაძლო ვარიანტი, რათა მოთამაშემ აირჩიოს.
    10) card_anchor - რაუნდის (4 კარტის ჩამოშვლის) შემდეგ ფუნქცია გადაუვლის ამ 4 კარტს და პოულობს ვის ეკუთვნის კარტი და აბრუნებს ინდექსს, ამ ინდექსით ვწვდები მიმდინარე ხელში სიაში დალაგებულ მოთამაშეებს რომ დავადგინო კარტის მფლობელი
    11) count_round_scores - კარტების ამოწურვის შემდეგ ფუნქცია ითვლის მოთამაშეების ქულებს
    12) count_true_values - მოთამაშის ქულასთან ერთად ვინახავ True ან False, რათა შემდეგში დავადგინო რაც თქვა მართლა იმდენი წაიყვანა თუ არა. ეს ფუნქცია ადგენს ეკუთვნის თუ არა პრემია მოთამაშეს.

4. class Print:
    1) print_table - კარტების ამოწურვის შემდეგ ეკრანზე გამოაქვს მოთამაშეს ნათქვამი სიტყვა და წაყვანილი კარტების რაოდენობა(ვიზუალიზაციისთვის)
    2) print_total_scores - ეკრანზე გამოაქვს მოთამაშეების ქულები თამაშის მიმდინარეობის პარარელელურად, ყოველი 9 კარტის გათამაშების შემდეგ
    3) print_names_and_cards - ეკრანზე გამოაქვს რომელი მოთამაშე რომელ კარტს ჩამოვიდა

5. class Joker:
    გადაცემული აქვს მშობელი კლასები ფუნქციების გამოსაყენებლად.

    1) game_process - აწყობილია 1 რაუნდის (9 კარტის დატრიალების) ლოგიკა. მაგ: პირველ მოთამაშეს არჩევინებს კოზირს, არცევინებს სვლას და შემდეგი პრინციპები აწყობილია პირველი კარტის (ნატარები) ირგვლივ

6. func start_game:

    ამ ფუნქციაში ხდება class joker -> game_process 16-ჯერ გამეორება, რომელიც თავის მხრივ დაყოფილია ოთხეულებად.
    ამავე ფუნქციაში ვქმნი ცვლადებს მონაცემების შესანახად შემდეგი გამოყენებისთვის.

