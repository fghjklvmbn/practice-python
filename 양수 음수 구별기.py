number = input("숫자를 입력하십시오: ")
number = int(number)

if number < 0:
    print("음수입니다.")
if number > 0:
    print("양수입니다.")
if number == 0:
    print("음수도 양수도 아닌 0 입니다.")