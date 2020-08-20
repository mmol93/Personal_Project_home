gun = 10

def checkpoint(solders):
    global gun
    gun = gun - solders
    print("남은 총 : {}".format(gun))

checkpoint(2)