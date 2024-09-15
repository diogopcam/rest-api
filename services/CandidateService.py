import os
import pandas as pd

class CandidateService:
    def __init__(self):
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'repository', 'candidatos_poa_rs_2024.csv')
        excel_path = os.path.join(os.path.dirname(__file__), '..', 'repository', 'candidatos_poa_rs_2024.xlsx')
        self.df = pd.read_excel(excel_path)

    def obter_dados(self):
        return self.df

    def get_from_party(self, party_name):
        candidatos_do_partido = self.df[self.df.iloc[:, 8] == party_name]
        lista_candidatos = candidatos_do_partido.to_dict(orient='records')
        return lista_candidatos
    
    def get_by_number(self, candidate_number):
        candidato = self.df[self.df['NR_CANDIDATO'] == int(candidate_number)]
        return candidato.to_dict(orient='records')
    
    def add_candidate(self, data):
        self.df = self.df._append(data, ignore_index=True)
        return

    def update_candidate(self, candidate_number, data):
        candidato = self.df[self.df['NR_CANDIDATO'] == int(candidate_number)]
        self.df = self.df.drop(candidato.index)
        self.df = self.df._append(data, ignore_index=True)
        return

    def delete_candidate(self, candidate_number):
        candidato = self.df[self.df['NR_CANDIDATO'] == int(candidate_number)]
        self.df = self.df.drop(candidato.index)
        return