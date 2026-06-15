import GG_and_enemy
import item
import view
import pyglet
import json

Hero = GG_and_enemy.Player.glavniy_geroy()
printik = view

def Main_menu():
    print('''1. начать игру/создать персонажа
2. Посмотреть персонажа
3. Выход
          ''')
    
# pyglet.media.load("Dvorovye_pesni_-_Ty_ne_prishla_i_khujj_s_tobojj_62486589.mp3").play()

while True:
    Main_menu()
    try:
        enter_user = int(input("Введите число тут: "))
        if enter_user == 1:

            x = input("Введите имя: ")
            Hero["Name"] = x

            x = str(input("Введите позывной: "))
            Hero["Firstname"] = x
# =====================================================================
            try:
                x = int(input("Введите Возраст от 18 до 50: "))
                if 18 <= x <= 50:
                    Hero["Age"] = x
                else:
                    print("Возраст должен быть от 18 до 50!")
            except:
                ("Введите возраст цифрами!")
            
            x = input("Введите описание персонажа(не обязательно): ")
            if x == None:
                if x == "" or x is None:
                    Hero["dop_data"] = "Описание отсутствует"
                else:
                    Hero["dop_data"] = x

# =====================================================================            
        elif enter_user == 2:
                if Hero["Name"] is None:
                    print("Сначала создайте персонажа!")
                else:
                    view.show_hero(Hero)
        elif enter_user == 3:
            break

    except:
        print("Шо ты ввёл мудак? Вводи только цифры блэат!")

