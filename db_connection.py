import json
import psycopg2
import pandas as pd

with open("config.json") as config_file:
    config = json.load(config_file)

conn = psycopg2.connect(**config)
cursor = conn.cursor()

df = pd.read_csv("real_data.csv")

cursor.executemany(
    "INSERT INTO test_data (year, industry_name, value, variable) VALUES (%s, %s, %s, %s)",
    df[['year', 'industry_name_ANZSIC', 'value', 'variable']].values.tolist()
)

conn.commit()
cursor.close()
conn.close()
print("All done, records inserted.")
