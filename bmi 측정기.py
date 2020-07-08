#키, 몸무게 정보수집
old = input("나이가 몇세이신가요?: ")
height = input("키가 몇m 인가요?(소수점으로 적으시기 바랍니다.): ")
weight = input("몸무게는 몇kg 이신가요?: ")
old = int(old)
height = float(height)
weight = int(weight)
#bmi 공식 대입
bmi =  int(weight) / (float(height)*float(height)) 

print("당신의 bmi는 {}입니다.".format(bmi))
print("당신의 나이는 {}세입니다.".format(old))
print("프로그램이 종료되었습니다. \n향후 업데이트 시 나이별 bmi를 업데이트 할 예정이니, 기다려주세요!")