import pandas as pd
import os


class DataLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        ext = os.path.splitext(self.path)[1]

        if ext in [".csv"]:
            return pd.read_csv(self.path, dtype=str)
        elif ext in [".xlsx", ".xls"]:
            return pd.read_excel(self.path, dtype=str)
        else:
            raise Exception("Formato não suportado")