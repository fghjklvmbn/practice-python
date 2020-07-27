subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

subway.append("유재석")
print(subway.count("유재석"))

num_list = [5,4,3,2,1]

num_list.reverse()
print(num_list)

num_list.extend(subway)
print(num_list)


