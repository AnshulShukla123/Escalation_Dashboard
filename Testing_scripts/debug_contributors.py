from app import app, Escalation, db
from datetime import datetime, timedelta
from collections import Counter

with app.app_context():
    all_escalations = Escalation.query.all()
    print('Total escalations:', len(all_escalations))
    
    # Debug individual escalations
    for e in all_escalations:
        print(f'ID {e.id}: contributors="{e.contributors}", date={e.reported_on}')
    
    # Check date filtering
    now = datetime.now()
    one_month_ago = now - timedelta(days=30)
    three_months_ago = now - timedelta(days=90)
    print(f'Current date: {now.strftime("%Y-%m-%d")}')
    print(f'One month ago: {one_month_ago.strftime("%Y-%m-%d")}')
    print(f'Three months ago: {three_months_ago.strftime("%Y-%m-%d")}')
    
    # Manual calculation for 1 month
    contributors_1m = []
    for item in all_escalations:
        if item.contributors and item.reported_on:
            try:
                reported_date = datetime.strptime(item.reported_on, '%Y-%m-%d')
                if reported_date >= one_month_ago:
                    item_contributors = [c.strip() for c in item.contributors.split(',') if c.strip()]
                    contributors_1m.extend(item_contributors)
                    print(f'Adding contributors from {item.reported_on}: {item_contributors}')
            except Exception as e:
                print(f'Error processing escalation {item.id}: {e}')
    
    # Manual calculation for 3 months
    contributors_3m = []
    for item in all_escalations:
        if item.contributors and item.reported_on:
            try:
                reported_date = datetime.strptime(item.reported_on, '%Y-%m-%d')
                if reported_date >= three_months_ago:
                    item_contributors = [c.strip() for c in item.contributors.split(',') if c.strip()]
                    contributors_3m.extend(item_contributors)
            except Exception as e:
                print(f'Error processing escalation {item.id}: {e}')
    
    contributor_counts_1m = Counter(contributors_1m)
    contributor_counts_3m = Counter(contributors_3m)
    
    print('1 Month contributor counts:', contributor_counts_1m.most_common(5))
    print('3 Month contributor counts:', contributor_counts_3m.most_common(5))
    
    # Check what the statistics route would return
    contributor_stats_1_month = contributor_counts_1m.most_common(5)
    contributor_stats_3_months = contributor_counts_3m.most_common(5)
    
    print('Stats for template (1M):', contributor_stats_1_month)
    print('Stats for template (3M):', contributor_stats_3_months)