from drink import Drink

class VendingMachine:
    def __init__(self):
        """自動販売機の初期在庫と売り上げ総額の設定を行います"""
        # 自動販売機の初期在庫
        self.drinks_info = [{"name": "ペプシ", "price": 150, "stock": 5},
                            {"name": "モンスター", "price": 230, "stock": 5},
                            {"name": "いろはす", "price": 120, "stock": 5}]
        # 初期在庫を元に辞書を作成
        # キーはドリンクの名前、値はリストにDrinkインスタンスを在庫数分格納する
        self.drink_stock_dict = {}
        for drink_info in self.drinks_info:
            stock_list = [Drink(drink_info["name"], drink_info["price"]) for _ in range(drink_info["stock"])]
            self.drink_stock_dict[drink_info["name"]] = stock_list
        # 自動販売機の売り上げ総額
        self.__total_revenue = 0

    def get_stock(self, drink_name):
        """
        ドリンクの在庫数を取得します
        :param drink_name: 在庫数を取得するドリンクの名前
        :return: ドリンクの在庫数
        """
        return len(self.drink_stock_dict[drink_name])

    def is_purchasable(self, drink_name):
        """
        ドリンクの在庫数を元に購入可否を真偽値で取得します（1本以上の場合は可）
        :param drink_name: 購入可否の真偽値を取得するドリンクの名前
        :return: True/False
        """
        return self.get_stock(drink_name) > 0

    def purchase(self, suica_instance, drink_name):
        """
        ドリンクを購入する際の処理を行います
        購入した場合はドリンクを1本減らし、自販機の売り上げを追加し、suicaの残高を減らします
        購入できない場合は例外を発生させます
        :param suica_instance: 購入に使用するsuicaインスタンス
        :param drink_name: 購入するドリンク
        :raises ValueError: 在庫不足またはsuicaの残高不足の場合
        """
        if not self.is_purchasable(drink_name):
            raise ValueError(f"{drink_name}の在庫がありません")
        deposit = suica_instance.deposit
        drinks = self.drink_stock_dict[drink_name]
        price = drinks[0].price
        if deposit < price:
            raise ValueError(f"suicaの残高が不足しています")
        del drinks[0]
        self.__total_revenue += price
        suica_instance.pay(price)

    @property
    def total_revenue(self):
        """
        自動販売機の売り上げ総額を取得します
        :return: 自動販売機の売り上げ総額
        """
        return self.__total_revenue

    def purchasable_list(self):
        """
        購入可能なドリンク（在庫が1本以上）の名前をリスト型で取得します
        :return: 購入可能なドリンク名のリスト
        """
        purchasable_list = [drinks[0].name for drinks in self.drink_stock_dict.values() if len(drinks) > 0]
        return purchasable_list

    def add_stock(self, drink_name, pieces):
        """
        自動販売機にドリンクの在庫を補充します
        :param drink_name: 補充するドリンクの名前
        :param pieces: 補充する本数
        """
        for drink_info in self.drinks_info:
            if drink_name == drink_info["name"]:
                for _ in range(pieces):
                    self.drink_stock_dict[drink_name].append(Drink(drink_name, drink_info["price"]))
