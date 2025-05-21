from abc import ABC, abstractmethod

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self, length: int) -> str:
        """Gera uma senha com o comprimento especificado"""
        pass

    @abstractmethod
    def get_strength(self) -> str:
        """Retorna a força da senha gerada"""
        pass