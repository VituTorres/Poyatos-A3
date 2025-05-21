from generators.factory import GeneratorFactory
from validators.password_validator import PasswordValidator

def main():
    print("=== Password Generator ===")
    print("Options: basic, strong")
    generator_type = input("Generator type: ").strip().lower()
    length = int(input("Length: ").strip())
    
    try:
        generator = GeneratorFactory.create_generator(generator_type)
        password = generator.generate(length)
        
        print(f"\nGenerated Password: {password}")
        print(f"Strength: {generator.get_strength()}")
        
        validation = PasswordValidator.validate(password)
        print(PasswordValidator.get_validation_message(validation))
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()