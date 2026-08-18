from database import Database
from managers import CurrencyManager, CustomerManager, ExchangeRateManager, TransactionManager
# Manager classes above each wrap one table and expose add()/list()/report methods.


def seed(currencies, rates):
    # Sample data used to populate an empty database on first run.
    # Customers are added via the "Add Customer" menu option instead of being seeded here.

    # Base set of currencies the system can exchange between.
    currencies.add("NZD", "New Zealand Dollar", "$")
    currencies.add("USD", "US Dollar", "$")
    currencies.add("EUR", "Euro", "€")
    currencies.add("AUD", "Australian Dollar", "$")

    # Rates are quoted both ways so a customer can exchange in either direction.
    rates.set_rate("NZD", "USD", 0.61, "2026-08-01")
    rates.set_rate("USD", "NZD", 1.64, "2026-08-01")
    rates.set_rate("NZD", "EUR", 0.56, "2026-08-01")
    rates.set_rate("EUR", "NZD", 1.79, "2026-08-01")
    rates.set_rate("NZD", "AUD", 0.92, "2026-08-01")
    rates.set_rate("AUD", "NZD", 1.09, "2026-08-01")


def menu():
    # Prints the main menu options for the user to choose from.
    print("\n==== Money Exchange System ====")
    print("1. View Currencies")
    print("2. View Customers")
    print("3. Add Customer")
    print("4. View Exchange Rates")
    print("5. View Transactions")
    print("6. Make an Exchange")
    print("7. Report: Most active customers")
    print("8. Report: Total bought per currency")
    print("9. Exit")


def add_customer(customers):
    # Prompts for customer details and auto-generates the customer ID.

    # Collect the raw details from the user. Phone is optional, so an empty
    # string is converted to None rather than stored as blank text.
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone number (optional): ").strip() or None

    # First name, last name, and email are mandatory fields on the Customer table.
    if not first or not last or not email:
        print("  First name, last name, and email are required.")
        return

    # Auto-generate the next customer ID from how many customers already exist,
    # e.g. the 4th customer added becomes CUST004.
    customer_id = f"CUST{len(customers.list()) + 1:03d}"
    try:
        customers.add(customer_id, first, last, email, phone)
    except Exception as e:
        # Covers cases like a duplicate email, which the Customer table enforces as UNIQUE.
        print(f"  Could not add customer: {e}")
        return
    print(f"  Added {customer_id} | {first} {last} | {email} | {phone}")


def make_exchange(customers, currencies, rates, transactions):
    # Walks the user through converting one currency into another for a customer.

    # The customer must already exist before they can make an exchange.
    customer_id = input("Customer ID: ").strip()
    if not any(c["customer_id"] == customer_id for c in customers.list()):
        print("  No such customer.")
        return

    # Only currencies present in the Currency table are valid to exchange.
    available_codes = [c["currency_code"] for c in currencies.list()]

    # Keep re-prompting for the source currency until a valid code is entered,
    # rather than aborting the whole exchange on the first bad input.
    from_currency = input("From currency (e.g. NZD): ").strip().upper()
    while from_currency not in available_codes:
        print(f"  Currency '{from_currency}' is not available. Available currencies: {', '.join(available_codes)}")
        from_currency = input("From currency (e.g. NZD): ").strip().upper()

    # Same re-prompt loop for the destination currency.
    to_currency = input("To currency (e.g. USD): ").strip().upper()
    while to_currency not in available_codes:
        print(f"  Currency '{to_currency}' is not available. Available currencies: {', '.join(available_codes)}")
        to_currency = input("To currency (e.g. USD): ").strip().upper()

    # The amount must be numeric; anything else is rejected outright.
    try:
        amount = float(input(f"Amount of {from_currency} to exchange: ").strip())
    except ValueError:
        print("  Amount must be a number.")
        return

    # A rate must exist for this currency pair before we can convert.
    rate = rates.get_rate(from_currency, to_currency)
    if rate is None:
        print(f"  No exchange rate found for {from_currency} -> {to_currency}.")
        return

    # Auto-generate the next transaction ID and record the exchange.
    transaction_id = f"TXN{len(transactions.list()) + 1:03d}"
    to_amount = transactions.exchange(transaction_id, customer_id, from_currency, to_currency, amount, "2026-08-18")
    print(f"  Done: {amount} {from_currency} -> {to_amount} {to_currency} (rate {rate})")


def main():
    # Connect to the database and make sure the schema exists before doing anything else.
    db = Database()
    db.create_tables()

    # Managers encapsulate CRUD/query logic for each entity, sharing the same db connection.
    currencies = CurrencyManager(db)
    customers = CustomerManager(db)
    rates = ExchangeRateManager(db)
    transactions = TransactionManager(db)

    # Only seed sample data the first time the app runs against a fresh database.
    if db.is_empty():
        seed(currencies, rates)
        print("Database was empty - sample data has been loaded.")

    # Main application loop: show the menu, read a choice, dispatch, repeat until exit.
    while True:
        menu()
        choice = input("Select an option (1-9): ").strip()
        if choice == "1":
            # List all currencies.
            for c in currencies.list():
                print(f"  {c['currency_code']} | {c['currency_name']} | {c['symbol']}")
        elif choice == "2":
            # List all customers.
            for c in customers.list():
                print(f"  {c['customer_id']} | {c['first_name']} {c['last_name']} | {c['email']} | {c['phone_number']}")
        elif choice == "3":
            # Add a new customer.
            add_customer(customers)
        elif choice == "4":
            # List all exchange rates.
            for r in rates.list():
                print(f"  {r['from_currency']} -> {r['to_currency']} : {r['rate']} (as of {r['updated_date']})")
        elif choice == "5":
            # List all transactions.
            for t in transactions.list():
                print(f"  {t['transaction_id']} | {t['customer_id']} | "
                      f"{t['from_amount']} {t['from_currency']} -> {t['to_amount']} {t['to_currency']} "
                      f"| rate={t['rate_applied']} | {t['transaction_date']}")
        elif choice == "6":
            # Make a new exchange transaction.
            make_exchange(customers, currencies, rates, transactions)
        elif choice == "7":
            # Report: number of transactions made by each customer.
            for r in transactions.most_active_customers():
                print(f"  {r['customer_id']} | {r['full_name']} | {r['transaction_count']} transaction(s)")
        elif choice == "8":
            # Report: total amount of each currency bought across all transactions.
            for r in transactions.total_bought_per_currency():
                print(f"  {r['to_currency']} ({r['currency_name']}): {r['total_amount']} total bought")
        elif choice == "9":
            # Exit the loop and end the program.
            print("Goodbye!")
            break
        else:
            # Anything outside 1-9 is not a valid menu option.
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
