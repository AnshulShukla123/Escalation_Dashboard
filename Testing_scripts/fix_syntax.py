#!/usr/bin/env python3
"""
Quick fix script to remove orphaned code lines causing syntax errors
"""

def fix_syntax_error():
    with open('app.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the line numbers to clean up
    cleaned_lines = []
    in_orphaned_section = False
    
    for i, line in enumerate(lines, 1):
        # Check if we're at the end of send_escalation_update_to_webex function
        if 'print(f"❌ Failed to post escalation update to Webex: {e}")' in line:
            cleaned_lines.append(line)
            in_orphaned_section = True
            continue
            
        # Check if we've reached the next function definition
        if in_orphaned_section and line.strip().startswith('def send_escalation_card'):
            # Add a blank line before the function
            cleaned_lines.append('\n\n')
            cleaned_lines.append(line)
            in_orphaned_section = False
            continue
            
        # Skip orphaned lines in the problematic section
        if in_orphaned_section:
            # Skip lines that look like orphaned code
            stripped = line.strip()
            if (stripped == '' or 
                'f"' in stripped or 
                stripped == ')' or
                '# Prepare data for the table card format' in stripped or
                'payload = {' in stripped or
                stripped.startswith('"id":') or
                stripped.startswith('"date":') or
                stripped.startswith('"customer":') or
                stripped.startswith('"component":') or
                stripped.startswith('"severity":') or
                stripped.startswith('"remarks":') or
                stripped.startswith('"url":') or
                stripped == '}' or
                '# Send table card to Webex' in stripped or
                'try:' in stripped or
                'response = send_escalation_card' in stripped or
                'if response.status_code == 200:' in stripped or
                'print(f"✅ Successfully posted escalation update' in stripped or
                'else:' in stripped or
                'print(f"❌ Failed to post update to Webex' in stripped or
                'except Exception as e:' in stripped):
                print(f"Skipping orphaned line {i}: {stripped}")
                continue
        
        # Keep all other lines
        if not in_orphaned_section:
            cleaned_lines.append(line)
    
    # Write the cleaned file
    with open('app.py', 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    print("✅ Syntax error fix completed!")

if __name__ == "__main__":
    fix_syntax_error()