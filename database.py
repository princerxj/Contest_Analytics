import sqlite3

def store_standings(records, db_name="contest.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS standings (
            rank INTEGER,
            handle TEXT,
            points REAL,
            penalty INTEGER,
            solved INTEGER
        )
    """)

    cursor.execute("DELETE FROM standings")

    for r in records:
        cursor.execute("""
            INSERT INTO standings VALUES (?, ?, ?, ?, ?)
        """, (
            r["rank"],
            r["handle"],
            r["points"],
            r["penalty"],
            r["solved"]
        ))

    conn.commit()
    conn.close()
