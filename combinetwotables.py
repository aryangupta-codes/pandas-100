import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person, address, on='personId', how='left')
    return df[['firstName', 'lastName', 'city', 'state']]

if __name__ == "__main__":
    p_data = pd.DataFrame({
        'personId': [1, 2], 
        'lastName': ['Wang', 'Alice'], 
        'firstName': ['Allen', 'Bob']
    })
    a_data = pd.DataFrame({
        'addressId': [1, 2], 
        'personId': [2, 3], 
        'city': ['New York City', 'Leetcode'], 
        'state': ['New York', 'California']
    })
    
    print(combine_two_tables(p_data, a_data))