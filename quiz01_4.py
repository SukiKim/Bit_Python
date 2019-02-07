def quiz01_4():
    lst_date = ["2018.01.02", "2018.01.03", "2018.01.04", "2018.01.05"]
    lst_dow = ["화", "수", "목", "금"]
    lst_price = [2479.65, 2486.35, 2466.46, 2497.52]


    kospi_price = dict()

    #딕셔너리 K, V 설정
    kospi = {"dow": lst_dow[0], "price":lst_price[0]} #2018년 1월 2일
    kosp= {"dow": lst_dow[1], "price": lst_price[1]} #2018년 1월 3일
    kos = {"dow": lst_dow[2], "price": lst_price[2]} #2018년 1월 4일
    ko = {"dow": lst_dow[3], "price": lst_price[3]} #2018년 1월 5일


    ##이중 딕셔너리 K, V 설정
    kospi_price = {
        lst_date[0]: kospi,        lst_date[1]: kosp,        lst_date[2]: kos,        lst_date[3]: ko}


    # 전날과 현재날 차이 값 K, V 삽입
    kosp["price_diff"] = kospi["price"]-kosp["price"] #2018년 1월 3일기준으로 전 날과의 차이를
    kos["price_diff"] = kosp["price"] - kos["price"] #2018년 1월 4일기준으로 전 날과의 차이를
    ko["price_diff"] = kos["price"] - ko["price"] #2018년 1월 5일기준으로 전 날과의 차이를
    print(kospi_price)

    #파이썬에 내장되어있는 max와 min함수를 쓰기 위해 사용할 값들을 튜플 형식으로 지정
    a = [kospi_price[lst_date[0]]["price"], kospi_price[lst_date[1]]["price"], kospi_price[lst_date[2]]["price"], kospi_price[lst_date[3]]["price"]]


    print("max = ", max(a))
    print("min = ", min(a))


quiz01_4()