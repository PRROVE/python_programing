class Equipment:
    def __init__(self,name,grade,attack_bonus,defense_bonus):
        self.name = name
        self.grade = grade
        self.attack_bonus = attack_bonus
        self.defense_bonus= defense_bonus

    def __str__(self):
        return (f"Name: {self.name},Grade: {self.grade},Attack_bonus: {self.attack_bonus},Defense_bonus: {self.defense_bonus}")