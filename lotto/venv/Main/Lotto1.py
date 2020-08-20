import random

def generate_numbers(chance):   # 지정한 횟수만큼 랜덤 숫자 생성
    i = 0   # 카운터
    list_chance = []

    while chance > i:
        list_chance.append(random.randint(1, 45))
        i += 1

    return list_chance

def draw_winning_numbers():     # 7개의 당첨번호 생성(6개 + 1개(보너스))
    target_6 = sorted(generate_numbers(6))
    bonus = random.randint(1,45)

    target_7 = target_6.append(bonus)

    return target_6

print(draw_winning_numbers())