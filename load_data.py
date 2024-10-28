import json
import psycopg2
import pandas as pd

with open("config.json") as config_file:
    config = json.load(config_file)

conn = psycopg2.connect(**config)
cursor = conn.cursor()

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [24, 27, 22],
    "score": [88.5, 92.3, 79.9]
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
print("all done")
