import json
import psycopg2

with open("config.json") as config_file:
    config = json.load(config_file)

def connect_to_db():
    conn = psycopg2.connect(
        host=config["host"],
        port=config["port"],
        dbname=config["dbname"],
        user=config["user"],
        password=config["password"]
    )
    print("connected")
    return conn

if __name__ == "__main__":
    connection = connect_to_db()
    connection.close()
