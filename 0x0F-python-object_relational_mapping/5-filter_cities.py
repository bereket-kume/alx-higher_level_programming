#!/usr/bin/python3
"""
Displays all cities of a given state from the states table
of the database hbtn_0e_4_usa. The script is safe from SQL injections.

Usage:
    ./5-filter_cities.py <mysql username> \
                         <mysql password> \
                         <database name> \
                         <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch all cities with their corresponding state
    # names
    cursor.execute("SELECT * FROM `cities` as `c` "
                   "INNER JOIN `states` as `s` "
                   "ON `c`.`state_id` = `s`.`id` "
                   "ORDER BY `c`.`id`")

    # Fetch and print all cities of the given state
    cities = cursor.fetchall()
    matching_cities = [city[2] for city in cities if city[4] == sys.argv[4]]
    print(", ".join(matching_cities))
