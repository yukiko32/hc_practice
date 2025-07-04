from suica import Suica
from vending_machine import VendingMachine

# 実行例
def main():
    # インスタンス生成
    suica = Suica()
    vending_machine = VendingMachine()

    # suicaのチャージ残高
    print(f"suicaのチャージ残高：{suica.deposit}")

    # suicaにチャージする
    charge = 300
    print(f"suicaに{charge}円チャージする")
    suica.deposit = charge

    # suicaのチャージ残高
    print(f"suicaのチャージ残高：{suica.deposit}")

    # ドリンクの在庫数を取得
    drink = "ペプシ"
    print(f"{drink}の在庫数：{vending_machine.get_stock(drink)}")
    drink = "モンスター"
    print(f"{drink}の在庫数：{vending_machine.get_stock(drink)}")
    drink = "いろはす"
    print(f"{drink}の在庫数：{vending_machine.get_stock(drink)}")

    # ドリンクを購入できるか判定
    drink = "ペプシ"
    print(f"{drink}の購入判定：{vending_machine.is_purchasable(drink)}")

    # ドリンクを購入する
    drink = "ペプシ"
    vending_machine.purchase(suica, drink)
    print(f"{drink}を購入する")

    # 売り上げ総額を取得
    print(f"売り上げ総額：{vending_machine.total_revenue}")

    # 購入可能なドリンクのリスト
    print(f"購入可能なドリンクのリスト：{vending_machine.purchasable_list()}")

    # ドリンクを補充する
    drink = "ペプシ"
    pieces = 5
    vending_machine.add_stock(drink, pieces)
    print(f"{drink}を{pieces}本補充する")

    # ドリンクの在庫数を取得
    drink = "ペプシ"
    print(f"{drink}の在庫数：{vending_machine.get_stock(drink)}")


if __name__ == "__main__":
    main()
