import characters


def Main_menu():
    print('''1. начать игру/создать персонажа
2. Посмотреть персонажа
3. Продолжить
4. Выход
          ''')
    
def Menu_bar():
        print('''Бар Жабы. Хорошее место для отдыха и возможности закупиться и что-то продать
1. Осмотреться
2. Торговец
3. Выйти в рейд''')




def show_hero(hero_data):
    print(f'''
Ваш персонаж:
Имя: {hero_data["Name"]}
Позывной: {hero_data["Firstname"]}
Возраст: {hero_data["Age"]}
Описание: {hero_data["dop_data"]}
Инвентарь: {hero_data["inventar"]}
Голод: {hero_data["hunger"]}
Жажда: {hero_data["thirst"]}
Хп в голове: {hero_data["head"]}
Хп в груди: {hero_data["thorax"]}
Хп в левой руке: {hero_data["left arm"]}
Хп в правой руке: {hero_data["right arm"]}
Хп в животе: {hero_data["stomach"]}
Хп в левой ноге: {hero_data["left leg"]}
Хп в правой ноге: {hero_data["right leg"]}
Хп всего: {hero_data["full_hp"]}
''')
    
# Создание перса
def create_person(Hero):
    x = input("Введите имя: ")
    Hero["Name"] = x
            # Ввод позывного
    x = str(input("Введите позывной: "))
    Hero["Firstname"] = x
            # Ввод возраста и проверка на число
    while True:
        try:
            x = int(input("Введите Возраст от 18 до 50: "))
            # Если x больше 18 и меньше 50 - то норм, в остальном: Ебанулся? Давай, шурши обратно
            if 18 <= x <= 50:
                Hero["Age"] = x
                break
            else:
                print("Возраст должен быть от 18 до 50!")
        except:
            # Чё те блять сказали? Пиши цифрами! Дегенерат
            print("Введите возраст цифрами!")

    # Описание юзера
    x = input("Введите описание персонажа(не обязательно): ")
    # Если описание пустое, то мы делаем пишем "описания нема", если туда чёт вписали, то х приравниваем в переменную|is - является-ли?(Проверяет идентичность — один ли это и тот же объект в памяти)
    if x == "" or x is None:
        Hero["dop_data"] = "Описание отсутствует"
    else:
        Hero["dop_data"] = x
