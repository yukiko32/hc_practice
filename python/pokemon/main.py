from player import Satoshi
from pokemon import Pikachu


def main():
    # ポケモンの動作確認
    pika = Pikachu("ピカチュウ","でんき", "", 100)
    pika.attack()
    print(pika.name)
    pika.name = "うんこ"
    print(pika.name)
    pika.name = "テキセツ"
    print(pika.name)

    print("-"*25)

    # プレイヤーの動作確認
    satoshi = Satoshi("サトシ")
    satoshi.greeting()
    print(satoshi.name)
    satoshi.name = "うんこ"
    print(satoshi.name)
    satoshi.name = "テキセツ"
    print(satoshi.name)


if __name__ == "__main__":
    main()
