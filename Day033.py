class Warrior:
    def __init__(self,power,defense,hp) -> None:
        self.atk=power
        self.defense=defense
        self.hp=hp
    def attack(self,warrior_object):
        if self.atk > warrior_object.defense:
            warrior_object.hp -= (self.atk-warrior_object.defense)
    
Warrior_A = Warrior(100,50,80)
Warrior_B = Warrior(60,80,120)
print("=== Before Attack ===")
print("Warrior_A HP =",Warrior_A.hp)
print("Warrior_B HP =",Warrior_B.hp)
Warrior_A.attack(Warrior_B)
Warrior_B.attack(Warrior_A)
print("=== After Attack ===")
print("Warrior_A HP =",Warrior_A.hp)
print("Warrior_B HP =",Warrior_B.hp)