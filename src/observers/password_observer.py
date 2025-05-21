from abc import ABC, abstractmethod

class PasswordObserver(ABC):
    """Interface Observer para notificação de geração de senhas."""
    @abstractmethod
    def on_password_generated(self, password: str, strength: str):
        """Método chamado quando uma nova senha é gerada."""
        pass