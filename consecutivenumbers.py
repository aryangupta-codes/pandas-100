import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # 1. We need to handle cases where there are fewer than 3 rows
    if logs.shape[0] < 3:
        return pd.DataFrame({'ConsecutiveNums': []})

    # 2. Compare the 'num' column with the next two rows using .shift()
    # shift(-1) looks at the next row, shift(-2) looks at the one after that
    is_consecutive = (
        (logs['num'] == logs['num'].shift(-1)) & 
        (logs['num'] == logs['num'].shift(-2))
    )
    
    # 3. Filter the dataframe and get unique values
    consecutive_values = logs.loc[is_consecutive, 'num'].unique()
    
    # 4. Return as a new DataFrame with the required column name
    return pd.DataFrame({'ConsecutiveNums': consecutive_values})

# Example usage (to test it in your terminal):
data = {'id': [1, 2, 3, 4, 5, 6, 7], 'num': [1, 1, 1, 2, 1, 2, 2]}
df = pd.DataFrame(data)
print(consecutive_numbers(df))