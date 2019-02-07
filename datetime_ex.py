# datetime 예제
import datetime
#datetime, date, time,timedelta

#현재 시간을 얻어오기
now = datetime.datetime.now()
print(now)

past = datetime.datetime(1999, 12, 31)
print(past)

#dt = datetime(1999, 12, 32) #-> 없는 날짜

print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
#datetime의 메소드들
print("요일 :", now.weekday()) #요일 월(0) ~ 일(6)

now_date = now.date()
print(now_date, type(now_date))
now_time = now.time()
print(now_time, type(now_time))

#날짜는 비교가 가능
print(now > past)

#날짜의 차이도 얻을수도 있습니다
datediff = now - past
print(datediff, type(datediff))

#timedelta의속성
print(datediff.days,datediff.seconds, datediff.microseconds)
print(datediff.total_seconds())

#datetime과 timedelta를 합산 새 시간을 만들어 낼 수 있음
diff = datetime.timedelta(days = 365) #시간차 365일
print("365일후 :", now+diff)

import locale
locale.setlocale(locale.LC_ALL,'ko_KR.UTF-8')
#datetime 포매팅
print(now.strftime("%Y/%m%d %H:%M"
                   ))
print(now.strftime("%Y년 %m월 %d일 %H시 %M분"))

#문자열로된 날짜 정보가 있을 경우 : strptime
str = "2019-12-24 23:59"
dt = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M")
print(dt, type(dt))