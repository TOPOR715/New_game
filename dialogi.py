import random

# Trader JABA

def random_hi():
    words_hi = ["Ну здарова, чего пришёл?", "Чё хотел?", "Тут недавно подвоз был. Хабар нужен?"]
    return random.choice(words_hi)
        
def random_goodbye():
    words_goodbye = ["Ну и пошёл на хер отседава!", "Давай, проваливай", "А Я уж собирался тебя выгонять"]
    return random.choice(words_goodbye)