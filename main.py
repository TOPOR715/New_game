import characters
import dialogi
import item
import view
import json
import music
import sys
import save
from colorama import init, Fore, Back, Style
init(autoreset=True) # СБРОС СТИЛЯ ТЕКСТА

# Hero - Наш гг, в который потом пойдут данные
Hero = characters.Player.glavniy_geroy()
Hi_jaba = dialogi.random_hi()
goodbye_jaba = dialogi.random_goodbye()



while True:
    view.Main_menu()  
    try:
        # Ввод юзера
        enter_user = int(input("> "))
        if enter_user == 1:
            view.create_person(Hero)
            break

        elif enter_user == 2:
                if Hero["Name"] is None:
                    print("Сначала создайте персонажа!")
                else:
                    view.show_hero(Hero)
        elif enter_user == 3:
            if save.hero_exists():
                Hero = save.load_hero()
                print("Игра загружена!")
                break
            else:
                print("Нет сохранения! Создай персонажа.")

        elif enter_user == 0:
            sys.exit()

    except ValueError:
        print(Fore.GREEN + "\nШо ты ввёл мудак? Вводи только цифры блэат!\n")
# Сама игра
# music.play_random_music()
while True:
        try:
            view.Menu_bar()
            enter_user_bar = int(input("\n> "))
            if enter_user_bar == 3:
                while True:
                    print (Hi_jaba)
                    view.traid_menu()
                    enter_user_bar = int(input("\n> "))
        except ValueError:
             print("Введите число\n")