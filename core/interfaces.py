from abc import ABC, abstractmethod
import pandas as pd


class StatementProcessor(ABC):
    """Abstract base class for processing bank statements."""

    @abstractmethod
    def process(self, file_path: str) -> pd.DataFrame:
        """Processes a bank statement file and returns the extracted data as a DataFrame."""
        pass
