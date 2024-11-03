import json
import psycopg2
import pandas as pd

with open("config.json") as config_file:
    config = json.load(config_file)

conn = psycopg2.connect(**config)
cursor = conn.cursor()

df = pd.read_csv("real_data.csv")

print(df.head())

df.dropna(subset=['value'], inplace=True)

df['value'] = pd.to_numeric(df['value'], errors='coerce')

cursor.executemany(
    """
    INSERT INTO test_data (year, industry_code_ANZSIC, industry_name_ANZSIC, rme_size_grp, variable, value, unit)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
    df[['year', 'industry_code_ANZSIC', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value', 'unit']].values.tolist()
)

conn.commit()
cursor.close()
conn.close()
print("All done, records inserted.")
