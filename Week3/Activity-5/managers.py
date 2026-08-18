class CurrencyManager:
    def __init__(self, db):
        self.db = db

    def add(self, code, name, symbol=None):
        connection = self.db.connect()
        connection.execute("INSERT INTO Currency VALUES (?, ?, ?)", (code, name, symbol))
        connection.commit()
        connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Currency").fetchall()
        connection.close()
        return rows


class CustomerManager:
    def __init__(self, db):
        self.db = db

    def add(self, customer_id, first, last, email, phone=None):
        connection = self.db.connect()
        connection.execute("INSERT INTO Customer VALUES (?, ?, ?, ?, ?)", (customer_id, first, last, email, phone))
        connection.commit()
        connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Customer").fetchall()
        connection.close()
        return rows


class ExchangeRateManager:
    def __init__(self, db):
        self.db = db

    def set_rate(self, from_currency, to_currency, rate, date):
        # INSERT OR REPLACE lets us update today's rate for a currency pair.
        connection = self.db.connect()
        connection.execute(
            "INSERT OR REPLACE INTO ExchangeRate VALUES (?, ?, ?, ?)",
            (from_currency, to_currency, rate, date),
        )
        connection.commit()
        connection.close()

    def get_rate(self, from_currency, to_currency):
        connection = self.db.connect()
        row = connection.execute(
            "SELECT rate FROM ExchangeRate WHERE from_currency = ? AND to_currency = ?",
            (from_currency, to_currency),
        ).fetchone()
        connection.close()
        return row["rate"] if row else None

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM ExchangeRate").fetchall()
        connection.close()
        return rows


class TransactionManager:
    def __init__(self, db):
        self.db = db
        self.rates = ExchangeRateManager(db)

    def exchange(self, transaction_id, customer_id, from_currency, to_currency, from_amount, date):
        # Look up the current rate and compute the converted amount before recording the transaction.
        rate = self.rates.get_rate(from_currency, to_currency)
        if rate is None:
            return None

        to_amount = round(from_amount * rate, 2)
        connection = self.db.connect()
        connection.execute(
            "INSERT INTO ExchangeTransaction VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (transaction_id, customer_id, from_currency, to_currency, from_amount, to_amount, rate, date),
        )
        connection.commit()
        connection.close()
        return to_amount

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM ExchangeTransaction").fetchall()
        connection.close()
        return rows

    def most_active_customers(self):
        """Report: number of exchange transactions made by each customer."""
        connection = self.db.connect()
        rows = connection.execute(
            """SELECT c.customer_id, c.first_name || ' ' || c.last_name AS full_name,
                      COUNT(t.transaction_id) AS transaction_count
               FROM Customer c
               JOIN ExchangeTransaction t ON t.customer_id = c.customer_id
               GROUP BY c.customer_id
               ORDER BY transaction_count DESC"""
        ).fetchall()
        connection.close()
        return rows

    def total_bought_per_currency(self):
        """Report: total amount of each currency purchased (to_currency) across all transactions."""
        connection = self.db.connect()
        rows = connection.execute(
            """SELECT t.to_currency, cur.currency_name, SUM(t.to_amount) AS total_amount
               FROM ExchangeTransaction t
               JOIN Currency cur ON cur.currency_code = t.to_currency
               GROUP BY t.to_currency
               ORDER BY total_amount DESC"""
        ).fetchall()
        connection.close()
        return rows
