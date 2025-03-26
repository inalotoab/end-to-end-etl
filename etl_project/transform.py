# transform.py
def transform(df):
    df['Salary'] = df['Salary'] * 1.05  # Give a 5% salary increase
    df = df[df['Department'] != 'HR']  # Remove HR records as an example
    return df
