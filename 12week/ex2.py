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

cusor.execute('SELECT * FROM city')
results = cusor.fetchall()
for row in results:
    print(row)

df = pd.DataFrame(results)
print(df.head(10), end="\n\n")

conn.close()