import random

dict_en = {}    # 사전의 초기화
list_en = []    # 영어 단어 리스트의 초기화
list_kor = []   # 한글 단어 리스트의 초기화
i = 0   # 카운터

with open("vocabulary.txt", 'r') as f:
    for line in f:
        dict_en[line.split()[0]] = line.split()[2]
        # line.split()[0] : 영단어 부분(사전의 인덱스)
        # line.split()[2] : 한글단어 부분(사전의 값)

        list_en.append(line.split()[0])     # 영어 단어 부분 리스트
        list_kor.append(line.split()[2])    # 한글 단어 부분 리스트

    while i >= 0:

        random_num = random.randint(0, len(dict_en) - 1)     # 랜덤숫자 생성(0 ~ 사전 인덱스 갯수 -1)
        answer = input(list_kor[random_num] + ": ")

        if answer == "q":
            exit()
        elif answer == list_en[random_num]:
            print("맞았습니다!")
        else:
            print("틀렸습니다. 정답은 {}입니다".format(list_en[random_num]))
