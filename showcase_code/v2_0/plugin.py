from abc import ABC, abstractmethod
import logging
from typing import Tuple, Union, Generator

class Plugin(ABC):
    """Абстрактный базовый класс для всех плагинов"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def execute(self, command: str) -> Tuple[Union[str, bool], str]:
        """
        Обязательный метод для выполнения команды
        :return: (status: str|bool, message: str)
        """
        pass
    
    def execute_stream(self, command: str) -> Generator[Tuple[Union[str, bool], str], None, None]:
        """
        Опциональный метод для потокового выполнения
        По умолчанию просто вызывает execute
        """
        yield self.execute(command)
    
    @property
    @abstractmethod
    def keywords(self) -> list:
        """Обязательное свойство - ключевые слова для активации плагина"""
        return []
