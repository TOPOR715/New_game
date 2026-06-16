import json
import os

SAVE_DIR = "save"
SAVE_FILE = os.path.join(SAVE_DIR, "hero.json")

def save_hero(hero_data):
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print("Папка save создана")
    
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(hero_data, f, ensure_ascii=False, indent=4)
    print("Персонаж сохранён!")

def load_hero():
    """Загружает персонажа из JSON"""
    if not os.path.exists(SAVE_FILE):
        print("Нет сохранения!")
        return None
    
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        hero_data = json.load(f)
    print("Персонаж загружен!")
    return hero_data

def hero_exists():
    return os.path.exists(SAVE_FILE)