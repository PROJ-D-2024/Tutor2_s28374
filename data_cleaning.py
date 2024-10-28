import pandas as pd
from sqlalchemy import create_engine
import json

with open("config.json") as config_file:
    config = json.load(config_file)

db_url = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}"
engine = create_engine(db_url)

df = pd.read_sql("SELECT * FROM test_data", engine)

df['score'] = df['score'].fillna(df['score'].mean())

df.drop_duplicates(inplace=True)

Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['score'] >= (Q1 - 1.5 * IQR)) & (df['score'] <= (Q3 + 1.5 * IQR))]

df['name'] = df['name'].astype('category')