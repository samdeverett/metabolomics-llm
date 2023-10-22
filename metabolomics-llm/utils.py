import pandas as pd

def get_works_from_years(start_year: int, end_year: int) -> pd.DataFrame:
    dfs = []
    for year in range(start_year, end_year + 1):
        dfs.append(pd.read_parquet(f"data/{year}.parquet"))
    df = pd.concat(dfs)
    return df
