🏦 ATM Banking System

A console-based ATM & Banking Management System built with Python, designed to demonstrate practical Object-Oriented Programming (OOP) concepts through a realistic banking application.

The project supports multiple account types, secure PIN handling, deposits, withdrawals, overdrafts, minimum-balance rules, interest calculation, transaction history, and persistent JSON storage.

The main goal of this project is not just to build a banking application, but to demonstrate how OOP concepts can be combined to design a maintainable, modular, and extensible software system.

🚀 Project Highlights
🔐 Secure PIN storage using SHA-256 hashing
👤 Savings and Current account support
💰 Deposit and withdrawal operations
🏦 Savings account minimum-balance restriction
💳 Current account overdraft facility
📈 Savings account interest calculation
🔄 PIN change functionality
📜 Complete transaction history
💾 Persistent data storage using JSON
🔁 Accounts and transactions survive application restart
🆔 Automatic account number generation
🧾 Automatic transaction ID generation
🛡️ Input validation and error handling
🧩 Modular project architecture
🐍 Built completely with Python Standard Library
🎯 Why I Built This Project

I built this project to apply Python OOP concepts to a practical real-world problem instead of learning them only through isolated examples.

The system demonstrates how a base BankAccount class can provide common functionality while specialized account classes modify behavior according to their own business rules.

For example:

A SavingsAccount must maintain a minimum balance.
A CurrentAccount can use an overdraft facility.
Both accounts expose the same withdraw() method.
Python determines the correct implementation at runtime.

This makes the project a practical demonstration of inheritance, method overriding, polymorphism, encapsulation, composition, and abstraction-oriented design.

🧠 OOP Concepts Demonstrated
1. Classes & Objects

The application is designed using multiple classes:

BankAccount
SavingsAccount
CurrentAccount
Transaction
Bank
ATM

Objects are created from these classes during runtime.

Example:

account = SavingsAccount(
    "Tirth Patel",
    "1234",
    5000
)
2. Encapsulation

Sensitive account information is kept inside the class using private attributes.

self.__balance
self.__pin_hash
self.__account_number

External code cannot directly modify these attributes.

Instead, controlled methods are provided:

account.get_balance()
account.deposit()
account.withdraw()
account.change_pin()

This protects the internal state of the object.

3. Inheritance

SavingsAccount and CurrentAccount inherit common functionality from BankAccount.

                 BankAccount
                 /          \
                /            \
               ▼              ▼
      SavingsAccount    CurrentAccount

This prevents duplication of common account logic.

4. Method Overriding

BankAccount provides a basic withdraw() implementation.

def withdraw(self, amount):
    ...

Both subclasses override it according to their own rules.

SavingsAccount
def withdraw(self, amount):
    ...

Checks minimum balance.

CurrentAccount
def withdraw(self, amount):
    ...

Checks overdraft limit.

The same method name has different behavior.

5. Polymorphism

The Bank class can work with different account types through the same interface.

balance = account.withdraw(amount)

If account is a:

SavingsAccount
       ↓
SavingsAccount.withdraw()

If account is a:

CurrentAccount
       ↓
CurrentAccount.withdraw()
Runtime Polymorphism
                    withdraw()
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      SavingsAccount        CurrentAccount
             │                     │
             ▼                     ▼
    Minimum Balance          Overdraft Rule

This is one of the main OOP concepts demonstrated by the project.

6. super()

The subclasses reuse the parent constructor:

super().__init__(
    account_holder,
    pin,
    initial_balance
)

super() allows the subclasses to reuse common parent functionality without duplicating code.

7. Class Variable

The project uses:

account_counter = 100000

This variable is shared by all account objects.

It is used to generate unique account numbers.

Example:

100001
100002
100003
100004
8. Class Method

Account numbers are generated using:

@classmethod
def generate_account_number(cls):
    ...

A class method is appropriate because the method operates on class-level data.

9. Static Method

PIN validation does not require object or class state.

Therefore it is implemented as:

@staticmethod
def validate_pin(pin):
    ...

It simply validates whether the PIN contains exactly four digits.

10. Magic Methods

The project implements several Python magic methods.

__init__()

Initializes objects.

__str__()

Provides a readable string representation.

print(account)
__eq__()

Allows account objects to be compared using their account number.

account1 == account2
11. Name Mangling

Private attributes use double underscores:

self.__balance
self.__pin_hash

Python internally name-mangles them, for example:

_BankAccount__balance

This demonstrates Python's approach to implementing private attributes.

12. Protected Method

The project uses:

_apply_withdrawal()

The single underscore communicates that the method is intended for internal/subclass use.

CurrentAccount uses it after applying its own overdraft rule.

13. Composition

The project also demonstrates has-a relationships.

Bank has Accounts
Bank
 │
 ├── SavingsAccount
 ├── CurrentAccount
 └── SavingsAccount
Account has Transactions
SavingsAccount
 │
 ├── Transaction
 ├── Transaction
 └── Transaction

This is composition: objects work together to build the larger system.

🏗️ System Architecture
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
                    │      Base Class         │
                    └────────────┬────────────┘
                                 │
                  ┌──────────────┴──────────────┐
                  │                             │
                  ▼                             ▼
        ┌──────────────────┐          ┌──────────────────┐
        │ SavingsAccount   │          │ CurrentAccount   │
        │                  │          │                  │
        │ Min Balance      │          │ Overdraft        │
        │ Interest         │          │ Facility         │
        └────────┬─────────┘          └────────┬─────────┘
                 │                             │
                 └──────────────┬──────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Transaction   │
                       │ Transaction Log │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ accounts.json   │
                       │ Persistent Data │
                       └─────────────────┘
🔄 Application Flow
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
              │            │
              │            ▼
              │       Verify PIN
              │            │
              │            ▼
              │       Account Menu
              │            │
              │      ┌─────┼──────┐
              │      │     │      │
              │      ▼     ▼      ▼
              │   Deposit Withdraw Balance
              │      │     │
              │      └──┬──┘
              │         ▼
              │    Transaction
              │         │
              └─────────┤
                        ▼
                  Save to JSON
                        │
                        ▼
                  Continue / Exit
💳 Account Behavior
Savings Account

A Savings Account:

Requires a minimum opening balance
Must maintain the minimum balance
Supports deposits
Supports withdrawals
Supports interest calculation
Stores transaction history

Example:

Balance:       ₹5000
Minimum:       ₹1000

Withdraw ₹3000
       ↓
Balance = ₹2000
       ↓
Allowed ✓

But:

Balance:       ₹2000
Minimum:       ₹1000

Withdraw ₹1500
       ↓
Balance would become ₹500
       ↓
Rejected ✗
Current Account

A Current Account supports overdraft.

Example:

Balance:        ₹3000
Overdraft:      ₹5000

Withdraw ₹6000
       ↓
Balance = -₹3000
       ↓
Allowed ✓

But:

Balance:        -₹3000
Overdraft:       ₹5000

Withdraw ₹3000
       ↓
Balance = -₹6000
       ↓
Rejected ✗
🔐 PIN Security

The application does not store the user's original PIN.

Instead:

User PIN
   │
   ▼
SHA-256 Hash
   │
   ▼
Stored in JSON

When the user logs in:

Entered PIN
    │
    ▼
SHA-256 Hash
    │
    ▼
Compare with Stored Hash
    │
    ├── Match ──► Login Successful
    │
    └── No Match ► Wrong PIN

Note: SHA-256 is used here for educational purposes. Production banking systems should use a password/PIN hashing algorithm designed specifically for credential storage, with appropriate salting and security controls.

💾 Data Persistence

The application stores account information in:

data/accounts.json

The application converts objects into dictionaries before saving.

Python Object
      │
      ▼
   to_dict()
      │
      ▼
 Dictionary
      │
      ▼
    JSON

When the application starts again:

JSON
 │
 ▼
Dictionary
 │
 ▼
from_dict()
 │
 ▼
Python Object

This means data survives application restarts.

🆔 Unique Account Numbers

Account numbers are generated automatically using a class-level counter.

First account
    ↓
100001

Second account
    ↓
100002

Third account
    ↓
100003

When accounts are loaded from JSON, the counter is updated so that newly created accounts do not reuse an existing number.

🧾 Transaction Management

Every successful financial operation creates a transaction.

Supported transaction types:

DEPOSIT
WITHDRAW
INTEREST

Each transaction contains:

Transaction ID
Transaction Type
Amount
Balance After Transaction
Timestamp

Example:

#1 | DEPOSIT  | ₹2000.00 | Balance: ₹7000.00
#2 | WITHDRAW | ₹1000.00 | Balance: ₹6000.00
#3 | INTEREST | ₹240.00  | Balance: ₹6240.00

Transaction IDs are also restored from JSON to prevent duplicates after restarting the application.

🔁 Persistence & Restart Demonstration
Before closing:
Account Number: 100001
Balance: ₹7000

Transactions:
#1 DEPOSIT
#2 WITHDRAW
Close application
Data → accounts.json
Start application again
accounts.json
     ↓
load_accounts()
     ↓
Account reconstructed
     ↓
Transaction history restored

Result:

Account Number: 100001
Balance: ₹7000

Transactions:
#1 DEPOSIT
#2 WITHDRAW

The application does not lose its data after restart.

📁 Project Structure
ATM-Banking-System/
│
├── main.py
│
├── data/
│   └── accounts.json
│
├── models/
│   ├── __init__.py
│   ├── bank_account.py
│   ├── savings_account.py
│   ├── current_account.py
│   └── transaction.py
│
├── services/
│   ├── __init__.py
│   ├── bank.py
│   └── atm.py
│
├── .gitignore
│
└── README.md
Responsibility of Each File
File	Responsibility
main.py	Application entry point
bank_account.py	Base account class
savings_account.py	Savings-specific behavior
current_account.py	Current-specific behavior
transaction.py	Transaction model
bank.py	Account management and business logic
atm.py	Console UI and user interaction
accounts.json	Persistent account data
🛠️ Technologies Used
Python 3
Object-Oriented Programming
Python Standard Library
JSON
hashlib
datetime
File I/O
Git & GitHub

No external Python packages are required.

▶️ How to Run
1. Clone the repository
git clone git@github.com:TIRTH-25/ATM-Banking-System.git
2. Enter the project
cd ATM-Banking-System
3. Run the application
python main.py
🧪 Features Tested

The application supports and has been designed to handle:

Create Savings Account

Create Current Account

Login

Wrong PIN

Deposit

Savings minimum balance

Current overdraft

Change PIN

Interest calculation

Transaction history

Close application

Restart application

Account persistence

Transaction persistence

Unique account numbers

Unique transaction IDs

📌 Learning Outcomes

Through this project, I practiced:

Python
   │
   ├── Classes & Objects
   ├── Constructors
   ├── Encapsulation
   ├── Name Mangling
   ├── Inheritance
   ├── Polymorphism
   ├── Method Overriding
   ├── super()
   ├── Class Variables
   ├── Class Methods
   ├── Static Methods
   ├── Magic Methods
   ├── Protected Methods
   ├── Composition
   ├── Exception Handling
   ├── JSON Serialization
   ├── JSON Deserialization
   ├── File Handling
   └── Data Persistence
👨‍💻 Author

Tirth Patel

Computer Science Engineering Graduate

GitHub: @TIRTH-25

⭐ Project Summary

ATM Banking System is a Python-based console application built to demonstrate practical Object-Oriented Programming through a realistic banking workflow. It combines inheritance, polymorphism, encapsulation, composition, persistence, transaction management, and error handling into a modular application.

If you found this project useful, feel free to ⭐ the repository.
