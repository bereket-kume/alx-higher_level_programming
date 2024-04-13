#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, ordered by city ID.

Usage:
    ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch all cities with their corresponding state
    # names
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` "
                   "FROM `cities` as `c` "
                   "INNER JOIN `states` as `s` "
                   "ON `c`.`state_id` = `s`.`id` "
                   "ORDER BY `c`.`id`")

    # Fetch and print all cities
    cities = cursor.fetchall()
    [print(city) for city in cities]
