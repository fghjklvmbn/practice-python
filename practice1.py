#파이썬 연습용입니다. 간단한 함수들이나 코드가 적혀 있습니다.
#시간 추출기
import datetime
now = datetime.datetime.now()
a = int(now.hour)
b = int(now.minute)
c = int(now.second)
print("지금 {}시 {}분 {}초 입니다.".format(a,b,c))

sentense = 'park'
print(sentense)
sentense2 = '''park
kyeong
hwan'''
print(sentense2)

jumin = "100323-1208322"

print("성별: "+ jumin[7]) #숫자 문자열 찾기:[]
print("연: "+ jumin[0:2]) #0부터 2 직전 까지
print("월: "+ jumin[2:4])
print("일: "+ jumin[4:6])
print("뒷자리 7자리: "+ jumin[7:]) # 7번쨰 부터 끝까지
print("앞자리 6자리: "+ jumin[:6]) # 처음부터 6번째 까지
print('뒷자리 7자리: '+ jumin[-7:]) # 뒷자리 7자리 추출

#문자열 처리 함수
python = "Python Is Amazing"
print(python.lower()) #대문자로 변환해준다.
print(python.upper()) #소문자로 변환해준다.
print(python[0].isupper()) #python 변수에서 []안에 있는 숫자 순서에 대문자가 있는지 확인 하는 함수이다.
print(len(python)) #글자수를 세준다.
print(python.replace("Python","java")) #python 변수에 있는 단어를 replace 함수에서 (a를 ,b로)바꾼다는 함수이다.

index = python.index("n") #문자만 사용가능, python 변수에서 "n"이란 단어가 몇번째에 있는지 찾는다.(숫자로 알려준다.)
print(index)

index = python.index('n', index + 1) #python 변수에서 "n"이란 2번째로 사용된 단어가 몇번째에 있는지 찾는다.(숫자로 알려준다.)
print(index)

print(python.find("java")) #python 변수에서 "java"이란 단어를 찾는다. 있으면 0 없으면 -1값으로 반환된다. index로 바꾸고 실행하면, 프로그램 오류를 내고 강제로 종료된다.

'''ex)
print(python.index("java"))
print("hi")
이러면, value관련 오류가 난다.'''
print(python.find("java"))
print("hi") #오류 없이 -1이 출력되어지고, 다음 명령어도 잘 실행된다.

print(python.count("n")) # 문자열 전체중에서 "n"의 문자의 갯수를 센다.


#https://naver.com 과제
url = "https://naver.com"
my_str = url.replace("https://", "")#앞부분 없애기
my_str = my_str[:my_str.index(".")]
# naver
a = str(len(my_str))
my_str = str(my_str[0:3])# nav
b = str(len("e"))
print(my_str + a + b + "!")


url = "https://google.com"
my_str = url.replace("https://", "")
url = my_str[:my_str.index(".")]
#naver
#print(url)
a = len(url)
url1 = url[:3]
b = my_str.count("e")
a = str(a)
b = str(b)
password = url1 + a + b + "!"
print("이 사이트({})의 비밀번호는 {} 입니다.".format(url, password))

subway = [10,20,30]

subway.append(10)
subway.append("박경환")
subway.insert(1, "경환박")

#print(subway)

subway.append("park")
print(subway.pop())
print(subway)
 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
#num_list.clear()
#print(num_list)

mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[100])#실행 종료

print(cabinet.get(5, "사용가능"))#키가 없음을 인지하고 다음으로 넘김
print("hi")

print(3 in cabinet)#true
print(5 in cabinet)#false

cabinet2 = {"p-12" : "박", "k-13" : "경"}
print(cabinet2)
cabinet2["p-12"] = "asdfads"
cabinet2["k-13"] = "asdf"
print(cabinet2)

del cabinet2["p-12"]

print(cabinet2.keys())

print(cabinet2.values())

cabinet2.clear()
print(cabinet2)

#튜플
menu1 = ("돈가스", "치즈가스")
print(menu1[0])
print(menu1[1])
#menu1.add("생선가스")

name = "박경환"
age = 20
hobby = "코딩"

print(name, age, hobby)





















