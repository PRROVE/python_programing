#battle.py
import random
class Battle:
    def fight(self, hero, monster):
        print(f"\n전투 시작! {hero.name} vs {monster.name}")
        if hero.speed > monster.speed:
            print(f"{hero.name}이(가) 속도가 더 빨라서 선공합니다!")
            attacker, defender = hero, monster
        elif hero.speed < monster.speed:
            print(f"{monster.name}이(가) 속도가 더 빨라서 선공합니다!")
            attacker, defender = monster, hero
        else:
            print("속도가 동일하여 무작위로 선공을 결정합니다!")
            if random.choice([True, False]):
                attacker, defender = hero, monster
            else:
                attacker, defender = monster, hero
        turn = 0

        while hero.is_alive() and monster.is_alive():
            if turn % 2 == 0:
                damage = hero.special_attack()
                monster.take_damage(damage)
                print(f"{hero.name}이(가) {monster.name}에게 {damage}의 피해를 입혔습니다!")
            else:
                if random.random() < 0.3:
                    damage = monster.special_attack()
                    print(f"{monster.name}이(가) 파워 공격을 사용했습니다!")
                else:
                    damage = monster.attack
                    print(f"{monster.name}이(가) 일반 공격을 사용했습니다!")

                hero.take_damage(damage)
                print(f"{monster.name}이(가) {hero.name}에게 {damage}의 피해를 입혔습니다!")
            turn += 1

        if not monster.is_alive():
            print(f"{monster.name}이(가) 쓰러졌습니다! {hero.name}이(가) 승리했습니다!")
            hero.gain_exp(20)
            print(f"{hero.name}가 경험치 20 얻음")
        else:
            print(f"{hero.name}이(가) 쓰러졌습니다! {monster.name}이(가) 승리했습니다!")

#character.py
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

#Equipment.py
class Equipment:
    def __init__(self,name,grade,attack_bonus,defense_bonus):
        self.name = name
        self.grade = grade
        self.attack_bonus = attack_bonus
        self.defense_bonus= defense_bonus

    def __str__(self):
        return (f"Name: {self.name},Grade: {self.grade},Attack_bonus: {self.attack_bonus},Defense_bonus: {self.defense_bonus}")

    #main
    from character import Hero, Monster
    from battle import Battle

    def main():
        print("==== RPG 게임 ====")
        name = input("영웅의 이름을 입력하세요: ")
        role = input("직업을 선택하세요 (Warrior/Mage/Archer): ")
        hero = Hero(name="아서", hp=100, attack=20, defense=10, role="전사")
        print(f"\n{hero.name} ({hero.role})이(가) 생성되었습니다!")
        print(hero)

        monster = Monster(name="고블린", hp=50, attack=15, defense=5, )
        print(f"\n몬스터 {monster.name}이(가) 등장했습니다!")
        print(monster)

        battle = Battle()
        for i in range(5):
            print(f"\n====={i + 1}번째 전투=====")
            Battle.fight(hero, monster)
            monster.level_up()
        print("\n전투 후 영웅 상태:")
        print(hero)

    if __name__ == "__main__":
        main()
