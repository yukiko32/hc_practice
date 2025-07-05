class Suica:

    def __init__(self):
        """suicaのデフォルトの預かり金を設定します"""
        self.__deposit = 500

    @property
    def deposit(self):
        """:return: suicaの現在の預かり金を返します"""
        return self.__deposit

    @deposit.setter
    def deposit(self, amount):
        """
        amount分の金額をsuicaにチャージ、または例外を発生させます
        :param amount: suicaにチャージする金額
        :raises ValueError: amountが100未満の場合
        """
        if amount < 100:
            raise ValueError("100円以上をチャージしてください")
        self.__deposit += amount

    def pay(self, amount):
        """amountの金額をsuicaのチャージ残高から減らします（支払い用）"""
        self.__deposit -= amount
