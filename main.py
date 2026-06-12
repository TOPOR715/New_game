import GG_and_enemy
import item
import view

Hero = GG_and_enemy.Player.glavniy_geroy()
printik = view

def Main_menu():
    print('''1. начать игру
2. Посмотреть персонажа
3. Выход
          ''')
    
while True:
    Main_menu()
    try:
        enter_user = int(input("Введите число тут: "))
        if enter_user == 1:
            x = input("Введите имя: ")
            Hero["Name"] = x

            x = int(input("Введите Возраст от 18 до 50: "))
            if 18 <= x <= 50:
                Hero["Age"] = x
                printik.show_hero(Hero)
            else:
                print("Возраст должен быть от 18 до 50!")
        elif enter_user == 3:
            break

    except:
        print("Шо ты ввёл мудак? Вводи только цифры блэат!")