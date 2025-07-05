from player_base import Player

class Satoshi(Player):
    def greeting(self):
        """挨拶の表示"""
        print(f"こんにちは！{self.name}です")
