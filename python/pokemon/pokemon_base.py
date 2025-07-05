from abc import abstractmethod
from name_servise import NameService


class Pokemon(NameService):
    def __init__(self, name, type1, type2, hp):
        """
        ポケモンの初期値を設定する
        :param name: 名前
        :param type1: 一つ目のタイプ
        :param type2: 二つ目のタイプ
        :param hp: 体力
        """
        self.__name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        """攻撃メソッドを子クラスに強制する"""
        pass

    @property
    def name(self):
        """ポケモンの名前を取得する"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        ポケモンに新しい名前を設定する
        :param new_name: 新しい名前
        :return: 不適切な名前の場合、None
        """
        if NameService.validate_name(new_name):
            return
        self.__name = new_name
