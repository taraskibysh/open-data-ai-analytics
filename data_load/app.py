
import os
import time
import pandas as pd
from sqlalchemy import create_engine, text


def wait_for_db(engine, retries=30, delay=2):
    for attempt in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("[data_load] DB is available!")
            return True
        except Exception as e:
            print(f"[data_load] Attempt {attempt + 1}/{retries}: DB is not ready yet — {e}")
            time.sleep(delay)
    raise ConnectionError("[data_load] Failed to connect to the DB.")


def main():
    db_host = os.environ.get("MYSQL_HOST", "db")
    db_user = os.environ.get("MYSQL_USER", "appuser")
    db_password = os.environ.get("MYSQL_PASSWORD", "apppassword")
    db_name = os.environ.get("MYSQL_DATABASE", "docflow")

    csv_path = "/data/dataset.csv"

    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}"
    engine = create_engine(connection_string)

    wait_for_db(engine)

    # Load CSV
    print(f"[data_load] Reading data from {csv_path}...")
    df = pd.read_csv(csv_path, encoding="utf-8")
    print(f"[data_load] Read {len(df)} rows, {len(df.columns)} columns.")
    print(f"[data_load] Columns: {list(df.columns)}")

    # Normalize column names — remove possible line breaks
    df.columns = [col.replace("\n", "_").replace("\r", "") for col in df.columns]
    print(f"[data_load] Normalized columns: {list(df.columns)}")

    # Write to DB (replace table if it exists)
    table_name = "documents"
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"[data_load] Data successfully loaded into table '{table_name}'.")

    # Verification
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        count = result.scalar()
        print(f"[data_load] Verification: {count} records in table '{table_name}'.")

    print("[data_load] Completed successfully!")


if __name__ == "__main__":
    main()
