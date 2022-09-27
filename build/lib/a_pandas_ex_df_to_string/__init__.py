from typing import Union

import pandas as pd
from pandas.core.base import PandasObject


def ds_to_string(df: Union[pd.DataFrame, pd.Series]) -> Union[pd.Series, pd.DataFrame]:
    """
    Example:
    from random import choice
    csvtests = [
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_long.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_no2.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_no2_long.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_parameters.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_pm25_long.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_stations.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/baseball.csv",
    "https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv",
    ]
    csvfile = choice(csvtests)
    df = pd.read_csv(csvfile)
    print(df)
    print(df.dtypes)
    df2=df.ds_to_string()
    print(df2)
    print(df2.dtypes)

    """
    nastring = str(pd.NA)
    df2 = df.copy()
    if isinstance(df, pd.DataFrame):
        for col in df2.columns:
            if not df2[col].dtype == "string":
                try:
                    df2[col] = df2[col].fillna(nastring)
                except Exception:
                    pass
                df2[col] = df2[col].astype("string")
    else:
        try:
            df2 = df2.fillna(nastring)
        except Exception:
            pass
        df2 = df2.astype("string")
    df2 = df2.fillna(nastring).copy()
    return df2


def pd_add_to_string():
    PandasObject.ds_to_string = ds_to_string
