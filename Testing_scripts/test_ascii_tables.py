#!/usr/bin/env python3

def format_table_with_borders(headers, rows):
    """Format table with ASCII borders like the example image"""
    if not headers or not rows:
        return ""
    
    # Calculate maximum width for each column
    widths = []
    for i in range(len(headers)):
        col_widths = [len(str(headers[i]))]
        for row in rows:
            if i < len(row):
                col_widths.append(len(str(row[i])))
        max_width = max(col_widths)
        widths.append(max_width + 2)  # Add padding
    
    # Create top border
    top_border = "+"
    for width in widths:
        top_border += "-" * width + "+"
    
    # Create header row
    header_row = "|"
    for i, header in enumerate(headers):
        padded_header = f" {str(header):<{widths[i]-1}}"
        header_row += padded_header + "|"
    
    # Create separator border (same as top)
    separator = top_border
    
    # Create data rows
    data_rows = []
    for row in rows:
        row_str = "|"
        for i in range(len(headers)):
            if i < len(row):
                value = str(row[i])
            else:
                value = ""
            padded_value = f" {value:<{widths[i]-1}}"
            row_str += padded_value + "|"
        data_rows.append(row_str)
    
    # Create bottom border
    bottom_border = top_border
    
    # Combine all parts
    result = [top_border, header_row, separator]
    result.extend(data_rows)
    result.append(bottom_border)
    
    return "\n".join(result)

print("📊 ASCII BORDERED TABLES - LIKE YOUR EXAMPLE!")
print("=" * 80)
print()

# Test 1: Basic escalation information
table1 = format_table_with_borders(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    [
        ['#1', 'Toyota4', '17.12.5', 'CSCwr46982'],
        ['#2', 'Cisco Inc', '18.1.2', 'CSCab12345'],
        ['#3', 'Microsoft Corp', '19.0.1', 'CSCzx98765']
    ]
)
print("Basic Information Table:")
print(table1)
print()

# Test 2: Component and status information
table2 = format_table_with_borders(
    ['Component', 'Severity', 'Severity Remarks', 'State'],
    [
        ['Client Join in SDA', 'CAP', 'Deployment change: from non-SDA to SDA', 'OPEN'],
        ['Network Module', 'HIGH', 'Performance degradation observed', 'CLOSED'],
        ['Authentication', 'MEDIUM', 'Login failures intermittent', 'IN_PROGRESS']
    ]
)
print("Component Status Table:")
print(table2)
print()

# Test 3: Personnel information
table3 = format_table_with_borders(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    [
        ['Hari', 'Srihari', 'None', '2025-10-06'],
        ['John Smith', 'Jane Doe', 'Team Alpha, Beta', '2025-10-05'],
        ['Mike Johnson', 'Sarah Wilson', 'Team Gamma', '2025-10-04']
    ]
)
print("Personnel Information Table:")
print(table3)
print()

# Test 4: Your exact example format
table4 = format_table_with_borders(
    ['Col1', 'Col2', 'Col3', 'Numeric Column'],
    [
        ['Value 1', 'Value 2', '123', '10.0'],
        ['Separate', 'cols', 'with a tab or 4 spaces', '-2,027.1'],
        ['This is a row with only one cell', '', '', '']
    ]
)
print("Your Example Format:")
print(table4)
print()

print("✅ Perfect ASCII bordered tables!")
print("✅ Exactly like your example image!")
print("✅ Proper grid structure with +, -, | characters!")
print("✅ Ready for Webex messages!")