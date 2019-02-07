def define_list():
    """
    리스트 정의 연습
    """
    lst1 = list()   # 타입 객체를 이용한 생성
    print(lst1, type(lst1))
    lst2 = [] #리스트 리터럴로 생성 : 일반적
    lst3 = [1, 2, "Python"]
    lst4 = list("Python")#다른 시퀀스 객체를 리스트에 넣기
    lst5 = "I like Python Programming".split()

    print("lst4:", lst4)
    print("lst5:", lst5)

def list_oper():
    """
    리스트 연산
    """
    lst = [1, 2, "Python"]

    #길이 확인
    print(lst, "Length:", len(lst))

    #인덱싱
    print("indexing:", lst[0], lst[1], lst[2])  #정방향 인덱스
    print("rindexing:", lst[-3], lst[-2], lst[-1])#역방향 인덱스
    
    # 슬라이싱
    print(lst[1:3])
    print(lst[:2])  #처음부터
    print(lst[2:])  #끝까지
    print(lst[:])   #전체

    #슬라이싱을 이용한 리스트의 복제
    lst_copy = lst[:]   #새 리스트로 복제
    print("COPY:", lst_copy)

    # append vs extends
    lst_copy.append(["Java", True, 3.14159])
    print(lst_copy)
    lst_copy.extend(["Java", True, 3.14159])
    print(lst_copy)

    #insert
    lst_copy.insert(2, [1, 2, 3])
    print(lst_copy)

    #포함 여부 확인 : in, not in
    print("Python" in lst_copy)
    #항목값을 이용한 인덱스 값 확인
    print(lst_copy.index("Python"))
    # 항목 개수 출력
    print("count:", lst_copy.count("Python"))
    #삭제 : 인덱스를 이용한 삭제
    del lst_copy[2]
    print(lst_copy)
    #삭제 : 객체 값을 이용한 삭제
    print(lst_copy)

    #슬라이싱 활용
    print("--------슬라이싱")
    lst2 = [1, 12, 123, 1234, 12345]
    print("lst2: ", lst2)

    #슬라이싱을 이용한 치환
    lst2[0:2] = [10, 20]
    print(lst2)
    lst2[0:2] = [10]
    lst2[1:2] = [20]
    lst2[2:] = [30]

    print(lst2)

    #슬라이싱을 이용한 삭제
    lst2 = [1, 12, 123, 1234, 12345]
    print("lst2 : ", lst2)
    lst2[1:2] = [] #슬라이스 부분을 빈 배열로 -> 삭제
    print(lst2)


    #슬라이싱을 이용한 삽입
    lst2[1:1] = ['CHUNK']
    print(lst2)
    #가장 앞쪽에 삽입
    lst2[:0] = ["HEAD"]
    print(lst2)
    #가장 뒤쪽에 삽입
    lst2[len(lst2):] = ["TAIL"]
    print(lst2)


    lst2[2] = [9, 8, 7]
    print(lst2)
    lst2[2:2] = [9, 8, 7]
    print(lst2)

def list_methods():
    list = [10, 2, 22, 9, 8, 33, 4, 12]
    print("Original list: ", list)
    list.reverse()
    print("reverse:", list)

    list_copy = list.copy()
    print("Original copy", list_copy)

    # SORT 정렬
    list_copy.sort()
    print("Sort list_copy", list_copy)
    list_copy.sort(reverse = True)
    print("desc list_copy:", list_copy)
    list_copy.sort(key = int)
    print("int key sort:", list_copy)
    list_copy.sort(key = str)
    print("str key sort:", list_copy)

    #정렬을 위한 키값 함수
    def key_func(val):
        return val % 10

    list_copy.sort(key = key_func)
    print("custom sort:" , list_copy)

    #sort 메소드와 sorted 내장 함수
    list_copy = list.copy()

    print("list원본 : ", list)
    list.sort()
    print("list sort: ", list)

    print("list_copy 원본", list_copy)
    print("sorted list_copy", sorted(list_copy))
    print("list_copy:", list_copy)

def loop():
    words = "Life is too short, You need Python".spilt()
    print(words, type(words))

    for word in words:
        print(word)

def stack_ex():
    stack = [] # 빈 리스트

    #데이터의 입력
    stack.append(10)
    stack.append(20)
    stack.append(30)

    print("Stack:", stack)
    print(stack.pop(), stack)
    print(stack.pop(), stack)
    print(stack.pop(), stack)


def queue_ex():
    queue = []

    #데이터의 입력
    queue.append(10)
    queue.append(20)
    queue.append(30)

    print("Queue:", queue)
    print(queue.pop(0), queue)
    print(queue.pop(0), queue)
    print(queue.pop(0), queue)

#define_list()
#list_oper()
#list_methods()
#loop()
#stack_ex()
queue_ex()