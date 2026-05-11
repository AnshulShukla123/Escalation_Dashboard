from app import app, db, Escalation
import datetime

def clear_and_add_dummy():
    # Clear all existing data
    db.drop_all()
    db.create_all()

    # Add 10 fresh dummy entries with empty remarks
    dummy_entries = []
    closing_reasons = ["Bug", "Network issue", "Config issue", "Infra issue", "Serviceability issue"]
    # 5 open entries
    for i in range(5):
        dummy_entries.append(Escalation(
            customer=f"DemoCustomer{i+1}",
            version=f"v{3.0+i}",
            bugid=f"BUG000{i+1}",
            dedt_manager=f"Manager{i+1}",
            engineer=f"Engineer{i+1}",
            cross_team="Routing" if i % 2 == 0 else "IOS-XE",
            component_name=f"Component{i+1}",
            director=f"Director{i+1}",
            cross_de_manager=f"CrossManager{i+1}",
            cross_engineer=f"CrossEngineer{i+1}",
            sr=f"SR{i+1}",
            bems=f"BEMS{i+1}",
            upgrade_attempt=f"Upgrade{i+1}",
            symptom=f"Symptom{i+1}",
            next_step=f"NextStep{i+1}",
            functionality=f"Functionality{i+1}",
            director2=f"Director2_{i+1}",
            escalation_manager=f"EscManager{i+1}",
            escalation_engineer=f"EscEngineer{i+1}",
            remarks="",
            state="Open",
            reopen_reason="",
            closing_reason="",
            reported_on=(datetime.datetime.now() - datetime.timedelta(days=8-i)).strftime('%Y-%m-%d'),
            closed_on="",
            created_on=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_on=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        ))
    # 5 closed entries
    for i in range(5):
        dummy_entries.append(Escalation(
            customer=f"DemoCustomerClosed{i+1}",
            version=f"v{4.0+i}",
            bugid=f"BUG00C{i+1}",
            dedt_manager=f"ManagerC{i+1}",
            engineer=f"EngineerC{i+1}",
            cross_team="Routing" if i % 2 == 0 else "IOS-XE",
            component_name=f"ComponentC{i+1}",
            director=f"DirectorC{i+1}",
            cross_de_manager=f"CrossManagerC{i+1}",
            cross_engineer=f"CrossEngineerC{i+1}",
            sr=f"SRC{i+1}",
            bems=f"BEMSC{i+1}",
            upgrade_attempt=f"UpgradeC{i+1}",
            symptom=f"SymptomC{i+1}",
            next_step=f"NextStepC{i+1}",
            functionality=f"FunctionalityC{i+1}",
            director2=f"Director2_C{i+1}",
            escalation_manager=f"EscManagerC{i+1}",
            escalation_engineer=f"EscEngineerC{i+1}",
            remarks="",
            state="Closed",
            reopen_reason="",
            closing_reason=closing_reasons[i],
            reported_on=(datetime.datetime.now() - datetime.timedelta(days=15-i)).strftime('%Y-%m-%d'),
            closed_on=(datetime.datetime.now() - datetime.timedelta(days=1+i)).strftime('%Y-%m-%d'),
            created_on=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_on=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        ))
    db.session.add_all(dummy_entries)
    db.session.commit()
    print("Database cleared and 10 dummy entries added (5 open, 5 closed, remarks empty).")

if __name__ == "__main__":
    with app.app_context():
        clear_and_add_dummy()
