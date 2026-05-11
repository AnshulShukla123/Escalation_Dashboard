import sqlite3

# Add severity_text column to the database
conn = sqlite3.connect('instance/escalations.db')
cursor = conn.cursor()

try:
    # Add the new column
    cursor.execute("ALTER TABLE escalation ADD COLUMN severity_text TEXT")
    print("✅ Successfully added severity_text column to the database")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("⚠️ Column severity_text already exists")
    else:
        print(f"❌ Error adding column: {e}")

# Verify the column was added
cursor.execute("PRAGMA table_info(escalation)")
columns = cursor.fetchall()
print("\nUpdated table columns:")
for col in columns:
    print(f"  {col[1]} ({col[2]})")

conn.commit()
conn.close()