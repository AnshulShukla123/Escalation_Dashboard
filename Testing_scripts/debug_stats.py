#!/usr/bin/env python3

from app import app, db, Escalation
from collections import Counter

with app.app_context():
    # Get all escalations for basic statistics
    all_escalations = Escalation.query.all()
    
    print("=== DEBUG STATISTICS DATA ===")
    print(f"Total escalations found: {len(all_escalations)}")
    
    print("\nEscalation details:")
    for e in all_escalations:
        print(f"  ID: {e.id}")
        print(f"    Customer: {e.customer}")
        print(f"    State: '{e.state}' (type: {type(e.state)})")
        print(f"    Severity Type: '{e.severity_type}'")
        print(f"    Reported On: {e.reported_on}")
        print(f"    Closed On: {getattr(e, 'closed_on', 'None')}")
        print()
    
    # Test state calculations
    open_escalations = len([e for e in all_escalations if e.state and e.state.upper() == 'OPEN'])
    closed_escalations = len([e for e in all_escalations if e.state and e.state.upper() == 'CLOSED'])
    
    print(f"Open escalations (using upper()): {open_escalations}")
    print(f"Closed escalations (using upper()): {closed_escalations}")
    
    # Test severity type counts
    severity_counts = Counter([e.severity_type for e in all_escalations if e.severity_type])
    print(f"Severity type counts: {dict(severity_counts)}")
    
    print("=== END DEBUG ===")