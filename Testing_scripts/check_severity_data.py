import sqlite3

# Check sample records for severity data
conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

cursor.execute('SELECT id, severity, severity_text FROM escalation LIMIT 5')
rows = cursor.fetchall()

print('Sample records:')
for row in rows:
    print(f'ID: {row[0]}, Severity: "{row[1]}", Severity_text: "{row[2]}"')

conn.close()