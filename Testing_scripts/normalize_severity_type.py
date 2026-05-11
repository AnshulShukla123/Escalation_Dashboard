import sqlite3

# Normalize severity_type values in the database
conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

# Update 'Cap' to 'CAP'
cursor.execute("UPDATE escalation SET severity_type = 'CAP' WHERE severity_type = 'Cap'")
cap_updates = cursor.rowcount

# Update 'Pre-CAP' to 'pre-CAP'  
cursor.execute("UPDATE escalation SET severity_type = 'pre-CAP' WHERE severity_type = 'Pre-CAP'")
pre_cap_updates = cursor.rowcount

conn.commit()

print(f"Updated {cap_updates} records from 'Cap' to 'CAP'")
print(f"Updated {pre_cap_updates} records from 'Pre-CAP' to 'pre-CAP'")

# Verify the changes
cursor.execute("SELECT DISTINCT severity_type FROM escalation WHERE severity_type IS NOT NULL AND severity_type != ''")
print("Current severity_type values after normalization:", cursor.fetchall())

conn.close()
print("Database normalization completed!")