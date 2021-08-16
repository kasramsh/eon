import pandas as pd
from utils import plz_normalizer, remove_bundes_nans, remove_conflicts


def load_clean_data(csv_path: str) -> pd.DataFrame:

    data = pd.read_csv(
        csv_path,
        low_memory=False,
        parse_dates=["order_date"],
        date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d"),
    )
    data = remove_bundes_nans(data)
    data["postcode"] = data.postcode.apply(lambda x: plz_normalizer(x))
    data["original_product_name"] = data.original_product_name.apply(
        lambda x: "E.ON STROM 24" if "E.ON STROM 24" in x else x
    )
    data = remove_conflicts(data, "postcode", "bundesland")
    data = data.reset_index(drop=True)

    return data
