# thorax - грудь, stomach - живот
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