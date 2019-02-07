def sys_module():
    """
    sys모듈 : 파이썬 인터프리터 관련
    """
    import sys
    print(sys.platform) #플랫폼 정보 열기
    print(sys.version)  # 파이썬 버전 정보

    print(sys.path, type(sys.path))#파이썬 모듈 검색 디엑토리
    # import 할때 모듈 위치 검색
    #모듈 검색 디렉토리를 추가
    sys.path.append("D:\\Python_Study")# 모듈 임포트시 디렉터리 안쪽

def math_module():
    import math
    print(math.pi, math.e)

    #알고 갑시다 : round(반올림), trunc(버림)
    print(round(3.56, math.trunc(3.56)))
    print(round(3.56789,2)) #소수점 특정 자리까지 반올림해서 표시


def re_module():
    import re
    namecards = """
    
Email: comnat12@naver.com
Phone:010-0000-0000

Email:something@naver.com
Phone:000-1234-5678
"""

    email_pattern = r"\w+[\w\.]*@\w+[\w\.\].[a-z]+"

    email_list = re.findall(email_pattern, namecards)
    print(email_list, type(email_list))

    phone_pattern = r"[0-9]{3}-[0-9}{4}-[0-9]{4}"
    phone_list = re.findall(phone_pattern, namecards)
    print(phone_list, type(phone_list))


def random_module():
    import random
    print(random.random)    # 0 ~ 1 사이에 실수 난수
    print(random.randint(1, 6)) # 1 ~ 6 사이의 정수 난수

    print(random.randrange(100)) #인자 1개면 끝값만 정의
    print(random.randrange(1, 100, 3)) #1부터 100사이에 step 3인 수

    seqvar = ["짬뽕", "짜장면", "짬짜면"]
    random.shuffle(seqvar)
    print(seqvar)

    print(random.choice(seqvar))    #임의로 한개 객체 뽑기

    #표본 추출 함수
    print(random.sample(range(1, 101), 10))


#sys_module()

#math_module()
#re_module()
random_module()