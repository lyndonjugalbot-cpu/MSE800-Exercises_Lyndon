# Money Exchange System

A simple OOP + SQLite money exchange application for a currency exchange
business. It manages customers, currencies, exchange rates, and the
transactions where a customer converts one currency into another.

## How to run

```
python main.py
```

The first run creates `exchange.db` and loads sample data automatically.
A text menu then lets you view records, run an exchange, and print reports.

## Database design — 4 tables

The database has **4 tables**. Each one models a distinct thing the business
needs to track, and none of them can be merged without losing information or
creating duplicate/inconsistent data.

1. **Currency** — the set of currencies the business trades (e.g. NZD, USD,
   EUR, AUD). This is necessary as its own table because both `ExchangeRate`
   and `ExchangeTransaction` reference currencies twice each (a "from" and a
   "to" currency), and a lookup table keeps the currency name/symbol defined
   in exactly one place instead of repeated as free text everywhere.

2. **Customer** — the people who exchange money with the business. This is
   necessary because a real customer makes many transactions over time, and
   without a dedicated table the business would have no way to look up a
   customer's history, contact details, or enforce a unique email per person.

3. **ExchangeRate** — the current conversion rate between every currency
   pair the business offers (e.g. NZD → USD). This must be its own table
   rather than a column on `Currency` because a rate is a relationship
   *between two* currencies, not a property of a single currency, and rates
   change independently of the currencies themselves.

4. **ExchangeTransaction** — a record of an actual exchange a customer made:
   who did it, which currencies were involved, how much was exchanged, the
   rate applied at the time, and when it happened. This is necessary as its
   own table (rather than reusing `ExchangeRate`) because rates fluctuate —
   a transaction must freeze the rate that was actually applied at the time
   of the trade, so historical transactions stay accurate even after rates
   are later updated.

See [ER_DIAGRAM.md](ER_DIAGRAM.md) for the full entity/attribute list and
relationships.

## Code structure (OOP style)

- `database.py` — `Database` class: owns the connection and the schema
  (`CREATE TABLE` statements), with foreign keys enforced via
  `PRAGMA foreign_keys = ON`.
- `managers.py` — one manager class per table (`CurrencyManager`,
  `CustomerManager`, `ExchangeRateManager`, `TransactionManager`), each
  wrapping that table's `add()`/`list()` operations and any reports specific
  to it. `TransactionManager` looks up the current rate before recording an
  exchange, so `to_amount` and `rate_applied` are always consistent.
- `main.py` — the menu-driven entry point that wires the managers together,
  seeds sample data on first run, and dispatches user choices.
