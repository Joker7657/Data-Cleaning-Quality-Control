from src.loader import DataLoader
from src.cleaner import DataCleaner
from src.normalizer import Normalizer
from src.validator import Validator
import pandas as pd


class Pipeline:

    def run(self, path):
        loader = DataLoader(path)
        df = loader.load()

        cleaner = DataCleaner()
        df = cleaner.basic_clean(df)

        normalizer = Normalizer()
        df["cpf"] = df["cpf"].apply(normalizer.normalize_cpf)
        df["email"] = df["email"].apply(normalizer.normalize_email)
        df["telefone"] = df["telefone"].apply(normalizer.normalize_phone)
        df["renda"] = df["renda"].apply(normalizer.normalize_currency)

        validator = Validator()
        report = validator.validate(df)

        df_validos = df.dropna()
        df_rejeitados = df[df.isna().any(axis=1)]

        return df_validos, df_rejeitados, report