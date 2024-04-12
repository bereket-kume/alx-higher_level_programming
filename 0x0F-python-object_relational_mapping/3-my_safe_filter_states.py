#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stat_name =  sys.argv[4]

    connection = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = username,
        passwd = password,
        db = database
    )

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(query, (stat_name,))
    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    connection.close()