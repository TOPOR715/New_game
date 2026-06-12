import GG_and_enemy
import item

Hero = GG_and_enemy.Player.glavniy_geroy()

def Main_menu():
    print('''1. начать игру
2. Посмотреть персонажа
          ''')
    
while True:
    Main_menu()
    try:
        enter_user = int(input("Введите число тут: "))
        if enter_user == 1:
            x = input("Введите имя: ")
            Hero["Name"] = x
            print(f'''Ваш персонаж создан:
Имя: {Hero["Name"]}
Позывной: {Hero["Firstname"]}
Возраст: {Hero["Age"]}
Описание: {Hero["dop_data"]}
Инвентарь: {Hero["inventar"]}
Хп в голове: {Hero["head"]}
Хп в груди: {Hero["thorax"]}
Хп в левой руке: {Hero["left arm"]}
Хп в правой руке: {Hero["right arm"]}
Хп в животе: {Hero["stomach"]}
Хп в левой ноге: {Hero["left leg"]}
Хп в правой ноге: {Hero["right leg"]}
Хп всего: {Hero["full_hp"]}





''')

    except:
        print("Шо ты ввёл мудак? Вводи только цифры блэат!")