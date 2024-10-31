from processors.xp.xp_credit_card_processor import XPCreditCardProcessor
from processors.xp.xp_checking_account_processor import XPCheckingAccountProcessor
from core.interfaces import StatementProcessor


class StatementProcessorFactory:
    """Fábrica para criar processadores de extratos."""

    @staticmethod
    def create_processor(statement_type: str) -> StatementProcessor:
        processors = {
            'xp_credit_card_processor': XPCreditCardProcessor(),
            'xp_checking_account_processor': XPCheckingAccountProcessor()
        }
        return processors.get(statement_type)
