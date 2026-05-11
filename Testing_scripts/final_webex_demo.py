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

print("🚀 FINAL WEBEX MESSAGE WITH IMPROVED SPACING")
print("="*70)
print()

# Format tables with improved spacing
main_table = format_table_with_borders(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    [['#1', 'Toyota4', '17.12.5', 'CSCwr46982']]
)

personnel_table = format_table_with_borders(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    [['Hari', 'Srihari', 'None', '2025-10-06']]
)

component_table = format_table_with_borders(
    ['Component', 'Severity', 'State'],
    [['Client Join in SDA', 'CAP', 'OPEN']]
)

# Compose the Webex message
message = f"""## 📊 **Escalation Details - Improved ASCII Format**

### 🔢 **Basic Information**
```
{main_table}
```

### 👥 **Personnel & Timeline** 
```
{personnel_table}
```

### 🏢 **Component & Status**
```
{component_table}
```

### 🔗 **Actions**
**[📝 View/Edit Escalation #1](http://localhost:5000/edit/1)**"""

print("📤 WEBEX MESSAGE PREVIEW:")
print("-" * 70)
print(message)
print("-" * 70)
print()

print("🎯 KEY IMPROVEMENTS:")
print("✅ Left-aligned content with full column width spacing")
print("✅ Content like 'Hari' fills the entire column space")  
print("✅ Professional ASCII borders with + - | characters")
print("✅ Consistent spacing across all columns")
print("✅ Perfect for Webex Teams display!")
print()
print("🚀 Your escalation app is ready with perfect table formatting!")