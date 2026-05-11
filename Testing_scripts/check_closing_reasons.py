import sqlite3

conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

cursor.execute("SELECT closing_reason, COUNT(*) FROM escalation WHERE state = 'Closed' AND closing_reason IS NOT NULL GROUP BY closing_reason")
results = cursor.fetchall()
print('Closing reason counts:')
for row in results:
    print(f'  {row[0]}: {row[1]}')

conn.close()