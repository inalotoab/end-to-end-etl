import pandas as pd

def extract(file_path):
    df = pd.read_csv(file_path)
    # Only get rows updated in the last 7 days
    df['LastUpdated'] = pd.to_datetime(df['LastUpdated'])
    recent_df = df[df['LastUpdated'] >= pd.Timestamp.today() - pd.Timedelta(days=7)]
    return recent_df
