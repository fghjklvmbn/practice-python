cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"a-3":"유재석", "b-100":"김태호"}
print(cabinet["a-3"])
print(cabinet["b-100"])

print(cabinet)
cabinet["a-3"] = "김종국"
cabinet["b-100"] = "조세호"
print(cabinet)
# a-3 삭제
del cabinet["a-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)


