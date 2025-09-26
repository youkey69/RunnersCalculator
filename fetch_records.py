"""Fetch analog record data from Google Sheets and store in SQLite."""

from __future__ import annotations

import os
from typing import List, Dict

import gspread
from google.oauth2.service_account import Credentials

import records_db

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def fetch_sheet_records(sheet_id: str, worksheet: str, creds_path: str) -> List[Dict[str, str]]:
    """Retrieve rows from a Google Sheet as a list of dicts."""
    creds = Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).worksheet(worksheet)
    return sheet.get_all_records()


def main() -> None:
    sheet_id = os.environ["SHEET_ID"]
    worksheet = os.environ.get("WORKSHEET", "Sheet1")
    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
    db_path = os.environ.get("DB_PATH", "records.db")

    records = fetch_sheet_records(sheet_id, worksheet, creds_path)
    records_db.init_db(db_path)
    records_db.upsert_records(records, db_path)


if __name__ == "__main__":
    main()
