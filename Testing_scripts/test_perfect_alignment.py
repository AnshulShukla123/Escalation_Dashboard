#!/usr/bin/env python3

def format_table_row(headers, values):
    """Format table row with fixed column widths for perfect vertical alignment"""
    if not headers or not values:
        return "", ""
    
    # Calculate maximum width for each column (header vs content) 
    widths = []
    for i in range(len(headers)):
        header_len = len(str(headers[i]))
        value_len = len(str(values[i]) if i < len(values) else '')
        max_width = max(header_len, value_len)
        # Add padding and ensure minimum width
        widths.append(max(max_width + 4, 8))  # More padding for better alignment
    
    # Format header row with left-aligned content in fixed width
    header_cells = []
    separator_cells = []
    for i, header in enumerate(headers):
        width = widths[i]
        padded_header = f" {str(header):<{width-2}} "
        header_cells.append(padded_header)
        separator_cells.append(' ' + '-' * (width-2) + ' ')
    
    # Format value row with left-aligned content in same fixed width
    value_cells = []
    for i, value in enumerate(values):
        if i < len(widths):
            width = widths[i]
            padded_value = f" {str(value):<{width-2}} "
            value_cells.append(padded_value)
    
    header_row = '|' + '|'.join(header_cells) + '|'
    separator_row = '|' + '|'.join(separator_cells) + '|'
    value_row = '|' + '|'.join(value_cells) + '|'
    
    return f"{header_row}\n{separator_row}\n{value_row}"

print("="*80)
print("PERFECT VERTICAL ALIGNMENT - ALL | BARS LINE UP!")
print("="*80)
print()

# Test 1: Your exact requested format
result1 = format_table_row(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    ['#1', 'Toyota4', '17.12.5', 'CSCwr46982']
)
print("Test 1: Your Requested Format")
print("-" * 40)
print(result1)
print()

# Test 2: Longer content
result2 = format_table_row(
    ['Component', 'Severity', 'Severity Remarks', 'State'],
    ['Client Join in SDA', 'CAP', 'Deployment change: from non-SDA to SDA', 'OPEN']
)
print("Test 2: Longer Content")  
print("-" * 40)
print(result2)
print()

# Test 3: Personnel information
result3 = format_table_row(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    ['Hari', 'Srihari', 'None', '2025-10-06']
)
print("Test 3: Personnel Information")
print("-" * 40) 
print(result3)
print()

print("✅ All vertical bars (|) are perfectly aligned!")
print("✅ Content is left-aligned within fixed-width columns!")
print("✅ No more truncation - full content displayed!")
print("✅ Professional table formatting for Webex messages!")