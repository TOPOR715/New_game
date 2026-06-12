import random

class Item():
    @staticmethod
    def weapon():
        return {
            "AK74M": {
                "Название": "Автомат Калашникова АК-74М",
                "Описание": "Величайшее оружие в мире, созданное Калашниковым",
                "Калибр": "5.45x39",
                "Вместимость магазина": "30 патронов"
            },
            "PM": {
                "Название": "Пистолет Макарова",
                "Описание": "Величайшее оружие, созданное Макаровым",
                "Калибр": "9x18",
                "Вместимость магазина": "8 патронов"
            }
        }
    
    @staticmethod
    def get_random_weapon():
        weapons = Item.weapon()
        # Возвращаем случайное оружие как словарь с ключом и значением
        weapon_name = random.choice(list(weapons.keys()))
        return {weapon_name: weapons[weapon_name]}
    
# guns = item
# print(guns.weapon())