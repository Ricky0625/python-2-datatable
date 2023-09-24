import pandas as pd


def load(path: str) -> pd.DataFrame:

    """
    Load csv file and return as data frame
    """

    try:
        if not isinstance(path, str):
            raise AssertionError("expect path to be a string")

        dataframe = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataframe.shape}")
        return dataframe
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
