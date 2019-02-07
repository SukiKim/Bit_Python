
sum = 0

while(True):
    input_num = input("수를 입력하세요:")
    a = input_num.isdigit()
    if(a == True):
        input_num = int(input_num)
        for i in range(1, input_num+1):
           if(i % 3 == 0):
               sum += i
        print("1부터 ", input_num, "까지 3의 배수의 합 =", sum)
        break

    else:
        print("정수가 아님")
