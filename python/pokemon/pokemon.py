from pokemon_base import Pokemon


class Pikachu(Pokemon):
    def attack(self):
        """攻撃内容の表示"""
        print(f"{self.name}の10万ボルト！")
