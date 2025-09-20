import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

if __name__ == "__main__":
    # Create
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id integer PRIMARY KEY autoincrement,
            name text,
            weight real)
        """
    )
    connection.commit()

    # Delete
    cursor.execute(
        f"""
        DELETE FROM {TABLE_NAME}
        """
    )
    connection.commit()

    # Delete sequence
    cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")

    # Insert
    cursor.execute(
        f"""
        INSERT INTO {TABLE_NAME} (id, name, weight)
        VALUES
            (NULL, 'Xonorhc', 99.9),
            (NULL, 'Chronox', 88.8)
        """
    )
    connection.commit()

    # Insert with placeholder
    sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)"
    cursor.execute(sql, ["Anachronox", 66.6])
    connection.commit()

    # Insert with many placeholders
    sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)"
    cursor.executemany(sql, (("Mary", 55.5), ("John", 111.1)))
    connection.commit()

    # Insert with many placeholders from dict
    sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)"
    cursor.executemany(
        sql,
        (
            {"name": "Saly", "weight": 44.4},
            {"name": "Steve", "weight": 77.7},
            {"name": "Jane", "weight": 33.3},
        ),
    )
    connection.commit()

    # Select
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    # Update
    cursor.execute(
        f"""
        UPDATE {TABLE_NAME}
        SET name = "Other name"
        WHERE id = '5'
        """
    )
    connection.commit()

    # Select
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()
