#!/usr/bin/env python3
"""
Database migration script to remove the 'functionality' column from the escalation table.
Run this script to update your existing database.
"""

import sqlite3
import os
from datetime import datetime

def backup_database():
    """Create a backup of the database before migration."""
    db_path = 'instance/database.db'
    if os.path.exists(db_path):
        backup_path = f'instance/database_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db'
        import shutil
        shutil.copy2(db_path, backup_path)
        print(f"✅ Database backed up to: {backup_path}")
        return backup_path
    else:
        print("❌ Database file not found at instance/database.db")
        return None

def remove_functionality_column():
    """Remove the functionality column from the escalation table."""
    db_path = 'instance/database.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found. Please make sure the Flask app has been run at least once.")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if functionality column exists
        cursor.execute("PRAGMA table_info(escalation)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        
        if 'functionality' not in column_names:
            print("✅ Functionality column already removed or doesn't exist.")
            conn.close()
            return True
        
        print("🔄 Removing functionality column...")
        
        # SQLite doesn't support DROP COLUMN directly, so we need to recreate the table
        # First, get the table schema without the functionality column
        cursor.execute("""
            CREATE TABLE escalation_new AS 
            SELECT id, customer, version, engineer, state, closing_reason, component, 
                   dedt_manager, cross_team, director, reported_on, closed_on, 
                   closing_remarks, reopen_reason, senior_leaders, mgmt_escalation, 
                   severity, urgency, sr, bems, upgrade_attempt, symptom, next_step, 
                   director2, escalation_manager, escalation_engineer, remarks, 
                   remarks_value, escalation_person, director_dedt, engineering_mgr, 
                   consulting_engineer, consulting_manager, ad_manager, escalation_state, 
                   sjc_version, sjc_component, sjc_director, sjc_de_manager, sjc_engineer
            FROM escalation
        """)
        
        # Drop the old table
        cursor.execute("DROP TABLE escalation")
        
        # Rename the new table
        cursor.execute("ALTER TABLE escalation_new RENAME TO escalation")
        
        # Recreate the table with proper constraints and indexes if needed
        # Note: You might need to add back any indexes or constraints that were on the original table
        
        conn.commit()
        conn.close()
        
        print("✅ Successfully removed functionality column from escalation table.")
        return True
        
    except Exception as e:
        print(f"❌ Error removing functionality column: {str(e)}")
        return False

def main():
    print("🗄️  Starting database migration to remove 'functionality' column...")
    print("=" * 60)
    
    # Backup database first
    backup_path = backup_database()
    if not backup_path and os.path.exists('instance/database.db'):
        response = input("⚠️  Could not create backup. Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("❌ Migration cancelled.")
            return
    
    # Remove functionality column
    success = remove_functionality_column()
    
    if success:
        print("=" * 60)
        print("✅ Migration completed successfully!")
        print("📋 Summary of changes:")
        print("   - Removed 'functionality' column from escalation table")
        print("   - Updated database schema")
        if backup_path:
            print(f"   - Database backup saved at: {backup_path}")
        print("\n🚀 You can now restart your Flask application.")
    else:
        print("❌ Migration failed. Please check the error messages above.")
        if backup_path:
            print(f"💾 You can restore from backup: {backup_path}")

if __name__ == "__main__":
    main()