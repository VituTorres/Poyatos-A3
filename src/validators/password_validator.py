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
            return "Password is very strong"
        
        missing = []
        if not validation['length']: missing.append("at least 8 characters")
        if not validation['has_upper']: missing.append("uppercase letter")
        if not validation['has_lower']: missing.append("lowercase letter")
        if not validation['has_digit']: missing.append("digit")
        if not validation['has_special']: missing.append("special character")
        
        return "Password missing: " + ", ".join(missing)