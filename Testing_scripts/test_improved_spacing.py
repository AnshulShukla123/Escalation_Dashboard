#!/usr/bin/env python3

def format_table_with_borders(headers, rows):
    """Format table with ASCII borders with proper column spacing"""
    if not headers or not rows:
        return ""
    
    # Calculate maximum width for each column with generous padding
    widths = []
    for i in range(len(headers)):
        col_widths = [len(str(headers[i]))]
        for row in rows:
            if i < len(row):
                col_widths.append(len(str(row[i])))
        max_width = max(col_widths)
        # Add generous padding (minimum 6 extra characters or more)
        widths.append(max(max_width + 8, 12))
    
    # Create top border
    top_border = "+"
    for width in widths:
        top_border += "-" * width + "+"
    
    # Create header row with left alignment and full width padding
    header_row = "|"
    for i, header in enumerate(headers):
        padded_header = f" {str(header):<{widths[i]-2}} "
        header_row += padded_header + "|"
    
    # Create separator border (same as top)
    separator = top_border
    
    # Create data rows with full width padding
    data_rows = []
    for row in rows:
        row_str = "|"
        for i in range(len(headers)):
            if i < len(row):
                value = str(row[i])
            else:
                value = ""
            # Left align with full column width padding
            padded_value = f" {value:<{widths[i]-2}} "
            row_str += padded_value + "|"
        data_rows.append(row_str)
    
    # Create bottom border
    bottom_border = top_border
    
    # Combine all parts
    result = [top_border, header_row, separator]
    result.extend(data_rows)
    result.append(bottom_border)
    
    return "\n".join(result)

print("🎯 PERFECT COLUMN SPACING - YOUR REQUESTED FORMAT!")
print("="*60)
print()

print("Your Example - Personnel Table:")
print("-" * 40)
personnel_table = format_table_with_borders(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    [['Hari', 'Srihari', 'None', '2025-10-06']]
)
print(personnel_table)
print()

print("Escalation Information Table:")
print("-" * 40)
escalation_table = format_table_with_borders(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    [['#1', 'Toyota4', '17.12.5', 'CSCwr46982']]
)
print(escalation_table)
print()

print("Component Status Table:")
print("-" * 40)
component_table = format_table_with_borders(
    ['Component', 'Severity', 'Severity Remarks', 'State'],
    [['Client Join in SDA', 'CAP', 'Deployment change: from non-SDA to SDA', 'OPEN']]
)
print(component_table)
print()

print("✅ Perfect left-aligned spacing with full column width!")
print("✅ Content fills entire column like your example!")
print("✅ Professional ASCII bordered format!")
print("✅ Ready for Webex messages!")