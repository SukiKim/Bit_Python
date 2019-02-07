def quiz1():
    str = "Life is too short, You need Python" #주어진 문자열
    str = str.lower() #모두 소문자
    str = str.replace(" ","") # 공백 제거
    str = str.replace(",", "") # 콤마 제거
    lst = list(str) #리스트 형변환

    chars = set(lst)    #set으로 형변환하여 chars변수에 담기
    print(chars)    #화면에 출력
    lst_type = list(chars)  #list로 형변환
    lst_type.sort() #정렬

    print(len(lst_type)) # 길이 출력

quiz1()