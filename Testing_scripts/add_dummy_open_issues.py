from app import db, Escalation, app
from datetime import datetime

with app.app_context():
    # Add 5 dummy open issues
    for i in range(1, 6):
        issue = Escalation(
            customer=f"Customer {i}",
            functionality=f"Functionality {i}",
            dedt_manager=f"manager{i}@cisco.com",
            engineer=f"engineer{i}@cisco.com",
            remarks=f"[2025-09-02] Dummy remark for issue {i}",
            state="Open",
            reported_on=datetime.now().strftime("%Y-%m-%d")
        )
        db.session.add(issue)
    db.session.commit()
print("Dummy open issues added.")
