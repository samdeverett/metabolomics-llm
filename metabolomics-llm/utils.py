import pandas as pd


def get_works_from_years(start_year: int, end_year: int) -> pd.DataFrame:
    """Returns DataFrame with all the papers in the `data` folder for the given range of years.
    
    Args:
        start_year: Earliest year from which to pull papers.
        end_year: The latest year from which to pull papers.
    """
    dfs = []
    for year in range(start_year, end_year + 1):
        dfs.append(pd.read_parquet(f"data/{year}.parquet"))
    df = pd.concat(dfs)
    return df
