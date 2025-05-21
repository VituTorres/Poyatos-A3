from generators.factory import GeneratorFactory
from validators.password_validator import PasswordValidator

def get_valid_input(prompt, validation_func, error_message):
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if validation_func(user_input):
                return user_input
            print(error_message)
        except ValueError:
            print("Por favor, insira um valor válido.")

def main():
    print("=== Password Generator ===")
    print("Options: basic, strong")
    
    # Validação do tipo de gerador
    generator_type = get_valid_input(
        "Generator type (basic/strong): ",
        lambda x: x in ['basic', 'strong'],
        "Erro: Digite 'basic' ou 'strong'"
    )
    
    # Validação do comprimento
    length = int(get_valid_input(
        "Length (8-20): ",
        lambda x: x.isdigit() and 8 <= int(x) <= 20,
        "Erro: Digite um número entre 8 e 20"
    ))
    
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