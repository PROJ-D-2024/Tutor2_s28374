import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(subset=['value'], inplace=True)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    return df
