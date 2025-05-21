import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))
import unittest
from generators.basic_generator import BasicGenerator
from generators.strong_generator import StrongGenerator

class TestPasswordGenerators(unittest.TestCase):
    def test_basic_generator(self):
        generator = BasicGenerator()
        password = generator.generate(8)
        self.assertEqual(len(password), 8)
        self.assertEqual(generator.get_strength(), "Medium")
    
    def test_strong_generator(self):
        generator = StrongGenerator()
        password = generator.generate(12)
        self.assertEqual(len(password), 12)
        self.assertEqual(generator.get_strength(), "Strong")

# tests/test_validator.py
import unittest
from validators.password_validator import PasswordValidator

class TestPasswordValidator(unittest.TestCase):
    def test_validation(self):
        test_cases = [
            ("Abc123!", {'length': False, 'has_upper': True, 'has_lower': True, 'has_digit': True, 'has_special': True}),
            ("Abcdefgh", {'length': True, 'has_upper': True, 'has_lower': True, 'has_digit': False, 'has_special': False}),
            ("12345678", {'length': True, 'has_upper': False, 'has_lower': False, 'has_digit': True, 'has_special': False}),
        ]
        
        for password, expected in test_cases:
            with self.subTest(password=password):
                self.assertEqual(PasswordValidator.validate(password), expected)

if __name__ == "__main__":
    unittest.main()

# tests/test_observers.py
import unittest
from unittest.mock import patch
from src.observers.logging_observer import LoggingObserver

class TestLoggingObserver(unittest.TestCase):
    @patch('builtins.print')  # Mock da função print
    def test_logging(self, mock_print):
        """Testa se o observer registra no log corretamente"""
        observer = LoggingObserver()
        test_password = "test123"
        test_strength = "Medium"
        
        observer.on_password_generated(test_password, test_strength)
        
        # Verifica se print foi chamado com os valores esperados
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        self.assertIn("Nova senha gerada", args[0])
        self.assertIn(test_password, args[0])
        self.assertIn(test_strength, args[0])