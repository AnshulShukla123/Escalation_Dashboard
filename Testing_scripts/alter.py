from app import app, db
from sqlalchemy import text

with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(text("ALTER TABLE escalation ADD COLUMN severity VARCHAR(10);"))
        conn.commit()