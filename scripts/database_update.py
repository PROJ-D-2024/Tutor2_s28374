import json
import psycopg2


def update_database(df):
    with open("config.json") as config_file:
        config = json.load(config_file)

    conn = psycopg2.connect(**config)
    cursor = conn.cursor()

    try:
        cursor.executemany(
            """
            INSERT INTO test_data (year, industry_code_ANZSIC, industry_name_ANZSIC, rme_size_grp, variable, value, unit)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            df[['year', 'industry_code_ANZSIC', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value',
                'unit']].values.tolist()
        )
        conn.commit()
    except Exception as e:
        print("Ошибка при обновлении базы данных:", e)
    finally:
        cursor.close()
        conn.close()
