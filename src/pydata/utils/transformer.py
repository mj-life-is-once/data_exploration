import pandas as pd


class Transformer:

    @staticmethod
    def basic_cleanup(df: pd.DataFrame) -> pd.DataFrame:
        # Remove all unicode characters
        df.replace(r"[^\x00-\x7F]+", "", regex=True, inplace=True)
        return df

    @staticmethod
    def change_date_format(date: str) -> str:
        front, end = date.split(" ")
        year, _, _ = front.split("-")
        if year[:2] == "00":
            year = "20" + year[2:]
        front = year + "-" + front[5:]
        return front + " " + end

    @staticmethod
    def reformat_datetime(df: pd.DataFrame) -> pd.DataFrame:
        df["created"] = df["created"].apply(Transformer.change_date_format)
        df["ended"] = df["ended"].apply(Transformer.change_date_format)

        df["created"] = pd.to_datetime(df["created"])
        df["ended"] = pd.to_datetime(df["ended"])

        df["chargeTimeHrs"] = pd.to_timedelta(df["chargeTimeHrs"])
        return df

    @staticmethod
    def drop_columns_with_nulls(df: pd.DataFrame, threshold=30) -> pd.DataFrame:
        # calculate the percentage of missing values in each column
        missing_perc = df.isna().sum() / df.shape[0] * 100

        # Drop columns with a percentage of missing values above the threshold
        columns_to_drop = missing_perc[missing_perc > threshold].index
        df = df.drop(columns=columns_to_drop)
        return df

    @staticmethod
    def sort_by_week(df: pd.DataFrame) -> pd.DataFrame:
        sorter = [
            "Sun",
            "Sat",
            "Fri",
            "Thu",
            "Wed",
            "Tue",
            "Mon",
        ]
        # Convert 'day_of_week' to categorical type
        df["weekday"] = pd.Categorical(df["weekday"], categories=sorter, ordered=True)

        # Sort the DataFrame by 'day_of_week'
        df.sort_values("weekday", inplace=True)
        return df
