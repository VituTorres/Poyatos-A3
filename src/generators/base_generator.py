from abc import ABC, abstractmethod
from typing import List
from src.observers.password_observer import PasswordObserver

class PasswordGenerator(ABC):
    """Classe base abstrata para geradores de senha com suporte a Observer."""
    def __init__(self):
        self._observers: List[PasswordObserver] = []

    def add_observer(self, observer: PasswordObserver):
        """Adiciona um observer à lista."""
        self._observers.append(observer)

    def _notify_observers(self, password: str):
        """Notifica todos os observers registrados."""
        for observer in self._observers:
            observer.on_password_generated(password, self.get_strength())

    @abstractmethod
    def generate(self, length: int) -> str:
        """Gera uma senha com o comprimento especificado."""
        pass

    @abstractmethod
    def get_strength(self) -> str:
        """Retorna a força da senha gerada."""
        pass