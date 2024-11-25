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
