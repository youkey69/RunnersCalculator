import os
import sys
import tempfile
from pathlib import Path

# Ensure project root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import records_db


def test_init_and_search():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "test.db")
        records_db.init_db(db_path)
        sample = [
            {
                "title": "Blue Train",
                "artist": "John Coltrane",
                "label": "Blue Note",
                "year": "1957",
                "catalog": "BN 1577",
            },
            {
                "title": "Kind of Blue",
                "artist": "Miles Davis",
                "label": "Columbia",
                "year": "1959",
                "catalog": "CL 1355",
            },
        ]
        records_db.upsert_records(sample, db_path)
        result = records_db.search_records("Coltrane", db_path)
        assert result[0]["artist"] == "John Coltrane"
        assert len(records_db.search_records("Miles", db_path)) == 1
