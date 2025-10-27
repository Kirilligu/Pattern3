from abc import ABC, abstractmethod


class abstract_convertor(ABC):
    """
    Абстрактный класс конвертера объектов в словари
    """
    @abstractmethod
    def convert(self, obj) -> dict:
        pass