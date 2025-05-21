# Password Generator Refactored

## Novas Funcionalidades
- **Padrão Observer**: Notifica quando senhas são geradas
  - Exemplo: `LoggingObserver` registra em log
- **Factory Simplificada**: Função direta em vez de classe
- **Tratamento de Erros Aprimorado**

## Como Usar
```python
from observers.logging_observer import LoggingObserver
from generators.factory import create_generator

generator = create_generator("strong")
generator.add_observer(LoggingObserver())
password = generator.generate(12)