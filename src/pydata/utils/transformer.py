class Transformer:

    @staticmethod
    def basic_cleanup(df):
        # Remove all unicode characters
        df.replace(r"[^\x00-\x7F]+", "", regex=True, inplace=True)
        return df
