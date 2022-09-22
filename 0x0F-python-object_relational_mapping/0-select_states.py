#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa '''

import MySQLdb
import sys
if __name__ == "__main__":
    db_con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
    cur = db_con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db_con.close()