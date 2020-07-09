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

