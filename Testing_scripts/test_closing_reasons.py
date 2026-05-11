from app import app, Escalation
from collections import Counter

with app.app_context():
    # Get actual data like the statistics function does
    all_escalations = Escalation.query.all()
    closed_escalations_with_reasons = [e for e in all_escalations if e.state == 'Closed' and e.closing_reason]
    closing_reason_counts = Counter([e.closing_reason for e in closed_escalations_with_reasons])
    
    print("Actual closing reasons from database:")
    for reason, count in closing_reason_counts.items():
        print(f"  {reason}: {count}")
    
    # Test our labels and data arrays
    closing_reason_labels = ['Bug', 'Network issue', 'Config issue', 'Infra issue', 'Serviceability issue', 'Location/AP/SDA', 'Routing', 'IOS-XE']
    closing_reason_data = [closing_reason_counts.get(label, 0) for label in closing_reason_labels]
    
    print(f"\nChart labels: {closing_reason_labels}")
    print(f"Chart data: {closing_reason_data}")
    
    # Show which ones have data
    print("\nCategories with data:")
    for i, (label, data) in enumerate(zip(closing_reason_labels, closing_reason_data)):
        if data > 0:
            print(f"  {label}: {data}")