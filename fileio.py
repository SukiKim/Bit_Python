def create_home():
    dir = "D:\\Python_Study\\samples"

    import os   #
    if not os.path.exists(dir):
        os.makedirs(dir)    #디렉토리 생성
    else:
        print("이미 있습니다.")


def write_text():

    # f = open("D:\\Python_Study\\samples\\test.txt", "wt")  #t는 생략 가능
    # size = f.write("Life is too short, You need Python")
    # print("written size :", size)
    # f.close()

    f = open("D:\\Python_Study\\samples\\multilines.txt", "wt", encoding="utf-8")  # t는 생략 가능
    for i in range(100):
        f.write("Line %d\n" % i)
    f.close()


def read_txt():
    # f = open("D:\\Python_Study\\samples\\multilines.txt", "r", encoding="utf-8")  #t는 생략 가능
    # text = f.read()
    # print(text)
    # f.close()

    # 줄 단위로 불러오기
    f = open("D:\\Python_Study\\samples\\multilines.txt", "r", encoding="utf-8")  # t는 생략 가능


    while True:
        line = f.readline()
        if not line:
            break
        print(line)

    f.close()

    #편의 내용을 불러와서 자동으로 줄단위 리스트로 변환
    # readlines

    f = open("D:\\Python_Study\\samples\\multilines.txt", "r", encoding="utf-8")  # t는 생략 가능
    lines = f.readlines()
    #print(lines)
    for line in lines:
        print(line.strip())
    f.close()


def practice():     #응용
    """
    sangbuk.csv로 부터 내용을 읽어와서 각 선수별 사전을 딕셔너리에 담기
        """
    f = open("D:\\Python_Study\\samples\\sangbuk.csv", "r", encoding="utf-8")  # t는 생략 가능
    members = []     #빈 리스트
    while True:
        line = f.readline()
        if not line:
            break
        #print(line)
        line = line.strip().replace(" ", "")
        info = line.split(",") #문자열 -> 배열
        member = {"name": info[0],
                  "number": info[1],
                  "height": info[2],
                  "position": info[3]}
        members.append(member)
        print(member)
    print(members)


    f.close()



def binary_copy():
    """
    이진파일을 열어서 다른 이름으로 복사
    """
    f = open("D:\\Python_Study\\samples\\rose-flower.jpeg", "rb") #이진파일이라 b를 붙혀야 한다
    data = f.read()
    f.close()

    f_dest = open("D:\\Python_Study\\samples\\rose-flower-copy.jpeg", "wb")
    f_dest.write(data)
    f_dest.close()

def using_with():
    with open("D:\\Python_Study\\samples\\multilines.txt") as f:
        for line in f.readlines():
            print(line.strip())

        print("is file close?", f.closed)  #파일이 자동으로 닫혔는지 확인


def using_pickle():
    f_name = "D:\\Python_Study\\samples\\players.bin"
    data = {"baseball" : 9}

    import pickle
    #data를 피클로 저장해 봅시다
    with open(f_name, "wb") as f:
        pickle.dump(data, f)
        pickle.dump({"soccer":11}, f, 2)    #프로토콜 버전 지정 : 2
        pickle.dump({"basketball":5}, f, pickle.HIGHEST_PROTOCOL)
    #피클 데이터 불러오기
    with open(f_name, "rb") as f:
        #print(pickle.load(f))
        #print(pickle.load(f))
        #print(pickle.load(f))   #불러올 때는 프로토콜 버전 필요 없음
        #print(pickle.load(f))

        result = []
        while True:
            try:
                data = pickle.load(f)
                result.append(data)
            except EOFError:
                #더이상 불러올 데이타거 없는 경우
                break
        print(result)
#create_home()
#write_text()
#read_txt()
#practice()
#binary_copy()
#using_with()
using_pickle()