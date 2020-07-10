print(5)
print(-29)
print(3.14)
print(20000)
print(5+8)
print(3*8)
print(3*(3+2))
#문자열
print("풍선")
print('나비')
print('?')
#boolean
print(4 > 10)
print(4 < 10)
print(True)
print(False)
print(not True)
print(not (5 > 20))
#변수 입력
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
#출력
'''주석처리
여러줄 가능'''
print("우리집 개 이름은 " + name + "입니다.")
print("우리집 개의 나이는 " + str(age) + "세 입니다." )
print("우리집 개는 어른인가요? " + str(is_adult))

station_1 = "사당"
station_2 = "신도림"
station_3 = "인천공항"

print(station_1 + ', ' + station_2 + ', ' + station_3 + '행 열차가 들어오고 있습니다')

a = input("숫자를 적어주세요: ")
a = int(a)
#읍읍
if a < 5:
    print("조금 작군요")
if 5 <= a < 15:
    print("보통")
if 15 <= a:
    print("오오 크군요")

print(4%2) #나누기
print(10**2) #제곱
print(10 // 4) #몫

print(1 != 2) #true
print(not(1 != 3)) #false
print((10<100) or (10 != 100))

#자동 계산기(덧셈,뺄셈,곱셈등)
number = input("숫자를 입력해주세요: ")
number = int(number)
print(number)
number += 103
print(number)
number -=10
print(number)
number /= 3
print(number)
number *= 12
print(number)
number %= 3
print(number)

print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 2))
print(round(3.14)) #반올림
print(round(4.99)) #반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근 

from random import *

print(random()) #0.0~1.0 미만의 임의의 값을 생성
print(random() * 10) #0부터 10까지의 임의의 값을 생성
print(int(random() * 10)) #0부터 10까지의 소수점 없는 임의의 값을 생성
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10 ) + 1) # 1부터 10까지의 소수점 없는 임의의 값을 생성
print(int(random() * 10 ) + 1)
print(int(random() * 10 ) + 1)

print(randrange(1, 46)) #1부터 45까지의 소수점 없는 임의의 값을 생성
print(randrange(1, 46)) #1부터 45까지의 소수점 없는 임의의 값을 생성
print(randrange(1, 46)) #1부터 45까지의 소수점 없는 임의의 값을 생성
print(randrange(1, 46)) #1부터 45까지의 소수점 없는 임의의 값을 생성
print(randrange(1, 46)) #1부터 45까지의 소수점 없는 임의의 값을 생성

print(randint(1,34)) #1부터 34이하의 소수점 없는 임의의 값을 생성
print(randint(1,34)) #1부터 34이하의 소수점 없는 임의의 값을 생성
print(randint(1,34)) #1부터 34이하의 소수점 없는 임의의 값을 생성
print(randint(1,34)) #1부터 34이하의 소수점 없는 임의의 값을 생성
print(randint(1,34)) #1부터 34이하의 소수점 없는 임의의 값을 생성
print(randint(1,34)) #1부터 34이하의 소수점 없는 임의의 값을 생성

a = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 {}일로 선정되었습니다.".format(a))