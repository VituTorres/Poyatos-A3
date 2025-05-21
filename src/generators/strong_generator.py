import random
import string
from .base_generator import PasswordGenerator

class StrongGenerator(PasswordGenerator):
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self, length: int = 12) -> str:
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
        return ''.join(password)

    def get_strength(self) -> str:
        return "Strong"