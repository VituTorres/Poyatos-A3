import random
import string
from .base_generator import PasswordGenerator

class StrongGenerator(PasswordGenerator):
    """Gerador de senhas fortes com caracteres especiais."""
    def __init__(self):
        super().__init__()
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self, length: int = 12) -> str:
        """Gera uma senha forte garantindo pelo menos um caractere de cada tipo."""
        if length < 8:
            raise ValueError("Strong password must be at least 8 characters")
        
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password.extend(random.choice(self.characters) for _ in range(length-4))
        random.shuffle(password)
        password_str = ''.join(password)
        self._notify_observers(password_str)
        return password_str

    def get_strength(self) -> str:
        return "Strong"