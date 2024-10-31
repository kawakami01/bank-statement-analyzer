import pandas as pd


def add_weekday(dataframe: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Adds a new column to the DataFrame that represents the day of the week for a specified date column.

    Args:
        dataframe (pd.DataFrame): The DataFrame to which the weekday column will be added.
        date_column (str): The name of the column containing date values.

    Returns:
        pd.DataFrame: The original DataFrame with an additional column named 'dia_semana' containing the weekday names.
    """
    dataframe['day_of_the_week'] = pd.to_datetime(dataframe[date_column]).dt.day_name()
    return dataframe
