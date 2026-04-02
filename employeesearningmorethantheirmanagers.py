import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        employee, 
        left_on='managerId', 
        right_on='id', 
        suffixes=('', '_manager')
    )
    
    result = df[df['salary'] > df['salary_manager']][['name']]
    
    return result.rename(columns={'name': 'Employee'})

data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}

employee_df = pd.DataFrame(data)
print(find_employees(employee_df))