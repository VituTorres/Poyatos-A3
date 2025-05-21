# Poyatos-A3: GESTÃO E QUALIDADE DE SOFTWARE

## Professores
- Henrique Poyatos  
- Magda

## Alunos
- Victor Inocencio Torres RA:824213703
-
-
-
-

Projeto acadêmico demonstrando a refatoração de um gerador de senhas
## 📋 Estrutura do Projeto
```
Poyatos-A3/
├── legacy/              # Código original (para comparação)
├── src/               # Código refatorado
│   ├── generators/        # Implementações dos geradores (Strategy Pattern)
│   ├── observers/        # Sistema de notificação (Observer Pattern)
│   ├── validators/       # Validação de senhas
│   └── main.py           # Interface de linha de comando
├── tests/               # Testes unitários
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Pip instalado

### Instalação
```bash
git clone https://github.com/VituTorres/Poyatos-A3.git
cd Poyatos-A3
pip install -r requirements.txt
```

### Versão Refatorada
```bash
python src/main.py
```
### Versão Legada
```bash
python legacy/old_password_generator.py
```
**Fluxo:**
1. Escolha o tipo (`basic` ou `strong`)
2. Insira o comprimento (8-20 caracteres)
3. Receba a senha com análise de força

### Testes Unitários
```bash
# Executar todos os testes
pytest tests/ -v

# Com cobertura de código
pytest --cov=src --cov-report=term-missing tests/
```

## 🛠 Padrões de Design
| Padrão         | Implementação                        | Benefício                           |
|-----------------|----------------------------------------|-----------------------------------|
| **Strategy**    | `BasicGenerator` e `StrongGenerator`   | Algoritmos intercambiáveis        |
| *+Observer*+    | `LoggingObserver`                  | Notificações em tempo real       |
| **Factory**     | `GeneratorFactory`                | Criação centralizada de objetos   |


## 📝 Licença
MIT License - Veja o arquivo [LICENSE](LICENSE) para detalhes.
