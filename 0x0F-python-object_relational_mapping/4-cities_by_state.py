#!/usr/bin/python3
'''a script that lists all cities from the database hbtn_0e_4_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3],
                             charset="utf8")
    curr = db_con.cursor()
    curr.execute("SELECT cities.id , cities.name, states.name FROM \
        cities JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    cities = curr.fetchall()
    for city in cities:
        print(city)
