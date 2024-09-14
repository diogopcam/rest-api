import os
import pandas as pd

class CandidateService:
    def __init__(self):
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'repository', 'candidatos_poa_rs_2024.csv')
        self.df = pd.read_csv(csv_path)

    def obter_dados(self):
        return self.df

    def get_from_party(self, party_name):
        candidatos_do_partido = self.df[self.df.iloc[:, 26] == party_name]
        lista_candidatos = candidatos_do_partido.to_dict(orient='records')
        return lista_candidatos

