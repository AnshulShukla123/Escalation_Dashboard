import sqlite3

conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

cursor.execute("SELECT id, customer, severity_type FROM escalation WHERE severity_type IS NOT NULL AND severity_type != ''")
records = cursor.fetchall()

print('Records with severity_type:')
for row in records:
    print(f'ID: {row[0]}, Customer: {row[1]}, Severity Type: {row[2]}')

conn.close()