import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))
import unittest
from unittest.mock import Mock
from generators.basic_generator import BasicGenerator
from generators.strong_generator import StrongGenerator
from generators.base_generator import PasswordGenerator
from generators.factory import create_generator
from observers.password_observer import PasswordObserver

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

class ConcreteGenerator(PasswordGenerator):
    """Implementação concreta do PasswordGenerator para testes"""
    def generate(self, length: int) -> str:
        return "test" * (length // 4)
    
    def get_strength(self) -> str:
        return "Test"

class TestBaseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ConcreteGenerator()
        self.mock_observer = Mock(spec=PasswordObserver)

    def test_add_observer(self):
        """Testa a adição de um observador ao gerador"""
        self.generator.add_observer(self.mock_observer)
        self.assertIn(self.mock_observer, self.generator._observers)

    def test_abstract_class_instantiation(self):
        """Testa que PasswordGenerator não pode ser instanciado diretamente"""
        with self.assertRaises(TypeError):
            PasswordGenerator()

class TestFactory(unittest.TestCase):
    def test_create_basic_generator(self):
        """Testa a criação de um gerador básico"""
        generator = create_generator('basic')
        self.assertIsInstance(generator, BasicGenerator)

    def test_create_strong_generator(self):
        """Testa a criação de um gerador forte"""
        generator = create_generator('strong')
        self.assertIsInstance(generator, StrongGenerator)

    def test_invalid_generator_type(self):
        """Testa o tratamento de erro para tipo de gerador inválido"""
        with self.assertRaises(ValueError) as context:
            create_generator('invalid')
        self.assertIn('Tipo de gerador inválido', str(context.exception))

if __name__ == '__main__':
    unittest.main()