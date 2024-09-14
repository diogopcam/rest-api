# Classe onde as regras de negócio serão implementadas
import os
import pandas as pd

class CandidateService:
    def __init__(self):
        # Caminho da planilha
        planilha_path = os.path.join(os.path.dirname(__file__), '..', 'repository', 'candidatos_poa_rs_2024.xlsx')

        # Carregar a planilha
        self.df = pd.read_excel(planilha_path)


    def obter_dados(self):
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'repository', 'candidatos_poa_rs_2024.csv')
        df = pd.read_csv(csv_path)
        return df

