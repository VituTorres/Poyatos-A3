"""CÓDIGO LEGADO - Versão original do gerador de senhas # type: ignore
"""
import random
import string

def gerar(tamanho=8, especial=False):
    chars = string.ascii_letters + string.digits
    if especial:
        chars += '!@#$%^&*()'
    
    senha = ''
    for _ in range(tamanho):
        senha += random.choice(chars)
    
    return senha

def main():
    print("GERADOR DE SENHAS LEGADO")
    t = int(input("Tamanho: "))
    e = input("Especiais? (s/n): ").lower() == 's'
    
    print("Senha:", gerar(t, e))

if __name__ == "__main__":
    main()