#튜플(소괄호)
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

#값 추가 불가능

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)

#집합(중복 안됩, 순서 없음)
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

print(java & python)

java.remove("김태호")
print(java & python)