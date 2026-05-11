from app import app, db, Escalation
from datetime import datetime, timedelta
from collections import Counter

with app.app_context():
    escalations = Escalation.query.all()
    print('Real escalation data from dashboard:')
    for e in escalations:
        print(f'ID: {e.id}, DE Manager: {getattr(e, "de_manager", "N/A")}, Primary POC: {getattr(e, "primary_poc", "N/A")}, Contributors: {getattr(e, "contributors", "N/A")}, Date: {e.reported_on}')
    
    print('\nChecking all fields in first escalation:')
    if escalations:
        first_escalation = escalations[0]
        for attr in dir(first_escalation):
            if not attr.startswith('_'):
                value = getattr(first_escalation, attr)
                if not callable(value):
                    print(f'{attr}: {value}')