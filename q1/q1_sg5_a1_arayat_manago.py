# RPG Game
class Hero:
    def __init__(self, name: str, hp:int):
        self.name = name
        self.hp = hp
    def take_damage(self, amount:int):
        self.hp -= amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)
arthur.take_damage(10)
print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")

    
