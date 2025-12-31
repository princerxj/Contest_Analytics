import sqlite3

def get_rank(handle, db_name="contest.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT rank FROM standings
        WHERE LOWER(handle) = LOWER(?)
    """, (handle,))

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


def get_solved(handle, db_name="contest.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT solved FROM standings
        WHERE LOWER(handle) = LOWER(?)
    """, (handle,))

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


def get_percentile(handle, db_name="contest.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM standings")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT rank FROM standings
        WHERE LOWER(handle) = LOWER(?)
    """, (handle,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    rank = row[0]
    percentile = (total - rank + 1) / total * 100
    return round(percentile, 2)
