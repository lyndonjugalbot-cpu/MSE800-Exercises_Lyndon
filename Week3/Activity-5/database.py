import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "exchange.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS Currency (
    currency_code TEXT PRIMARY KEY,
    currency_name TEXT NOT NULL,
    symbol TEXT
);

CREATE TABLE IF NOT EXISTS Customer (
    customer_id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT
);

CREATE TABLE IF NOT EXISTS ExchangeRate (
    from_currency TEXT NOT NULL REFERENCES Currency(currency_code),
    to_currency TEXT NOT NULL REFERENCES Currency(currency_code),
    rate REAL NOT NULL,
    updated_date TEXT NOT NULL,
    PRIMARY KEY (from_currency, to_currency)
);

CREATE TABLE IF NOT EXISTS ExchangeTransaction (
    transaction_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL REFERENCES Customer(customer_id),
    from_currency TEXT NOT NULL REFERENCES Currency(currency_code),
    to_currency TEXT NOT NULL REFERENCES Currency(currency_code),
    from_amount REAL NOT NULL,
    to_amount REAL NOT NULL,
    rate_applied REAL NOT NULL,
    transaction_date TEXT NOT NULL
);
"""


class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = str(db_path)

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        # This PRAGMA turns on actual foreign key enforcement for this connection
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        conn = self.connect()
        conn.executescript(SCHEMA)
        conn.commit()
        conn.close()

    def is_empty(self):
        conn = self.connect()
        n = conn.execute("SELECT COUNT(*) FROM Currency").fetchone()[0]
        conn.close()
        return n == 0
