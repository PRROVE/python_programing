class Character:
    def __init__(self, name, hp, attack, defense,speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.hp = max(self.hp - actual_damage, 0)
        print(f"{self.name}이(가) {actual_damage}의 피해를 입었습니다. 남은 체력: {self.hp}")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}")

class Hero(Character):
    def __init__(self, name, job, hp, attack, defense, role):
        super().__init__(name, hp, attack, defense)
        self.job = job
        self.role = role
        self.exp = 0
        self.weapon=None
        self.armor=None
        self.level = 1
        self.max_level_up= 1
        self.attack_bonus=0
        self.defense_bonus=0

    def level_up(self):
        self.level += 1
        if self.role == "Warrior":
            self.hp += 20
            self.attack += 5
            self.defense += 3
        elif self.role == "Mage":
            self.hp += 10
            self.attack += 7
            self.speed += 5
        elif self.role == "Archer":
            self.hp += 15
            self.defense += 4
            self.speed += 7
        print(f"{self.name}의 레벨이 {self.level}로 올랐습니다!")


    def equip(self,equipment,attack_bonus=0,defense_bonus=0):
        self.attack_bonus += attack_bonus
        self.defense_bonus += defense_bonus

        if equipment.attack_bonus > 0:
            self.weapon = equipment
            print(f"{self.name}이(가) 무기 {equipment.name}(을)를 장착했습니다!")
        elif equipment.defense_bonus > 0:
            self.armor = equipment
            print(f"{self.name}이(가) 갑옷 {equipment.name}(을)를 장착했습니다!")

    def calculate_attack(self):
        if self.weapon:
            return self.attack+self.weapon.attack_bonus
        else:
            return self.attack

    def calculate_defense(self):
        if self.armor :
            return self.armor + self.armor.defense_bonus
        else:
            return self.armor



    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name}이(가) {amount}의 경험치를 얻었습니다. 총 경험치: {self.exp}")

    def special_attack(self):
        if self.role == "Warrior":
            bonus_damage = 20
        elif self.role == "Mage":
            bonus_damage = 30
        elif self.role == "Archer":
            bonus_damage = 25
        else:
            bonus_damage = 10
        return self.attack + bonus_damage

import random


from abc import ABC ,abstractmethod

class Monster(ABC):
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack

    @abstractmethod
    def special_attack(self): #특별공격
        pass

    @abstractmethod
    def Description(self): #몬스터의 특징
        pass


class Goblin(Monster):
    def special_attack(self):
        damage = self.attack * 1.5
        return (f"{self.name}의 파워어택!", f"데미지: {damage:.1f}")

    def Description(self):
        return(f"{self.name}",f"기본 공격력 : {self.attack}")

class Orc(Monster):
    def special_attack(self):
        damage = self.attack * 2
        return (f"{self.name}의 파워어택!", f"데미지: {damage:.1f}")

    def Description(self):
        return(f"{self.name}",f"기본 공격력 : {self.attack}")

class Dragon(Monster):
    def special_attack(self):
        damage = self.attack * 3
        return (f"{self.name}의 파워어택!", f"데미지: {damage:.1f}")

    def Description(self):
        return(f"{self.name}",f"기본 공격력 : {self.attack}")











# class Monster(Character):
#     def __init__(self, name, hp, attack, defense):
#         super().__init__(name, hp, attack, defense)
#         self.level=1
#
#     def drop_loot(self):
#         if random.random() <=0.5:
#             item_type = random.choice(["weapon", "armor"])
#             grade=random.random()
#
#             if grade <= 0.5:
#                 grade = "Common"
#             elif grade <= 0.3:
#                 grade = "Rare"
#             else :
#                 grade ="Legendary"
#
#     def exp_Leward(self):
#         return self.level *20
#
#     def level_up(self):
#         self.level += 1
#         self.hp= 15
#         self.attack= 3
#         self.defense= 3
#         self.speed= 1

