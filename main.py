from character import Hero, Monster
from battle import Battle


def main():
    print("==== RPG 게임 ====")
    name = input("영웅의 이름을 입력하세요: ")
    role = input("직업을 선택하세요 (Warrior/Mage/Archer): ")
    hero = Hero(name="아서",hp=100, attack=20, defense=10, role="전사")
    print(f"\n{hero.name} ({hero.role})이(가) 생성되었습니다!")
    print(hero)

    monster = Monster(name="고블린", hp=50, attack=15, defense=5,)
    print(f"\n몬스터 {monster.name}이(가) 등장했습니다!")
    print(monster)

    battle = Battle()
    for i in range(5):
        print(f"\n====={i+1}번째 전투=====")
        Battle.fight(hero,monster)
        monster.level_up()
    print("\n전투 후 영웅 상태:")
    print(hero)


if __name__ == "__main__":
    main()
