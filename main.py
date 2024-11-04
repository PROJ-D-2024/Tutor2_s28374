from scripts.data_cleaning import load_and_clean_data
from scripts.data_standardization import standardize_data
from scripts.database_update import update_database

df = load_and_clean_data("real_data.csv")
print("Данные загружены и очищены.")

df = standardize_data(df)
print("Данные стандартизированы.")

update_database(df)
print("Данные обновлены в базе данных.")
