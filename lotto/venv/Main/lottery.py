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

def count_maching_numbers(list1, list2):    # 2개의 리스트 항목에서 겹치는 항목 몇갠지 카운트

    # list1 : 6개의 항목 / list2 : 7개의 항목(보너스 번호 1개를 추가로 갖고 있기 때문)

    i = 0   # 횟수 카운터1
    j = 0   # 횟수 카운터2
    k = 0   # 일치 확인 카운터
    z = 0   # 보너스 번호 일치 확인


    while 6 > i:    # list1 기준이므로 6번 반복
        while 7 > j:    # list2 기준이므로 7번 반복
            if list1[i] == list2[j]:
                if j == 6 and list1[i] == list2[j]:
                    z += 1
                k += 1
            j += 1
        j = 0
        i += 1

    return k, z

def check(list1, list2):
    answer = count_maching_numbers(list1, list2)

    if answer[0] == 6 and answer[1] == 0:
        return 1000000000
    elif answer[0] == 6 and answer[1] == 1:
        return 50000000
    elif answer[0] == 5 and answer[1] == 0:
        return 1000000
    elif answer[0] == 4:
        return 50000
    elif answer[0] == 3:
        return 5000
    else:
        return 0


