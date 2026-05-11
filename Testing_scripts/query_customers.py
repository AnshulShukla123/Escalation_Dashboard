#!/usr/bin/env python3
"""
Customer Escalation Analysis Script
Runs the SQL query to show actual customers from the escalation database
"""

import sys
sys.path.append('.')

from app import app, Escalation, db
from collections import Counter

def main():
    # Connect to the database and analyze customers
    with app.app_context():
        print('=== CUSTOMER ESCALATION ANALYSIS ===')
        print()
        
        # Get all escalations
        all_escalations = Escalation.query.all()
        
        # Extract customers and count them
        customers = [e.customer for e in all_escalations if e.customer and e.customer.strip()]
        customer_counts = Counter(customers)
        
        print(f'Total escalations in database: {len(all_escalations)}')
        print(f'Escalations with customer data: {len(customers)}')
        print(f'Unique customers: {len(customer_counts)}')
        print()
        
        if customer_counts:
            print('Customer Name'.ljust(35) + 'Escalation Count')
            print('-' * 50)
            
            # Sort by count (descending)
            for customer, count in customer_counts.most_common():
                print(f'{customer:<35} {count}')
            
            print()
            print('=== TOP 3 CUSTOMERS (used in AI insights) ===')
            top_3 = customer_counts.most_common(3)
            for i, (customer, count) in enumerate(top_3, 1):
                print(f'{i}. {customer} - {count} escalations')
                
            print()
            print('=== AI INSIGHTS EXPLANATION ===')
            print('The customers mentioned in the AI insights come from this actual data.')
            print('The AI analyzes the top customers by escalation count to provide')
            print('meaningful recommendations for prioritizing support efforts.')
        else:
            print('No customer data found in escalations.')
            
        print()
        print('=== SAMPLE ESCALATION DATA ===')
        print('Customer'.ljust(25) + 'Component'.ljust(20) + 'State'.ljust(10) + 'Version')
        print('-' * 70)
        
        for escalation in all_escalations[:5]:  # Show first 5 escalations
            customer = escalation.customer or 'N/A'
            component = escalation.component_name or 'N/A'
            state = escalation.state or 'N/A'
            version = escalation.version or 'N/A'
            print(f'{customer[:24]:<25} {component[:19]:<20} {state:<10} {version}')
            
        # Show versions and components analysis too
        print()
        print('=== VERSIONS ANALYSIS ===')
        versions = [e.version for e in all_escalations if e.version and e.version.strip()]
        version_counts = Counter(versions)
        
        for version, count in version_counts.most_common(5):
            print(f'{version:<20} {count} escalations')
            
        print()
        print('=== COMPONENTS ANALYSIS ===')
        components = [e.component_name for e in all_escalations if e.component_name and e.component_name.strip()]
        component_counts = Counter(components)
        
        for component, count in component_counts.most_common(5):
            print(f'{component[:30]:<30} {count} escalations')

if __name__ == '__main__':
    main()