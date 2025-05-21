from .basic_generator import BasicGenerator
from .strong_generator import StrongGenerator

class GeneratorFactory:
    @staticmethod
    def create_generator(generator_type: str):
        generators = {
            'basic': BasicGenerator,
            'strong': StrongGenerator
        }
        if generator_type not in generators:
            raise ValueError(f"Invalid generator type: {generator_type}")
        return generators[generator_type]()