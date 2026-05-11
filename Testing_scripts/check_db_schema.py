import sqlite3

# Check the database schema
conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

# Get table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", tables)

# Get column info for escalation table
cursor.execute("PRAGMA table_info(escalation)")
columns = cursor.fetchall()
print("\nEscalation table columns:")
for col in columns:
    print(f"  {col[1]} ({col[2]})")

conn.close()