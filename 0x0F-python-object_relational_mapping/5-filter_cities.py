#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = username,
        passwd = password,
        db = database
    )

    cursor = connection.cursor()
    query = """
             SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
             FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name = %s
             ORDER BY cities.id ASC
            """
    
cursor.execute(query ,(state_name,))
result = cursor.fetchone()
if result:
    print(result[0])
else:
    print("No cities found for the state {}".format(state_name))

cursor.close()
connection.close()