#!/usr/bin/python3
'''a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.'''

import MySQLdb
import sys

if __name__ == "__main__":
    db_con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
    curr = db_con.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    states = curr.fetchall()
    print(states[0])
    # for state in states:
    #     print(state)
    curr.close()
    db_con.close()