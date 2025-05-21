import logging
from .password_observer import PasswordObserver

class LoggingObserver(PasswordObserver):
    """Observer que registra senhas geradas em log."""
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("PasswordGenerator")

    def on_password_generated(self, password: str, strength: str):
        self.logger.info(f"Nova senha gerada: {password} (Força: {strength})")