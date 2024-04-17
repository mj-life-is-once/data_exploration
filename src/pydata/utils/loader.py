import os

import pandas as pd


class Loader:
    @staticmethod
    def write_data_to_csv(df: pd.DataFrame, output_path: str, debug=False, **kwargs):
        if not os.path.isabs(output_path):
            output_path = os.path.abspath(output_path)
        dir_path = os.path.dirname(output_path)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        df.to_csv(output_path, **kwargs)
        if debug:
            print(f"Data written to {output_path}")
