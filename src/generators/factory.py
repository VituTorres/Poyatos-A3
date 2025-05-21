from .basic_generator import BasicGenerator
from .strong_generator import StrongGenerator

def create_generator(generator_type: str):
    """Função factory simplificada para criar geradores de senha."""
    generators = {
        'basic': BasicGenerator,
        'strong': StrongGenerator
    }
    if generator_type not in generators:
        raise ValueError(f"Tipo de gerador inválido: {generator_type}")
    return generators[generator_type]()