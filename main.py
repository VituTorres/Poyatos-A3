from src.generators.factory import create_generator
from src.validators.password_validator import PasswordValidator
from src.observers.logging_observer import LoggingObserver

def get_valid_input(prompt: str, validator, error_msg: str):
    """Obtém entrada do usuário com validação."""
    while True:
        try:
            value = input(prompt).strip()
            if validator(value):
                return value
            print(error_msg)
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def main():
    print("=== Gerador de Senhas Refatorado ===")
    
    # Configura observers
    generator = create_generator(
        get_valid_input(
            "Tipo (basic/strong): ",
            lambda x: x.lower() in ['basic', 'strong'],
            "Digite 'basic' ou 'strong'"
        )
    )
    generator.add_observer(LoggingObserver())

    # Gera senha
    password = generator.generate(
        int(get_valid_input(
            "Comprimento (8-20): ",
            lambda x: x.isdigit() and 8 <= int(x) <= 20,
            "Digite um número entre 8 e 20"
        ))
    )

    # Validação
    validation = PasswordValidator.validate(password)
    print(f"\nSenha: {password}")
    print(f"Força: {generator.get_strength()}")
    print(PasswordValidator.get_validation_message(validation))

if __name__ == "__main__":
    main()