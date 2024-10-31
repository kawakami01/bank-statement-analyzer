from core.analyzer import BankStatementAnalyzer
from config.settings import SUPPORTED_BANKS


def main():
    analyzer = BankStatementAnalyzer()

    file_mapping = {
        'cartao_credito_xp.csv': SUPPORTED_BANKS['xp']['credit_card'],
        'conta_corrente_xp.csv': SUPPORTED_BANKS['xp']['checking_account']
    }

    df_final = analyzer.process_directory('./extratos', file_mapping)

    df_final.to_excel('./extratos/final_dataframe.xlsx', index=False)
    print('DataFrame create successfully!')


if __name__ == "__main__":
    main()
