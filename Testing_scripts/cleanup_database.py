#!/usr/bin/env python3
"""
Database Cleanup Script for Escalation Management System
This script provides various options to clean up and standardize the database.
"""

from app import app, db, Escalation
import sys

def show_database_stats():
    """Display current database statistics"""
    with app.app_context():
        total = Escalation.query.count()
        print(f"\n=== DATABASE STATISTICS ===")
        print(f"Total escalations: {total}")
        
        # Check states
        states = db.session.query(Escalation.state).distinct().all()
        print(f"Distinct states: {[s[0] for s in states]}")
        
        # Check severity types
        severity_types = db.session.query(Escalation.severity_type).distinct().all()
        print(f"Distinct severity types: {[s[0] for s in severity_types if s[0]]}")
        
        # Show state distribution
        print("\nState distribution:")
        for state in states:
            count = Escalation.query.filter_by(state=state[0]).count()
            print(f"  {state[0]}: {count} records")
        
        # Show records with empty or null fields
        empty_customers = Escalation.query.filter((Escalation.customer == None) | (Escalation.customer == '')).count()
        empty_versions = Escalation.query.filter((Escalation.version == None) | (Escalation.version == '')).count()
        empty_engineers = Escalation.query.filter((Escalation.engineer == None) | (Escalation.engineer == '')).count()
        
        print(f"\nEmpty/null field counts:")
        print(f"  Empty customers: {empty_customers}")
        print(f"  Empty versions: {empty_versions}")
        print(f"  Empty engineers: {empty_engineers}")

def standardize_states():
    """Standardize state values (OPEN, Closed)"""
    with app.app_context():
        # Standardize state values
        # Convert 'Open' to 'OPEN'
        open_records = Escalation.query.filter_by(state='Open').all()
        print(f"Converting {len(open_records)} 'Open' records to 'OPEN'")
        
        for record in open_records:
            record.state = 'OPEN'
        
        db.session.commit()
        print("State standardization completed!")

def remove_demo_data():
    """Remove demo/test data"""
    with app.app_context():
        # Remove records with demo customers
        demo_records = Escalation.query.filter(
            Escalation.customer.like('%Demo%') | 
            Escalation.customer.like('%Test%') |
            Escalation.customer.like('%Sample%')
        ).all()
        
        print(f"Found {len(demo_records)} demo/test records")
        
        if demo_records:
            print("Demo records to be deleted:")
            for record in demo_records:
                print(f"  ID: {record.id}, Customer: {record.customer}")
            
            confirmation = input("Delete these demo records? (y/N): ")
            if confirmation.lower() == 'y':
                for record in demo_records:
                    db.session.delete(record)
                db.session.commit()
                print(f"Deleted {len(demo_records)} demo records!")
            else:
                print("Demo data deletion cancelled.")
        else:
            print("No demo records found.")

def clean_empty_records():
    """Remove records with critical empty fields"""
    with app.app_context():
        # Find records with empty critical fields
        empty_records = Escalation.query.filter(
            (Escalation.customer == None) | (Escalation.customer == '') |
            (Escalation.state == None) | (Escalation.state == '')
        ).all()
        
        print(f"Found {len(empty_records)} records with empty critical fields")
        
        if empty_records:
            print("Records with empty critical fields:")
            for record in empty_records:
                print(f"  ID: {record.id}, Customer: '{record.customer}', State: '{record.state}'")
            
            confirmation = input("Delete these incomplete records? (y/N): ")
            if confirmation.lower() == 'y':
                for record in empty_records:
                    db.session.delete(record)
                db.session.commit()
                print(f"Deleted {len(empty_records)} incomplete records!")
            else:
                print("Empty records deletion cancelled.")
        else:
            print("No records with empty critical fields found.")

def remove_duplicate_records():
    """Remove duplicate records based on customer and version"""
    with app.app_context():
        # Find potential duplicates
        all_records = Escalation.query.all()
        seen = set()
        duplicates = []
        
        for record in all_records:
            key = (record.customer, record.version, record.bugid)
            if key in seen:
                duplicates.append(record)
            else:
                seen.add(key)
        
        print(f"Found {len(duplicates)} potential duplicate records")
        
        if duplicates:
            print("Potential duplicate records:")
            for record in duplicates:
                print(f"  ID: {record.id}, Customer: {record.customer}, Version: {record.version}, Bug ID: {record.bugid}")
            
            confirmation = input("Delete these duplicate records? (y/N): ")
            if confirmation.lower() == 'y':
                for record in duplicates:
                    db.session.delete(record)
                db.session.commit()
                print(f"Deleted {len(duplicates)} duplicate records!")
            else:
                print("Duplicate deletion cancelled.")
        else:
            print("No duplicate records found.")

def complete_wipe():
    """Completely wipe all data from the database"""
    with app.app_context():
        total = Escalation.query.count()
        print(f"WARNING: This will delete ALL {total} records from the database!")
        print("This action cannot be undone!")
        
        confirmation1 = input("Are you sure you want to delete ALL data? (yes/no): ")
        if confirmation1.lower() == 'yes':
            confirmation2 = input("Type 'DELETE ALL' to confirm: ")
            if confirmation2 == 'DELETE ALL':
                Escalation.query.delete()
                db.session.commit()
                print("All data has been deleted from the database!")
            else:
                print("Complete wipe cancelled.")
        else:
            print("Complete wipe cancelled.")

def backup_database():
    """Create a backup of current data"""
    import json
    from datetime import datetime
    
    with app.app_context():
        all_records = Escalation.query.all()
        backup_data = []
        
        for record in all_records:
            backup_data.append({
                'id': record.id,
                'customer': record.customer,
                'version': record.version,
                'bugid': record.bugid,
                'state': record.state,
                'severity_type': record.severity_type,
                'engineer': record.engineer,
                'director': record.director,
                'dedt_manager': record.dedt_manager,
                'pending_action': record.pending_action,
                'reported_on': record.reported_on.isoformat() if record.reported_on else None,
                'closed_on': record.closed_on.isoformat() if record.closed_on else None,
                'updated_on': record.updated_on.isoformat() if record.updated_on else None,
                'closing_reason': record.closing_reason,
                'closing_remarks': record.closing_remarks,
                'description': record.description,
                'component_name': record.component_name,
                'contributors': record.contributors,
                'sr': record.sr,
                'bems': record.bems,
                'severity_text': record.severity_text
            })
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"database_backup_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(backup_data, f, indent=2, default=str)
        
        print(f"Database backup created: {filename}")
        print(f"Backed up {len(backup_data)} records")

def main():
    print("=== ESCALATION DATABASE CLEANUP TOOL ===")
    print("\nAvailable operations:")
    print("1. Show database statistics")
    print("2. Standardize state values (Open -> OPEN)")
    print("3. Remove demo/test data")
    print("4. Clean empty/incomplete records")
    print("5. Remove duplicate records")
    print("6. Create database backup")
    print("7. COMPLETE WIPE (delete all data)")
    print("0. Exit")
    
    while True:
        try:
            choice = input("\nSelect operation (0-7): ").strip()
            
            if choice == '0':
                print("Exiting...")
                break
            elif choice == '1':
                show_database_stats()
            elif choice == '2':
                standardize_states()
            elif choice == '3':
                remove_demo_data()
            elif choice == '4':
                clean_empty_records()
            elif choice == '5':
                remove_duplicate_records()
            elif choice == '6':
                backup_database()
            elif choice == '7':
                complete_wipe()
            else:
                print("Invalid choice. Please select 0-7.")
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()