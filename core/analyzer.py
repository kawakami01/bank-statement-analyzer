from typing import Dict
import pandas as pd
import os
from processors.factory import StatementProcessorFactory


class BankStatementAnalyzer:
    """Classe principal para análise de extratos bancários."""

    def __init__(self):
        self.factory = StatementProcessorFactory()
        self.final_df = pd.DataFrame()

    def process_directory(self, directory_path: str, file_mapping: Dict[str, str]) -> pd.DataFrame:
        """
        Processa todos os arquivos em um diretório.

        Args:
            directory_path: Caminho para o diretório com os extratos
            file_mapping: Dicionário mapeando nome do arquivo para tipo de extrato
        """
        dfs = []

        for filename, statement_type in file_mapping.items():
            file_path = os.path.join(directory_path, filename)
            if os.path.exists(file_path):
                if processor := self.factory.create_processor(statement_type):
                    df = processor.process(file_path)
                    dfs.append(df)

        if dfs:
            self.final_df = pd.concat(dfs, ignore_index=True)
            self.final_df = self.final_df.sort_values('date')

        return self.final_df
