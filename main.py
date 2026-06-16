import characters
import item
import view
import json
import music
import sys
import save

# Hero - Наш гг, в который потом пойдут данные
Hero = characters.Player.glavniy_geroy()
# Музыку в бар перетащим
# music.play_random_music()


while True:
    view.Main_menu()  
    try:
        # Ввод юзера
        enter_user = int(input("> "))
        if enter_user == 1:
            view.create_person(Hero)
            save.save_hero()
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

        elif enter_user == 4:
            sys.exit()

    except Exception:
        print("Шо ты ввёл мудак? Вводи только цифры блэат!")

while True:
        view.Menu_bar()
        enter_user = int(input("> "))

