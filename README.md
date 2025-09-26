# Record Inventory

This project demonstrates how to build a small inventory system for analog records.
Data is retrieved from a Google Spreadsheet, saved into a SQLite database, and
made searchable through a small Flask web application.

## Setup

1. Create a Google service account and download its JSON credentials file.
2. Share your Google Sheet containing record data with the service account.
3. Set environment variables:
   - `SHEET_ID`: ID of the Google Sheet (found in its URL).
   - `GOOGLE_APPLICATION_CREDENTIALS`: path to the service account JSON file.
   - `DB_PATH`: location for the SQLite database (defaults to `records.db`).
   - `WORKSHEET`: worksheet name within the sheet (defaults to `Sheet1`).

Install dependencies:

```bash
pip install -r requirements.txt
```

## Fetching data

Run the fetch script to populate the database from the spreadsheet:

```bash
python fetch_records.py
```

## Starting the web server

After the database has data, start the Flask app:

```bash
python server.py
```

Open `http://localhost:5000` in a browser and use the search field to look up
records by title or artist.
