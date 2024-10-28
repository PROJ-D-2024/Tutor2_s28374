import json
import psycopg2
import pandas as pd
from faker import Faker

with open("config.json") as config_file:
    config = json.load(config_file)

conn = psycopg2.connect(**config)
cursor = conn.cursor()

fake = Faker()

data = {
    "name": [fake.name() for _ in range(5000)],
    "age": [fake.random_int(min=18, max=70) for _ in range(5000)],
    "score": [round(fake.random_number(digits=2) + fake.random.random(), 2) for _ in range(5000)]
}

df = pd.DataFrame(data)

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO test_data (name, age, score) VALUES (%s, %s, %s)",
        (row["name"], row["age"], row["score"])
    )

conn.commit()
cursor.close()
conn.close()
print("All done, 5000 records inserted.")
