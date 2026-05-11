import sys
sys.path.insert(0, '.')
from app import app, db, Escalation

with app.app_context():
    all_escalations = Escalation.query.all()
    print('All escalations contributor data:')
    for item in all_escalations:
        contributor_val = item.contributors if item.contributors else 'EMPTY'
        print(f'  ID {item.id}: contributors="{contributor_val}" reported_on="{item.reported_on}"')
    
    # Let's add some sample contributor data to test
    if all_escalations:
        # Update first few escalations with sample contributor data
        escalations_to_update = all_escalations[:3]
        sample_contributors = [
            'John Doe, Jane Smith',
            'Alice Johnson, Bob Wilson, Charlie Brown',
            'David Lee, Emma Taylor'
        ]
        
        for i, escalation in enumerate(escalations_to_update):
            if i < len(sample_contributors):
                escalation.contributors = sample_contributors[i]
                print(f'Updated ID {escalation.id} with contributors: "{sample_contributors[i]}"')
        
        db.session.commit()
        print('\nSample contributor data added to database!')
    else:
        print('No escalations found in database')