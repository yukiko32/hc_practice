from abc import ABC, abstractmethod


class NameService(ABC):
    @property
    @abstractmethod
    def name(self):
        """ゲッターメソッドを子クラスに強制する"""
        pass

    @name.setter
    @abstractmethod
    def name(self, new_name):
        """セッターメソッド（強制力は無いが参考のため記述）"""
        pass

    @staticmethod
    def validate_name(new_name):
        """
        設定する名前を検証する
        :param new_name: 新しく設定する名前
        :return: 不適切な場合はTrue
        """
        if new_name == "うんこ":
            print("不適切な名前です")
            return True
        return False
