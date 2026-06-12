import GG_and_enemy

def show_hero(hero_data):
    print(f'''
Ваш персонаж:
Имя: {hero_data["Name"]}
Позывной: {hero_data["Firstname"]}
Возраст: {hero_data["Age"]}
Описание: {hero_data["dop_data"]}
Инвентарь: {hero_data["inventar"]}
Хп в голове: {hero_data["head"]}
Хп в груди: {hero_data["thorax"]}
Хп в левой руке: {hero_data["left arm"]}
Хп в правой руке: {hero_data["right arm"]}
Хп в животе: {hero_data["stomach"]}
Хп в левой ноге: {hero_data["left leg"]}
Хп в правой ноге: {hero_data["right leg"]}
Хп всего: {hero_data["full_hp"]}
''')