import unittest
from src.validators.password_validator import PasswordValidator

class TestPasswordValidator(unittest.TestCase):
    def test_validate_strong_password(self):
        """Testa a validação de uma senha forte que atende a todos os critérios"""
        password = "StrongP@ss123"
        validation = PasswordValidator.validate(password)
        self.assertTrue(all(validation.values()))
        message = PasswordValidator.get_validation_message(validation)
        self.assertEqual(message, "a senha é forte")

    def test_validate_weak_password(self):
        """Testa a validação de uma senha fraca que não atende a múltiplos critérios"""
        password = "weak"
        validation = PasswordValidator.validate(password)
        expected = {
            'length': False,
            'has_upper': False,
            'has_lower': True,
            'has_digit': False,
            'has_special': False
        }
        self.assertEqual(validation, expected)
        message = PasswordValidator.get_validation_message(validation)
        self.assertIn("pelo menos 8 caracteres", message)
        self.assertIn("letra maiúscula", message)
        self.assertIn("dígito", message)
        self.assertIn("caractere especial", message)

    def test_validate_partial_requirements(self):
        """Testa a validação de senhas que atendem alguns, mas não todos os critérios"""
        test_cases = [
            ("Password123", ['caractere especial']),  # Missing special char
            ("pass@word", ['letra maiúscula', 'dígito']),  # Missing upper and digit
            ("12345678@", ['letra maiúscula', 'letra minúscula']),  # Missing letters
        ]
        
        for password, expected_missing in test_cases:
            with self.subTest(password=password):
                validation = PasswordValidator.validate(password)
                message = PasswordValidator.get_validation_message(validation)
                for missing in expected_missing:
                    self.assertIn(missing, message)

    def test_validate_edge_cases(self):
        """Testa a validação com casos extremos"""
        test_cases = [
            ("", {'length': False, 'has_upper': False, 'has_lower': False,
                  'has_digit': False, 'has_special': False}),
            ("A1@a", {'length': False, 'has_upper': True, 'has_lower': True,
                     'has_digit': True, 'has_special': True}),
            ("12345678", {'length': True, 'has_upper': False, 'has_lower': False,
                         'has_digit': True, 'has_special': False}),
        ]
        
        for password, expected in test_cases:
            with self.subTest(password=password):
                validation = PasswordValidator.validate(password)
                self.assertEqual(validation, expected)

if __name__ == '__main__':
    unittest.main()