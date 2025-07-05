from pokemon_base import Pokemon


class Pikachu(Pokemon):
    def attack(self):
        print(f"{self.name}の10万ボルト！")
