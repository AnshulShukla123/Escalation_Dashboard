#!/usr/bin/env python3
"""
Test script for the new dynamic table formatting in Webex messages
"""

def format_table_row(headers, values):
    """Format table row with dynamic column widths based on content"""
    if not headers or not values:
        return "", ""
    
    # Calculate maximum width for each column (header vs content)
    widths = []
    for i in range(len(headers)):
        header_len = len(str(headers[i]))
        value_len = len(str(values[i]) if i < len(values) else '')
        max_width = max(header_len, value_len)
        # Add some padding space, minimum of 3 characters
        widths.append(max(max_width + 2, 5))
    
    # Format header row
    header_cells = []
    separator_cells = []
    for i, header in enumerate(headers):
        width = widths[i]
        padded_header = str(header).center(width)
        header_cells.append(padded_header)
        separator_cells.append(':' + '-' * (width-2) + ':')
    
    # Format value row  
    value_cells = []
    for i, value in enumerate(values):
        if i < len(widths):
            width = widths[i]
            padded_value = str(value).center(width) 
            value_cells.append(padded_value)
    
    header_row = '| ' + ' | '.join(header_cells) + ' |'
    separator_row = '| ' + ' | '.join(separator_cells) + ' |'
    value_row = '| ' + ' | '.join(value_cells) + ' |'
    
    return f"{header_row}\n{separator_row}\n{value_row}"

# Test cases
print("=" * 80)
print("DYNAMIC WEBEX TABLE FORMATTING - NO MORE TRUNCATION!")
print("=" * 80)
print()

# Test 1: Your original example
print("Test 1: Your Original Example")
print("-" * 40)
main_table = format_table_row(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    ['#1', 'Toyota4', '17.12.55', 'CSCwr46982']
)
print(main_table)
print()

# Test 2: Long content (no truncation)
print("Test 2: Long Content (No Truncation!)")
print("-" * 40)
component_table = format_table_row(
    ['Component', 'Severity', 'Severity Remarks', 'State'],
    ['Client Join in SDA', 'CAP', 'Deployment change: from non-SDA to SDA', 'OPEN']
)
print(component_table)
print()

# Test 3: Very long content
print("Test 3: Very Long Content")
print("-" * 40)
personnel_table = format_table_row(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    ['Hari Krishnamurthy', 'Srihari Subramanian', 'Team Alpha, Team Beta, Team Gamma', '2025-10-06']
)
print(personnel_table)
print()

# Test 4: Technical details
print("Test 4: Technical Details")
print("-" * 40)
tech_table = format_table_row(
    ['SR Number', 'BEMS', 'Symptom'],
    ['SR123456789', 'Yes', 'Client cannot join SDA environment after deployment change from traditional to SDA architecture']
)
print(tech_table)
print()

print("✅ All content displays fully - no more '...' truncation!")
print("✅ Column widths adjust dynamically based on content length!")
print("✅ Professional centered alignment maintained!")