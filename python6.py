'''weather = input("오늘날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("미스크를 챙기세요")
else:
    print("준비물을 필요 없어요")'''

temp= int(input("기온은 어때요? "))
if 30 <= temp:
    print("덥습니다")
elif 20 <= 30:
    print("활동 나가기 좋은 온도입니다.")
elif 0 <= 19:
    print("외투를 챙 기세요")
else:
    print("춥습니다.")
    
temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp <= 30:
    print("나가기 좋은 날씨에요")
elif 0 <= temp and temp < 10:
    print("조금 추워요")
else:
    print("추워요")
        
