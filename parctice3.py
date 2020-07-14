'''name = "park"
attack1 = 102
hp = 1092

print("{0}이  생성되었습니다.".format(name))
print("{0}는 체력이 {1} 이고, 공격력은 {2}입니다.".format(name, hp, attack1))

tank_name = "tank"
tank_hp = 982
tank_attack = 300

print("{0}가 생성되었습니다.".format(tank_name))
print("{0}는 체력이 {1}이고, 공격력은 {2}입니다.".format(tank_name, tank_hp, tank_attack))

tank1_name = "tank1"
tank1_hp = 982
tank1_attack = 300

print("{0}가 생성되었습니다.".format(tank1_name))
print("{0}는 체력이 {1}이고, 공격력은 {2}입니다.".format(tank1_name, tank1_hp, tank1_attack))

def attack(name, location, damage):
    print("{0}: {1}방향으로 적군을 공격합니다. (공격력은 {2})".format(name, location, damage))
attack(name, "1시", attack1)
attack(tank_name, "1시", tank_attack) 
attack(tank1_name, "1시", tank1_attack)'''

class unit:
    def __init__(self, name, hp, damage):
        self.name= name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

unit1 = unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(unit1.name, unit1.damage))

unit2 = unit("레이스2", 90, 43)

unit2.clocking = True
unit1.clocking = True

if unit1.clocking == True:
    print("{}와 {}는 강제로 마인드 컨트롤 당했습니다.".format(unit1.name, unit2.name))

