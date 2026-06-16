import random
from playsound3 import playsound
import threading

my_music = [#"Dvorovye_pesni_-_Ty_ne_prishla_i_khujj_s_tobojj_62486589.mp3",
            "STALKER BLUES - Русская Дорога [audiovk.com].mp3",
            "Рок-Острова - Ничего не говори [audiovk.com].mp3",
            "Сплин - Мы сидели и курили [audiovk.com].mp3",
            "R.P.G - Белые дяди [audiovk.com].mp3",
            "RADIO TAPOK - Танк Алёша [audiovk.com].mp3",
            "КАСПЕР - Минувшие дни - Prod. by SKWLKR [audiovk.com].mp3",
            "Ростислав Чебыкин - Не остановиться [audiovk.com].mp3"]


def _play_loop():
    while True:
        random_music = random.choice(my_music)
        playsound("music/" + random_music)  # block=True, но в отдельном потоке

def play_random_music():
    thread = threading.Thread(target=_play_loop, daemon=True)
    thread.start()