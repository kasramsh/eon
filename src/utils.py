import pandas as pd
from typing import Union


def plz_normalizer(plz: Union[int, float, str]) -> str:
    """
    Normalizes PLZ values to a proper string

    Parameters
    ----------
    plz : {str, int, float}
        Geographical postal code

    Returns
    -------
    string
        Normalized postal code

    Raises
    ------
    KeyError
        when a key error
    OtherError
        when an other error
    """
    plz = str(int(float(plz)))
    if len(plz) == 4:
        return "0" + plz
    else:
        return plz


def remove_nans(data: pd.DataFrame, col: str) -> pd.DataFrame:
    return data[~data[col].isna()]


def remove_conflicts(data: pd.DataFrame, col1: str, col2: str) -> pd.DataFrame:
    conflicts = (
        data.groupby(col1)
        .filter(lambda g: (g[col2].nunique() > 1))
        .drop_duplicates([col1, col2])
    )
    return data[~data[col1].isin(conflicts[col1].unique().tolist())]
