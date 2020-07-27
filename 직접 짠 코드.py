#커피 나왔습니다
import sys #sys를 임포트하여 아래의 sys.exit() 함수를 작동시키게 합니다.
customer = "박경환"
index = 5
person = "unknown"
while index >= 1:
    print("{}, 커피준비 되었습니다. {}번쨰 남았습니다.".format(customer, index))
    index -= 1
    person = input("성명을 적어주십시오: ")
    if person == customer:
        print("커피 나왔습니다.")
        sys.exit()
    else:
        print("{} 님이 아닙니다.".format(person))
    if index == 0:
        print("커피를 폐기처분 하겠습니다.")