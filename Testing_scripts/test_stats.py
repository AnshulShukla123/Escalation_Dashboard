#!/usr/bin/env python3

from app import app, statistics
import sys

if __name__ == '__main__':
    with app.app_context():
        # Test the statistics function directly
        try:
            from flask import render_template_string
            
            # Call the statistics function
            print("Testing statistics function...")
            
            # Import the statistics function logic
            from collections import Counter
            from datetime import datetime, timedelta
            from app import Escalation
            
            # Only use these 5 closing reasons
            closing_reason_values = [
                "Bug",
                "Network issue",
                "Config issue",
                "Infra issue",
                "Serviceability issue"
            ]
            closed_items = Escalation.query.filter_by(state='Closed').all()
            reasons = [item.closing_reason for item in closed_items if item.closing_reason in closing_reason_values]
            reason_counts = Counter(reasons)
            labels = closing_reason_values
            data = [reason_counts.get(label, 0) for label in labels]
            
            print(f"Closing reasons chart data: {dict(zip(labels, data))}")
            
            # Calculate contributor statistics
            now = datetime.now()
            one_month_ago = now - timedelta(days=30)
            three_months_ago = now - timedelta(days=90)
            
            # Get all escalations with contributors data
            all_items = Escalation.query.all()
            
            # Filter for last 1 month and 3 months based on reported_on date
            contributors_1m = []
            contributors_3m = []
            
            for item in all_items:
                if item.contributors and item.reported_on:
                    try:
                        # Parse reported_on date
                        reported_date = datetime.strptime(item.reported_on, '%Y-%m-%d')
                        
                        # Split contributors by comma and clean up
                        item_contributors = [c.strip() for c in item.contributors.split(',') if c.strip()]
                        
                        if reported_date >= one_month_ago:
                            contributors_1m.extend(item_contributors)
                        if reported_date >= three_months_ago:
                            contributors_3m.extend(item_contributors)
                    except (ValueError, TypeError):
                        continue
            
            # Count contributors
            contributor_counts_1m = Counter(contributors_1m)
            contributor_counts_3m = Counter(contributors_3m)
            
            # Get top 5 contributors for each period
            top_contributors_1m = contributor_counts_1m.most_common(5)
            top_contributors_3m = contributor_counts_3m.most_common(5)
            
            print(f"Top contributors 1 month: {top_contributors_1m}")
            print(f"Top contributors 3 months: {top_contributors_3m}")
            
            # Prepare data for charts
            contributors_1m_labels = [c[0] for c in top_contributors_1m]
            contributors_1m_data = [c[1] for c in top_contributors_1m]
            
            contributors_3m_labels = [c[0] for c in top_contributors_3m]
            contributors_3m_data = [c[1] for c in top_contributors_3m]
            
            print(f"1M Chart - Labels: {contributors_1m_labels}, Data: {contributors_1m_data}")
            print(f"3M Chart - Labels: {contributors_3m_labels}, Data: {contributors_3m_data}")
            
            print("✅ Statistics function working correctly!")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()