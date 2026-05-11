import sqlite3

conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

# Add some sample closed escalations with the new closing reasons
cursor.execute("UPDATE escalation SET closing_reason = 'Location/AP/SDA', state = 'Closed' WHERE id = 10")
cursor.execute("UPDATE escalation SET closing_reason = 'Routing', state = 'Closed' WHERE id = 15") 
cursor.execute("UPDATE escalation SET closing_reason = 'IOS-XE', state = 'Closed' WHERE id = 20")

conn.commit()
print('Added sample data for new closing reasons')

# Verify the changes
cursor.execute("SELECT id, closing_reason, state FROM escalation WHERE closing_reason IN ('Location/AP/SDA', 'Routing', 'IOS-XE')")
results = cursor.fetchall()
print('Updated escalations:')
for row in results:
    print(f'  ID {row[0]}: {row[1]} ({row[2]})')

conn.close()