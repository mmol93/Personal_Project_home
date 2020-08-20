def voca_en(word):
    with open("vocabulary.txt", 'a') as f:
        f.write(word + " : ")

def voca_kor(word):
    with open("vocabulary.txt", 'a') as f:
        f.write(word + "\n")

i = 1   # 카운터


while i >=1 :
    word_en = input("영어 단어를 입력하세요: ")
    if word_en == "q":
        exit()
    voca_en(word_en)

    word_kor = input("한국어 뜻을 입력하세요 : ")
    voca_kor(word_kor)

