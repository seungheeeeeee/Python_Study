import pandas as pd
import mariadb

conn = mariadb.connect(
    user="user025",
    password="!ai123",
    host="edu.ithows.com",
    port=53306,
    database="edudb"
)
cusor = conn.cursor()

cusor.execute('INSERT INTO user025 (userId, userPassword) VALUES ("Song", "!ai123");')
cusor.execute('DELETE FROM user025 WHERE userId = "Kim";')



conn.commit()
conn.close()