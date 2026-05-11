import sqlite3

# Check all records for any actual severity data
conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

cursor.execute('SELECT id, severity, severity_text FROM escalation')
rows = cursor.fetchall()

print(f'Total records: {len(rows)}')
print('\nRecords with severity data:')
for row in rows:
    if row[1] != 'None' and row[1] is not None:
        print(f'ID: {row[0]}, Severity: "{row[1]}", Severity_text: "{row[2]}"')
        
print('\nRecords with severity_text data:')
for row in rows:
    if row[2] != 'None' and row[2] is not None:
        print(f'ID: {row[0]}, Severity: "{row[1]}", Severity_text: "{row[2]}"')

conn.close()