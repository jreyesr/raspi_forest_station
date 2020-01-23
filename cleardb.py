#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

c.execute("DELETE FROM camera")
c.execute("DELETE FROM sensirion")
conn.commit()
