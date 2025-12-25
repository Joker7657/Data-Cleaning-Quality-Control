import pandas as pd
import re


class Validator:

    def validate(self, df):
        report = {}

        report["missing_name"] = df["nome"].isna().sum()

        report["invalid_email"] = df["email"].apply(
            lambda x: not bool(re.match(r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$", str(x)))
        ).sum()

        report["invalid_cpf"] = df["cpf"].apply(
            lambda x: len(str(x)) != 11
        ).sum()

        report["invalid_phone"] = df["telefone"].apply(
            lambda x: len(str(x)) < 10
        ).sum()

        return report