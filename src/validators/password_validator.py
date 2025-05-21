import re

class PasswordValidator:
    @staticmethod
    def validate(password: str) -> dict:
        return {
            'length': len(password) >= 8,
            'has_upper': bool(re.search(r'[A-Z]', password)),
            'has_lower': bool(re.search(r'[a-z]', password)),
            'has_digit': bool(re.search(r'\d', password)),
            'has_special': bool(re.search(r'[^A-Za-z0-9]', password))
        }
    
    @staticmethod
    def get_validation_message(validation: dict) -> str:
        if all(validation.values()):
            return "a senha é forte"
        
        missing = []
        if not validation['length']: missing.append("pelo menos 8 caracteres")
        if not validation['has_upper']: missing.append("letra maiúscula")
        if not validation['has_lower']: missing.append("letra minúscula")
        if not validation['has_digit']: missing.append("dígito")
        if not validation['has_special']: missing.append("caractere especial")
        
        return "Senha faltando: " + ", ".join(missing)