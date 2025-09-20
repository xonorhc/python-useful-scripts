import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = "customers"

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:

    # Create table
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(50) NOT NULL,
                age int NOT NULL,
                PRIMARY KEY (id))
            """
        )
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()

    # Truncate table
    with connection.cursor() as cursor:
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()

    # Insert
    with connection.cursor() as cursor:
        result = cursor.execute(
            f"""
            INSERT INTO {TABLE_NAME} (name, age)
                VALUES ('Mary', 20)
            """
        )
    connection.commit()

    # Insert with placeholder
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)"
        result = cursor.execute(sql, ("John", 30))

    # Insert with many placeholders
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s)"
        data = (
            {"name": "Chronox", "age": 33},
            {"name": "Xonorhc", "age": 44},
            {"name": "Anachronox", "age": 22},
        )
        cursor.executemany(sql, data)
    connection.commit()

    # Select
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT id, name, age
                FROM {TABLE_NAME}
                ORDER BY id DESC
            """
        )
        result = cursor.fetchall()
        print("\nSelect:\n")
        for row in result:
            print(row)
    connection.commit()

    # Delete with placeholder
    with connection.cursor() as cursor:
        sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
        cursor.execute(sql, (1,))
    connection.commit()

    # Update with palceholder
    with connection.cursor() as cursor:
        sql = f"UPDATE {TABLE_NAME} SET name = %s, age = %s WHERE id = %s"
        cursor.execute(
            sql,
            (
                "OTHER",
                100,
                3,
            ),
        )

    # Cursor
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT id, name, age FROM {TABLE_NAME}")

        print("\nFor 1:\n")
        for row in cursor.fetchall():
            print(row)

        print("\nFor 2:\n")
        cursor.scroll(0, "absolute")
        for row in cursor.fetchall():
            print(row)
        connection.commit()
