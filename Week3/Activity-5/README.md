# Money Exchange System

A simple program for managing currency exchanges, OOP and SQLite.

It keeps track of customers, the currencies we deal in, the exchange rates between them, and every transaction where a customer swaps one currency for another.

## How the database is set up

There are 4 tables:

1. **Currency** — just a list of the currencies we trade (NZD, USD, EUR, AUD, etc). I split this into its own table because both the rates and the transactions need to reference currencies twice (a "from" and a "to" side), so it's better to store each currency's name/symbol once and just point to it, instead of typing it out everywhere.

2. **Customer** — the people doing the exchanges. Needed as its own table because a customer will usually make several transactions over time, and we need somewhere to store their details and keep their email unique, plus be able to pull up their history later.

3. **ExchangeRate** — the current rate between any two currencies (like NZD → USD). This can't just live inside the Currency table because a rate is really a relationship *between two* currencies, not something that belongs to just one of them, and rates change on their own over time.

4. **ExchangeTransaction** — the actual record of an exchange: who did it, which currencies, how much, what rate was used, and when. This is kept separate from ExchangeRate because rates keep changing — if a transaction just pointed to the current rate, old transactions would end up showing the wrong numbers once rates update. So each transaction locks in the rate that was actually used at the time.

Full list of fields and how the tables connect is in [ER_DIAGRAM.md](ER_DIAGRAM.md).

## How the code is organized

- `database.py` — the `Database` class. Handles the connection and creates the tables, with foreign keys turned on (`PRAGMA foreign_keys = ON`) so bad references get caught.
- `managers.py` — one manager class per table (`CurrencyManager`, `CustomerManager`, `ExchangeRateManager`, `TransactionManager`). Each one handles adding/listing records for its table, plus any reports for that table. `TransactionManager` also looks up the current rate before saving a transaction, so the amount and rate always match up.
- `main.py` — the menu that ties everything together. Loads some sample data the first time it runs, then just routes whatever the user picks to the right manager.
