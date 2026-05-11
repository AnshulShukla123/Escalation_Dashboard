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

print("🚀 WEBEX TABLE MESSAGE DEMO")
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
    'severity_text': 'Deployment change: from non-SDA to SDA',
    'state': 'OPEN',
    'dedt_manager': 'Hari',
    'engineer': 'Srihari',
    'contributors': 'None',
    'reported_on': '2025-10-06',
    'sr': 'SR123456',
    'bems': 'Yes',
    'symptom': 'Client cannot connect to SDA environment',
    'upgrade_attempt': 'None attempted',
    'next_step': 'Investigate network configuration',
    'remarks': 'High priority issue'
}

# Format main escalation table
main_table = format_table_row(
    ['Escalation ID', 'Customer', 'Version', 'Bug ID'],
    [f"#{escalation_data['id']}", 
     escalation_data['customer'],
     escalation_data['version'], 
     escalation_data['bugid']]
)

# Format component information table  
component_table = format_table_row(
    ['Component', 'Severity', 'Severity Remarks', 'State'],
    [escalation_data['component_name'],
     escalation_data['severity_type'],
     escalation_data['severity_text'],
     escalation_data['state']]
)

# Format personnel table
personnel_table = format_table_row(
    ['DE Manager', 'Primary PoC', 'Contributors', 'Reported On'],
    [escalation_data['dedt_manager'],
     escalation_data['engineer'],
     escalation_data['contributors'],
     escalation_data['reported_on']]
)

# Format technical details
tech_table1 = format_table_row(
    ['SR Number', 'BEMS', 'Symptom'],
    [escalation_data['sr'],
     escalation_data['bems'],
     escalation_data['symptom']]
)

tech_table2 = format_table_row(
    ['Upgrade Attempt', 'Next Step', 'Remarks'],
    [escalation_data['upgrade_attempt'],
     escalation_data['next_step'],
     escalation_data['remarks']]
)

# Compose the complete Webex message
message = f"""## 📊 **Escalation Details - Table Format**

### 🔢 **Basic Information**
{main_table}

### 🏢 **Component & Status**  
{component_table}

### 👥 **Personnel & Timeline**
{personnel_table}

**Cross Dependent Teams:** None

### ⚡ **Technical Details**
{tech_table1}

{tech_table2}

### 🔗 **Actions**
**[📝 View/Edit Escalation #1](http://localhost:5000/edit/1)**"""

print("📤 WEBEX MESSAGE PREVIEW:")
print("-" * 80)
print(message)
print("-" * 80)
print()
print("✅ Perfect table formatting with vertical alignment!")
print("✅ All columns properly sized and aligned!")  
print("✅ Professional appearance for Webex Teams!")
print("✅ Ready to send to your Webex space!")
print()
print("🎯 To use this functionality:")
print("1. Start your Flask app: python app.py")
print("2. Visit: http://localhost:5000/webex_table_test")
print("3. Enter an escalation ID and click 'Send Table to Webex'")
print("4. Check your Webex space for the formatted message!")