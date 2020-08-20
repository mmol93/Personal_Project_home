# 마린 : 공격유닛

name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다".format(name))
print("체력{}, 공격력 {} \n".format(hp, damage))


# 탱크 : 공격 유닛, 일반 모드 / 시즈 모드

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다".format(tank_name))
print("체력{}, 공격력 {} \n".format(tank_hp, tank_damage))

tank_name2 = "탱크2"
tank_hp2 = 150
tank_damage2 = 35

print("{} 유닛이 생성되었습니다".format(tank_name2))
print("체력{}, 공격력 {} \n".format(tank_hp, tank_damage2))

def attack(name, location, damage):
    print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]"
          .format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank_name2, "1시", tank_damage2)