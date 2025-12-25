import pandas as pd


class DataCleaner:

    def basic_clean(self, df: pd.DataFrame):
        df = df.apply(lambda col: col.astype(str).str.strip())
        df = df.replace(["None", "nan", "NaN", "NULL", "?"], pd.NA)
        return df