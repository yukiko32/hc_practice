from abc import ABC, abstractmethod


class NameService(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, new_name):
        pass

    @staticmethod
    def validate_name(new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return True
        return False
