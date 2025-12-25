import re
import pandas as pd


class Normalizer:

    def normalize_cpf(self, cpf):
        if pd.isna(cpf):
            return pd.NA
        digits = re.sub(r'\D', '', cpf)
        return digits if len(digits) == 11 else pd.NA

    def normalize_email(self, email):
        if pd.isna(email):
            return pd.NA
        email = email.lower()
        pattern = r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$"
        return email if re.match(pattern, email) else pd.NA

    def normalize_phone(self, phone):
        if pd.isna(phone):
            return pd.NA
        digits = re.sub(r'\D', '', phone)
        if len(digits) >= 10:
            return digits
        return pd.NA

    def normalize_currency(self, value):
        if pd.isna(value):
            return pd.NA
        value = re.sub(r'[R$\\s]', '', value)
        value = value.replace('.', '').replace(',', '.')
        try:
            return float(value)
        except:
            return pd.NA