# 문자열 연습
def define_str():
    """이 함수는 문자열 정의에 대한 도움말 문자열입니다
    """


    # 한 줄 문자열의 정의
    s1 = "Hello Python" # 직접 리터럴
    s2 = str('Hello Python')
    s3 = str(3.14159)

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    print(s1, "is str instance?", isinstance(s1, str))

    #여러 줄 문자열
    s4 = """Life is too short, you need Pyhton.
    여러 줄 문자열
    여러 줄 문자열은 함수 docstring으로도 활용
    여러 줄 문자열은 여러 줄 주석으로도 활용
    """

    print(s4)
def string_oper():
    """문자열 연습
    """
    print("======문자열 연산 연습 함수")
    s = "Life is too short, You need Python!"

    #시퀀스형의 길이
    print("str length : ", len(s))
    #인덱스를 이용한 접근
    print(s[0], s[1], s[2], s[3]) #정방향 인덱스
    print(s[-7], s[-6], s[-5]) #역인덱스

    #문자열은 immutable(변경 불가) 자료형
    #str[0] = "L"   # -> 내부 자료 변경 불가

    #슬라이싱
    print(s[12:17])
    print(s[-7:-1])
    print(s[:17]) #처음부터 슬라이싱
    print(s[:]) #모두 생략하면 시퀀스 전체


    #연결(+)
    print("Python" + " " + "Programming")
    print("Python" + str(3))

    #반복(*)
    print("Python" * 3)

    # 포함 여부 : in, not in
    print("P" in s)
    print("P" not in s)



#define_str()
string_oper()