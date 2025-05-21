import unittest
from unittest.mock import patch
from src.observers.logging_observer import LoggingObserver

class TestLoggingObserver(unittest.TestCase):
    @patch('builtins.print')  # Mock da função print
    def test_logging(self, mock_print):
        """Testa se o observador registra no log corretamente"""
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

if __name__ == '__main__':
    unittest.main()