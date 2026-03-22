import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    second_highest = unique_salaries.iloc[1]
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})

if __name__ == "__main__":
    data = {'id': [1, 2, 3], 'salary': [100, 200, 300]}
    df = pd.DataFrame(data)
    print(second_highest_salary(df))