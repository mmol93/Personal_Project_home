def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.

    i = 1   # 카운터

    while i <= 3:
        new_guess_add = input("{}번째 숫자를 입력하세요: ".format(i))

        if int(new_guess_add) > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")

        elif i > 1 and int(new_guess_add) == new_guess[0]:
            print("중복되는 숫자입니다.")

        elif i > 2 and int(new_guess_add) == new_guess[0]:
            print("중복되는 숫자입니다.")

        elif i > 2 and int(new_guess_add) == new_guess[1]:
            print("중복되는 숫자입니다.")

        else:
            new_guess.append(int(new_guess_add))
            i += 1

    return new_guess

print(take_guess())