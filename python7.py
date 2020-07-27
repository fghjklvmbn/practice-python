for waiting_no in range(1, 6):
    print("대기번호 : {}".format(waiting_no))

#starbucks = ["park", "kyeong", "haan"]
#for customer in starbucks:
#    print("{}, 커피 준비하였습니다.".format(customer))

#customer = "park"
#index = 1
#while True:
#    print("{}번째 손님 {}님 커피 나왔습니다.".format(index, customer))
#    index += 5

customer = "박경환"
index = 5
네 = True
아니요 = False
while index >= 1:
    print("{}, 커피준비 되었습니다. {}번쨰 남았습니다.".format(customer, index))
    index -= 1
    input("혹시 박경환 님이신가요?: ")
    if 네:
        print("커피 나왔습니다.")
    if index == 0:
        print("커피 폐기 처분 하겠습니다.")
person = "unknown"

while person != customer:
    print("{}님 커피나왔습니다.".format(customer))
    person = input("이름을 적으시오: ")