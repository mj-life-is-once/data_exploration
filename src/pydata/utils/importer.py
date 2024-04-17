import os

import pandas as pd

from .logger import pydataLogger


class Importer:
    @staticmethod
    def read_csv(file_path: str, **kwargs) -> pd.DataFrame:
        if not os.path.isabs(file_path):
            file_path = os.path.abspath(file_path)
        df = pd.read_csv(file_path, **kwargs)
        return df

    @staticmethod
    def test():
        print("test")
        return "test"
