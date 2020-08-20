from random import randint


def generate_numbers(): # 0~9 사이의 랜덤 숫자 3개 뽑음
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = []
    i = 1   # 카운터

    while i <= 3:
        numbers.append(randint(0,9))
        i += 1
    # 코드를 작성하세요.

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.

    i = 1   # 카운터

    while i <= 3:
        new_guess_add = input("{}번째 숫자를 입력하세요: ".format(i))

        if new_guess_add == "":
            print("아무것도 입력하지 않았습니다 다시 입력하세요")

        elif i > 1 and int(new_guess_add) == new_guess[0]:
            print("중복되는 숫자입니다.")

        elif i > 2 and int(new_guess_add) == new_guess[0]:
            print("중복되는 숫자입니다.")

        elif i > 2 and int(new_guess_add) == new_guess[1]:
            print("중복되는 숫자입니다.")

        elif int(new_guess_add) > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")

        else:
            new_guess.append(int(new_guess_add))
            i += 1

    return new_guess

def get_score(guess, solution):
    strike_count = 0    # 스크라이크 갯수
    ball_count = 0      # 볼 갯수
    i = 0   # 카운터1
    j = 0   # 카운터2
    # 코드를 작성하세요.

    while i < 3:
        while j < 3:
            if guess[i] == solution[j] and i == j:
                strike_count += 1
            elif guess[i] == solution[j]:
                ball_count += 1
            j += 1
        j = 0
        i += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
i = 0   # 마침표


# 코드를 작성하세요.
while i == 0:
    seleted_answer = take_guess()
    score = get_score(seleted_answer, ANSWER)  # 랜덤 숫자 3개와 입력 숫자 3개를 비교
    tries += 1

    print("{}S {}B".format(score[0],score[1]))

    if score[0] == 3:
        i = 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
