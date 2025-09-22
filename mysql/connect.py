import os

import dotenv
import pymysql

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT DATABASE();
            """
        )
        result = cursor.fetchall()
        print("\nSelect:\n")
        for row in result:
            print(row)
