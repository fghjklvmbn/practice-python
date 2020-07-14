import datetime
now = datetime.datetime.now()
print(now.hour, now.minute, now.second)

print("나는 %d살입니다." % 20) # %d는 정수값이다.
print("나는 %s을 좋아해요" % "파이썬") # %s는 정수나 문자를 출력 해낼수 있다. 
print("Apple은 %c로 시작합니다." % "A") 
print("나는 %s색과 %s색을 좋아해요" %("파란", "노란")) # %s는 중복해서 쓰일수 있다. 

print("나는 {}살 입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "노란"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "노란"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "노란"))


print("나는 {a}살 이고, {b}을 좋아합니다.".format(a = 10, b = "빨간색"))
print("나는 {a}살 이고, {b}을 좋아합니다.".format(b = "빨간색", a = 20))
print("나는 {a}살 이고, {b}을 좋아합니다.".format(a = 10, b = "빨간색"))

#3.6이상만
age = 19
color = "빨간색"
print(f"나는 {age}살이며, {color}색을 좋아해요")
print("ㄹㅇ너ㅣㅏ렁니\nㅏㅓㄹㄴ아ㅣㄹ") 
print('저는 "나도코딩" 입니다.')
print()
print("저는 \"나도코딩\" 입니다.")
print("D:\\srv\dev-disk-by-label-nas\ssd\코딩 연습>")
# \r :커서 맨앞으로 이동
print("red apple \rpine")
# \b : 백스페이스(한글자 삭제)
print("red d\bapple")
# \t : 텝키 대신 사용
print("pe\tpper")

#복습
url = "https://naver.com"
url1 = url.replace("https://", "") #https://를 없앰
url1 = url1[:url1.index(".")]
a = len(url1)
a = str(a)
b = len("e")
b = str(b)
url1 = url1[0:3] #nav 표시
print(url1 + a + b + "!")
