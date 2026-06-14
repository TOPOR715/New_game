# thorax - грудь, stomach - живот
import random
class Player():
    def glavniy_geroy():
        head, thorax, stomach = 35, 85, 70
        left_arm, right_arm = 60, 60
        left_leg, right_leg = 65, 65
        
        data = {
            "Name": None,
            "Firstname": None,
            "Age": None,
            "dop_data": None,
            "inventar": [],
            "Money":0,
            "head": head,
            "thorax": thorax,
            "stomach": stomach,
            "left arm": left_arm,
            "right arm": right_arm,
            "left leg": left_leg,
            "right leg": right_leg,
            "full_hp": head + thorax + stomach + left_arm + right_arm + left_leg + right_leg
        }
        return data
    
class Enemy(): 
    def bandit():
        head, thorax, stomach = 35, 85, 70
        left_arm, right_arm = 60, 60
        left_leg, right_leg = 65, 65
        
        data = {
            "Name": None,
            "Firstname": None,
            "Age": None,
            "dop_data": None,
            "inventar": [],
            "Money":random.randint(100, 500),
            "head": head,
            "thorax": thorax,
            "stomach": stomach,
            "left arm": left_arm,
            "right arm": right_arm,
            "left leg": left_leg,
            "right leg": right_leg,
            "full_hp": head + thorax + stomach + left_arm + right_arm + left_leg + right_leg
        }
        return data
    
class trader():
    @staticmethod
    def Jaba():
        data = {
            "Name": "Жаба",
            "Firstname": None,
            "Age":None,
            "dop_data": None,
            "inventar": [],
            "Money":random.randint(5000, 10000)
                }
        return data
            
    @staticmethod
    def random_hi():
        words_hi = ["Ну здарова, чего пришёл?", "Чё хотел?", "Тут недавно подвоз был. Хабар нужен?"]
        return random.choice(words_hi)

    @staticmethod        
    def random_goodbye():
        words_goodbye = ["Ну и пошёл на хер отседава!", "Давай, проваливай", "Я уж собирался тебя выгонять"]
        return random.choice(words_goodbye)
            