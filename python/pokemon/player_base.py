from abc import abstractmethod
from name_servise import NameService


class Player(NameService):
    def __init__(self, name):
        """
        プレイヤーの初期値を設定する
        :param name: 名前
        """
        self.__name = name

    @abstractmethod
    def greeting(self):
        """挨拶を強制する"""
        pass

    @property
    def name(self):
        """プレイヤーの名前を取得する"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        プレイヤーに新しい名前を設定する
        :param new_name: 新しい名前
        :return: 不適切な名前の場合、None
        """
        if NameService.validate_name(new_name):
            return
        self.__name = new_name
