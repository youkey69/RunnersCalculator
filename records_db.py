"""Database helper functions for record inventory."""

from __future__ import annotations

import sqlite3
from typing import Dict, Iterable, List

def init_db(db_path: str) -> None:
    """Create the records table if it doesn't already exist."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            artist TEXT,
            label TEXT,
            year TEXT,
            catalog TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def upsert_records(records: Iterable[Dict[str, str]], db_path: str) -> None:
    """Insert records from an iterable of dictionaries."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for rec in records:
        cur.execute(
            """
            INSERT INTO records (title, artist, label, year, catalog)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                rec.get("title"),
                rec.get("artist"),
                rec.get("label"),
                rec.get("year"),
                rec.get("catalog"),
            ),
        )
    conn.commit()
    conn.close()


def search_records(query: str, db_path: str) -> List[Dict[str, str]]:
    """Search for records where title or artist matches the query."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    like = f"%{query}%"
    cur.execute(
        """
        SELECT title, artist, label, year, catalog
        FROM records
        WHERE title LIKE ? OR artist LIKE ?
        """,
        (like, like),
    )
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows
