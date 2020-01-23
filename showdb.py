#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

for row in c.execute("SELECT ROWID, timestamp, temp, humid FROM sensirion"):
    print(row)
for row in c.execute("SELECT ROWID, timestamp, filename FROM camera"):
    print(row)
