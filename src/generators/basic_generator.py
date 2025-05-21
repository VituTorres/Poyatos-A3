# src/generators/basic_generator.py
import random
import string
from .base_generator import PasswordGenerator

class BasicGenerator(PasswordGenerator):
    """Gerador de senhas básicas (letras e números) com suporte a Observer"""
    
    def __init__(self):
        super().__init__()  # Chama o __init__ da classe base (importante para observers)
        self.characters = string.ascii_letters + string.digits

    def generate(self, length: int = 8) -> str:
        """Gera uma senha básica e notifica os observers"""
        if length < 4:
            raise ValueError("a senha precisa ter pelo menos 4 caracteres")
        
        password = ''.join(random.choice(self.characters) for _ in range(length))
        self._notify_observers(password)  # Notifica todos os observers
        return password

    def get_strength(self) -> str:
        return "Medium"