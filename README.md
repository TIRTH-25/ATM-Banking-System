# 🏦 Fresher Bank — ATM Banking System

A console-based banking application built with Python to demonstrate how object-oriented design can model real banking rules. Users can create savings or current accounts, sign in securely, manage funds, view transaction history, and retain their data between program runs.

> Built as a focused OOP project: each account type owns its business rules while the banking service coordinates operations and persistence.

## Highlights

- Two account types: **Savings** and **Current**
- Secure 4-digit PIN verification using a SHA-256 hash (the plaintext PIN is never stored)
- Deposits, withdrawals, balance checks, and PIN changes
- Savings-account minimum-balance enforcement
- Current-account overdraft support with a configurable limit
- Interest calculation for savings accounts
- Timestamped transaction history with unique transaction IDs
- JSON persistence: accounts and transactions survive a restart
- Input validation and clear, user-friendly error messages
- Built entirely with the Python standard library

## What it demonstrates

| Concept | Where it is used |
| --- | --- |
| Encapsulation | `BankAccount` keeps balance, PIN hash, account number, and transactions private. |
| Inheritance | `SavingsAccount` and `CurrentAccount` extend `BankAccount`. |
| Polymorphism | `Bank.withdraw()` calls `account.withdraw()`; Python selects the appropriate account rule at runtime. |
| Method overriding | Savings withdrawals preserve a minimum balance; current withdrawals allow bounded overdraft. |
| Composition | A `Bank` owns accounts, and each account owns a collection of `Transaction` objects. |
| Class methods & variables | Counters generate unique account and transaction IDs. |
| Static methods | PIN and name validation do not need instance state. |
| Serialization | `to_dict()` / `from_dict()` convert objects to and from JSON. |

## Architecture

```text
                        ┌──────────────────┐
                        │     main.py      │
                        │ Application Entry│
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │       ATM        │
                        │  User Interface  │
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │       Bank       │
                        │ Business Logic   │
                        └────────┬─────────┘
                                 │
                         manages │
                                 ▼
                   ┌─────────────────────────┐
                   │      BankAccount        │
                   │       Base Class        │
                   └────────────┬────────────┘
                                │
                 ┌──────────────┴──────────────┐
                 │                             │
                 ▼                             ▼
       ┌──────────────────┐          ┌──────────────────┐
       │ SavingsAccount   │          │ CurrentAccount   │
       │ Min Balance      │          │ Overdraft        │
       │ Interest         │          │ Facility         │
       └────────┬─────────┘          └────────┬─────────┘
                │                             │
                └──────────────┬──────────────┘
                               │ records
                               ▼
                      ┌─────────────────┐
                      │   Transaction   │
                      │ Transaction Log │
                      └────────┬────────┘
                               │ serialized to
                               ▼
                      ┌─────────────────┐
                      │ accounts.json   │
                      │ Persistent Data │
                      └─────────────────┘
```

## Application flow

```text
                   START APPLICATION
                          │
                          ▼
                      main.py
                          │
                          ▼
                    Load JSON Data
                          │
                          ▼
                   Create Bank Object
                          │
                          ▼
                   Start ATM Interface
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
        Create Account   Login        Exit
             │            │             │
             │            ▼             │
             │       Verify PIN          │
             │            │             │
             │            ▼             │
             │       Account Menu        │
             │            │             │
             │      ┌─────┼──────┐      │
             │      │     │      │      │
             │      ▼     ▼      ▼      │
             │   Deposit Withdraw Balance│
             │      │     │              │
             │      └──┬──┘              │
             │         ▼                 │
             │    Transaction            │
             │         │                 │
             └─────────┴───────┬─────────┘
                               ▼
                         Save to JSON
                               │
                               ▼
                         Continue / Exit
```

## Key business rules

### Savings account

A savings account cannot fall below its configured minimum balance. For example, with a ₹5,000 balance and a ₹1,000 minimum, a withdrawal may leave at least ₹1,000.

### Current account

A current account can go below zero up to its overdraft limit. For example, a ₹3,000 balance with a ₹5,000 overdraft limit may reach -₹5,000, but cannot go lower.

### Persistence and ID safety

On exit and after each account-changing operation, data is written to `data/accounts.json`. When the program starts again, it rebuilds the correct account subclass and its transaction history from that file. The highest saved account and transaction IDs are restored into their respective counters, so newly created records never reuse an existing ID.

## Getting started

### Prerequisites

- Python 3.8 or newer
- No third-party packages required

### Run locally

```bash
git clone <your-repository-url>
cd ATM-Banking-System
python3 main.py
```

On Windows, use:

```bash
python main.py
```

## Example session

```text
1. Create Savings Account
2. Create Current Account
3. Login
4. Exit

Enter your choice: 1

CREATE SAVINGS ACCOUNT
Enter account holder name: Tirth Patel
Create 4-digit PIN: 1234
Enter initial balance: ₹5000
Minimum balance (default ₹1000):

✅ Savings account created!
Account Number : 100001
Account Holder : Tirth Patel
Account Type   : SavingsAccount
Balance        : ₹5000.00
```

After login, customers can check their balance, deposit, withdraw, change their PIN, review transactions, and—on savings accounts—add interest.

```text
#1   | DEPOSIT    | ₹2000.00    | Balance: ₹7000.00   | 2026-08-20 20:40:01
#2   | WITHDRAW   | ₹1000.00    | Balance: ₹6000.00   | 2026-08-20 20:41:22
#3   | INTEREST   | ₹240.00     | Balance: ₹6240.00   | 2026-08-20 20:42:10
```

## Project structure

```text
ATM-Banking-System/
├── data/
│   └── accounts.json
├── models/
│   ├── bank_account.py
│   ├── current_account.py
│   ├── savings_account.py
│   └── transaction.py
├── services/
│   ├── atm.py
│   └── bank.py
├── main.py
└── README.md
```

## Design notes

- PINs are stored as hashes rather than plaintext. For a production banking system, use a salted, deliberately slow password-hashing algorithm such as Argon2 or bcrypt, not plain SHA-256.
- This project uses `float` for simplicity. A production financial application should use `decimal.Decimal` and a database with transactional guarantees.
- JSON is intentionally used here as a lightweight persistence layer; a real deployment would add authentication controls, auditing, encryption, and a proper database.

## Future improvements

- Unit tests with `pytest` or `unittest`
- Use `Decimal` for currency calculations
- Transfer funds between accounts
- Account statements and date-range filtering
- Role-based administrator features
- Database persistence and secure password hashing

## Author

**Tirth Patel**

If you found this project useful, feel free to star the repository.
