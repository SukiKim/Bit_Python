#함수 인자값 예제
def sum_val(a, b):  #인자값의 개수는 제한 없음
    return a + b

if __name__=="__name__":
    print(sum_val(10, 20))

#기본 값이 있는 인자
def increase(a, step = 1):  #step의 기본 값은 1
    return a + step

print(increase(10)) #step값은 기본값을 사용
print(increase(10, 2))   #기본값 무시 직접 값 할당

#키워드 인수 : 인수값을 이름으로 전달 할 수 있다.
def area(width, height):
    return width * height

print(area(10, 12)) # 지정된 인자의 순서대로 값 전달
print(area(height = 12, width = 10)) #키워드로 인수를 전달할 수 있다
print(area(height = 12, width = 10) == area(10, 12) )

#가변 인자 : 정해지지 않은 수의 인수를 전달 "*"
def get_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(get_total(1,3,5,7,9))



"""
넘어온 가변 인자를 확인해서
int, float면 합산
list, tuple 이면 안쪽을 2차 루프 int, float면 합산
나머지는 합산해서 배제
"""





def get_total2(*args):
    total = 0
    for x in args:
        if isinstance(x, (int, float)):
            total += x
        elif isinstance(x, (list,tuple)):
            for item in x:
                if isinstance(item, (int, float)):
                    total += item
    return total



print(get_total2(1, 3, 5, 7, 9))
print(get_total2(1, [3, 5, 7], 9))
print(get_total2(1, [3, 5, 7],  "string", 9))



"""
가변 인수 뒤에 
사전인자 restrict = True    :합산할 수 없는 값이 포함되면 None반환
"""



def get_total3(*args, **kwargs): #kwargs는 사전인자
    restrict = True if kwargs.get("restrict") == True else False
    print("restrict", restrict)
    total = 0
    for x in args:
        if isinstance(x, (int, float)):
            total += x
        elif isinstance(x, (list,tuple)):
            for item in x:
                if isinstance(item, (int, float)):
                    total += item

                elif restrict:  # ->
                    return None
        elif restrict:  # ->
            return None
    return total



print(get_total3(1, 3, 5, 7, 9))
print(get_total3(1, [3, 5, 7], 9))
print(get_total3(1, [3, 5, 7],  "string", 9))



#함수도 객체 : 심볼 할당 가능, 함수의 인자로 전달 가능
# 외부로 내부 함수를 보낼 수 있습니다 -> Functional Programming

dirty_string = "python pRoGRAMming,"\
    "jAVA pRoGRAMming, LINUX, wINDows".split(",")   #    1. split, 2. 각 단어의 첫글자만 대문자
print(dirty_string)
def clean_strings(strings, *funcs):# func : 가변 인수
    results = []
    for string in strings:
        for func in funcs:
            if callable(func):  #func가 호출 가능 객체인가
                string = func(string)

        results.append(string)
    return results

cleaned_strings = clean_strings(dirty_string, str.strip, str.title)
print(cleaned_strings)
print(__name__)

#print(clean_strings)
