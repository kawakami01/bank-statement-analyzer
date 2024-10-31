from ..base_processor import BaseProcessor
import pandas as pd


class XPCreditCardProcessor(BaseProcessor):
    def process(self, file_path: str) -> pd.DataFrame:
        dataframe = pd.read_csv(file_path, sep=';')

        column_mapping = {
            'Data': 'date',
            'Estabelecimento': 'description',
            'Valor': 'amount'
        }

        dataframe = self._standardize_columns(dataframe, column_mapping)
        dataframe = self._prepare_dataframe(dataframe, 'credit_card')

        return dataframe
