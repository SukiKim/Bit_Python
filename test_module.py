#모듈 임포트 : 모듈명을 이름공간

import math
import mymod

print(math.pi, mymod.pi)  #이름 공간이 다름

#모듈명 리네임
import math as m    #math 모듈을 m이름으로 사용
print(m.pi)

#모듈명 없이 사용하고자 할 때
from math import pi, sin, cos

print(pi * 10 ** 2)
print(sin.__module__)    #객체가 속한 모듈 확인
print(pi)   #math에 속한 pi

from mymod import pi
print(pi)   #같은 이름의 객체를 중복 임포트
            #나중에 임포트한 객체를 사용

from function_args import clean_strings, get_total3 as total
print(total([1, 2, 3, 4, 5]))

print(dir(math))
print("pi" in dir(math))

#import funcion_args