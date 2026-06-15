import random

class Item():
    @staticmethod
    def weapon():
        return {
            "AK74M": {
                "Название": "Автомат Калашникова АК-74М",
                "Описание": "Величайшее оружие в мире, созданное Калашниковым",
                "Калибр": "5.45x39",
                "Вместимость магазина": "30 патронов",
                "price": 10000
            },
            "PM": {
                "Название": "Пистолет Макарова",
                "Описание": "Величайшее оружие, созданное Макаровым",
                "Калибр": "9x18",
                "Вместимость магазина": "8 патронов",
                "price": 5000
            }
        }
    
    def food():
        canned_food={}

    
    @staticmethod
    def get_random_weapon():
        weapons = Item.weapon()
        # Возвращаем случайное оружие как словарь с ключом и значением
        weapon_name = random.choice(list(weapons.keys()))
        return {weapon_name: weapons[weapon_name]}
    