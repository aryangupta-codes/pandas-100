import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if N <= 0 or N > len(unique_salaries):
        res = None
    else:
        res = unique_salaries.iloc[N - 1]
        
    return pd.DataFrame({f'getNthHighestSalary({N})': [res]})

if __name__ == "__main__":
    data = {'id': [1, 2, 3], 'salary': [100, 200, 300]}
    df = pd.DataFrame(data)
    print(nth_highest_salary(df, 2))