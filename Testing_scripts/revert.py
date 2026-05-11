import sqlite3

conn = sqlite3.connect('instance/escalations.db')
cur = conn.cursor()

# 1. Rename old table
cur.execute("ALTER TABLE escalation RENAME TO escalation_old;")

# 2. Create new table without closing_remarks
cur.execute('''
CREATE TABLE escalation (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    version TEXT,
    bugid TEXT,
    dedt_manager TEXT,
    engineer TEXT,
    cross_team TEXT,
    component_name TEXT,
    director TEXT,
    cross_de_manager TEXT,
    cross_engineer TEXT,
    sr TEXT,
    bems TEXT,
    upgrade_attempt TEXT,
    symptom TEXT,
    next_step TEXT,
    functionality TEXT,
    director2 TEXT,
    escalation_manager TEXT,
    escalation_engineer TEXT,
    remarks TEXT,
    state TEXT,
    reopen_reason TEXT,
    closing_reason TEXT,
    reported_on TEXT,
    closed_on TEXT,
    created_on TEXT,
    updated_on TEXT,
    pending_action TEXT,
    severity TEXT
);
''')

# 3. Copy data (excluding closing_remarks)
cur.execute('''
INSERT INTO escalation (
    id, customer, version, bugid, dedt_manager, engineer, cross_team, component_name, director,
    cross_de_manager, cross_engineer, sr, bems, upgrade_attempt, symptom, next_step, functionality,
    director2, escalation_manager, escalation_engineer, remarks, state, reopen_reason, closing_reason,
    reported_on, closed_on, created_on, updated_on, pending_action, severity
)
SELECT
    id, customer, version, bugid, dedt_manager, engineer, cross_team, component_name, director,
    cross_de_manager, cross_engineer, sr, bems, upgrade_attempt, symptom, next_step, functionality,
    director2, escalation_manager, escalation_engineer, remarks, state, reopen_reason, closing_reason,
    reported_on, closed_on, created_on, updated_on, pending_action, severity
FROM escalation_old;
''')

# 4. Remove old table
cur.execute("DROP TABLE escalation_old;")

conn.commit()
conn.close()
print("Column reverted!")