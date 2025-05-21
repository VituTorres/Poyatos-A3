import random
import string
from .base_generator import PasswordGenerator

class BasicGenerator(PasswordGenerator):
    def __init__(self):
        self.characters = string.ascii_letters + string.digits

    def generate(self, length: int = 8) -> str:
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        return ''.join(random.choice(self.characters) for _ in range(length))

    def get_strength(self) -> str:
        return "Medium"