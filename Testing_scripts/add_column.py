import sqlite3

conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()
try:
    cursor.execute("ALTER TABLE escalation ADD COLUMN remarks_value TEXT;")
    print("Column added successfully.")
except Exception as e:
    print("Error:", e)
conn.commit()
conn.close()