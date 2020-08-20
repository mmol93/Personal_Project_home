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


# 테스트
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
