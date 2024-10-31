import pandas as pd

from core.interfaces import StatementProcessor
from utils.date_helpers import add_weekday


class BaseProcessor(StatementProcessor):
    """Classe base com funcionalidades comuns para processadores."""

    def process(self, file_path: str) -> pd.DataFrame:
        pass

    @staticmethod
    def _standardize_columns(dataframe: pd.DataFrame, column_mapping: dict) -> pd.DataFrame:
        """Padroniza as colunas do DataFrame."""
        dataframe = dataframe.rename(columns=column_mapping)
        return dataframe[['date', 'description', 'amount']]

    @staticmethod
    def _prepare_dataframe(dataframe: pd.DataFrame, account_type: str) -> pd.DataFrame:
        """Prepara o DataFrame com colunas padrão."""
        dataframe['account_type'] = account_type
        dataframe['date'] = dataframe['date'].str.split(' às ').str[0]
        dataframe['date'] = pd.to_datetime(dataframe['date'], format='%d/%m/%y', dayfirst=True, errors='coerce')
        dataframe['date'] = dataframe['date'].dt.date
        dataframe = add_weekday(dataframe, 'date')
        return dataframe
