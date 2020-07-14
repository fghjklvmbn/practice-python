from random import randint
a = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 {}일로 선정되었습니다.".format(a))
'''랜덤 함수를 끌어와야 비로소 randint나 randrange등
random 관련한 모든 기능이 작동한다.'''

#과제 + 나의 생각
url = "https://naver.com"
asdf = url.replace("https://", "")
# print(asdf)
asdf = asdf[:asdf.index(".")]
a = str(len(asdf))
asdf = asdf[0:3]
b = str(len("e"))
print( asdf + a + b + "!")

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["park", "kyeong", "hwan"]
print(subway)

subway.append(123)
print(subway)

subway.insert(0, "hwan") # 끼어넣기
print(subway)
#뒤부터 없앰
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)