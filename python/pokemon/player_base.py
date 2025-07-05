from abc import abstractmethod
from name_servise import NameService


class Player(NameService):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def greeting(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if NameService.validate_name(new_name):
            return
        self.__name = new_name
