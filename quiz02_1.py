score1 = int(input("첫번째를 입력해주세요"))
score2 = int(input("두번째를 입력해주세요"))

if score1 >= 50 and score2 >= 50:
    if (score1+score2)/2 >= 60:
        print("합격")
    else:
        print("평균불합격")
else:
    print("각 점수 불합격")