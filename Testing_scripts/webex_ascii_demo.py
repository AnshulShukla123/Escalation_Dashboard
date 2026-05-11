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

print("🚀 WEBEX ASCII TABLE MESSAGE DEMO")
print("="*80)
print()

# Simulate escalation data
escalation_data = {
    'id': 1,
    'customer': 'Toyota4',
    'version': '17.12.5',
    'bugid': 'CSCwr46982',
    'component_name': 'Client Join in SDA',
    'severity_type': 'CAP',
    'severity_text': 'Deployment change',
    'state': 'OPEN',
    'dedt_manager': 'Hari',
    'engineer': 'Srihari',
    'contributors': 'None',
    'reported_on': '2025-10-06',
    'sr': 'SR123456',
    'bems': 'Yes',
    'symptom': 'Cannot connect to SDA',
    'upgrade_attempt': 'None attempted',
    'next_step': 'Investigate config',
    'remarks': 'High priority'
}

# Format tables with ASCII borders
main_table = format_table_with_borders(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    [[f"#{escalation_data['id']}", 
      escalation_data['customer'],
      escalation_data['version'], 
      escalation_data['bugid']]]
)

component_table = format_table_with_borders(
    ['Component', 'Severity', 'Severity Remarks', 'State'],
    [[escalation_data['component_name'],
      escalation_data['severity_type'],
      escalation_data['severity_text'],
      escalation_data['state']]]
)

personnel_table = format_table_with_borders(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    [[escalation_data['dedt_manager'],
      escalation_data['engineer'],
      escalation_data['contributors'],
      escalation_data['reported_on']]]
)

tech_table1 = format_table_with_borders(
    ['SR Number', 'BEMS', 'Symptom'],
    [[escalation_data['sr'],
      escalation_data['bems'],
      escalation_data['symptom']]]
)

tech_table2 = format_table_with_borders(
    ['Upgrade Attempt', 'Next Step', 'Remarks'],
    [[escalation_data['upgrade_attempt'],
      escalation_data['next_step'],
      escalation_data['remarks']]]
)

# Compose the complete Webex message
message = f"""## 📊 **Escalation Details - ASCII Table Format**

### 🔢 **Basic Information**
```
{main_table}
```

### 🏢 **Component & Status**  
```
{component_table}
```

### 👥 **Personnel & Timeline**
```
{personnel_table}
```

**Cross Dependent Teams:** None

### ⚡ **Technical Details**
```
{tech_table1}
```

```
{tech_table2}
```

### 🔗 **Actions**
**[📝 View/Edit Escalation #1](http://localhost:5000/edit/1)**"""

print("📤 WEBEX MESSAGE WITH ASCII TABLES:")
print("-" * 80)
print(message)
print("-" * 80)
print()
print("✅ Perfect ASCII bordered tables like your example!")
print("✅ Code blocks ensure proper formatting in Webex!")  
print("✅ Professional grid structure with +, -, | characters!")
print("✅ All data properly aligned and contained!")
print()
print("🎯 To use this functionality:")
print("1. Start your Flask app: python app.py")
print("2. Visit: http://localhost:5000/webex_table_test")
print("3. Enter an escalation ID and click 'Send Table to Webex'")
print("4. Your Webex space will show perfectly formatted ASCII tables!")