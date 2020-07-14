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
    def __init__(self, name, hp, speed):
        self.name= name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{}: {} 방향으로 이동합니다.[속도 {}]".format(\
            self.name, location, self.speed))
        

#데미지와 체력 관련 코드(공격유닛)
class attackunit(unit):
    def __init__(self, name, hp, damage, speed):
        unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{}을 {} 방향으로 적을 공격합니다.".format(\
            self.name, location))
         
    def damaged(self, damage):
        print("{}: {}데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("남은 hp가 {}입니다.".format(self.hp))
        if self.hp <= 0:
            print("{}이 파괴되었습니다.".format(self.name))
#날수 있는 기능을 가진 클래스
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{} : {} 방향으로 날아가고 있습니다. [속도 {}]".\
            format(name, location, self.flying_speed))

class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, 0, damage)
        flyable.__init__(self, flying_speed)
    def move(self, location):
        print("{공중유닛 이동}")
        self.fly(self.name, location)

class buildingunit:
    def __init__(self, name, hp, location ):
        pass

supply_depot = buildingunit("서플라이 디폿", 500, "7시")

def game_start():
    print("게임을 시작하겠습니다.")

def game_over():
    pass

game_start()
game_over()