import hashlib


class BankAccount:
    """
    Base class for all bank accounts.

    Demonstrates:
    - Encapsulation
    - Constructor
    - Class variable
    - Class method
    - Static method
    - Getters / Setters
    - Magic methods
    - Protected method
    """

    account_counter = 100000

    def __init__(self, account_holder, pin, initial_balance=0):

        if not self.validate_name(account_holder):
            raise ValueError("Account holder name cannot be empty.")

        if not self.validate_pin(pin):
            raise ValueError("PIN must be exactly 4 digits.")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.__account_number = BankAccount.generate_account_number()
        self.__account_holder = account_holder.strip()
        self.__pin_hash = self._hash_pin(pin)
        self.__balance = float(initial_balance)
        self.__transactions = []

    # =====================================================
    # CLASS METHOD
    # =====================================================

    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter

    # =====================================================
    # STATIC METHODS
    # =====================================================

    @staticmethod
    def validate_name(name):
        return (
            isinstance(name, str)
            and bool(name.strip())
        )

    @staticmethod
    def validate_pin(pin):
        return (
            isinstance(pin, str)
            and len(pin) == 4
            and pin.isdigit()
        )

    @staticmethod
    def _hash_pin(pin):
        return hashlib.sha256(
            pin.encode()
        ).hexdigest()

    # =====================================================
    # DEPOSIT
    # =====================================================

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self.__balance += amount

        return self.__balance

    # =====================================================
    # WITHDRAW
    # =====================================================

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.__balance:
            raise ValueError(
                "Insufficient balance."
            )

        self.__balance -= amount

        return self.__balance

    # =====================================================
    # PROTECTED WITHDRAWAL HELPER
    # =====================================================

    def _apply_withdrawal(self, amount):

        self.__balance -= amount

        return self.__balance

    # =====================================================
    # BALANCE
    # =====================================================

    def check_balance(self):
        return self.__balance

    def get_balance(self):
        return self.__balance

    # =====================================================
    # PIN
    # =====================================================

    def verify_pin(self, pin):

        return (
            self.__pin_hash
            == self._hash_pin(pin)
        )

    def change_pin(self, old_pin, new_pin):

        if not self.verify_pin(old_pin):
            raise ValueError(
                "Old PIN is incorrect."
            )

        if not self.validate_pin(new_pin):
            raise ValueError(
                "New PIN must be exactly 4 digits."
            )

        if old_pin == new_pin:
            raise ValueError(
                "New PIN must be different from old PIN."
            )

        self.__pin_hash = self._hash_pin(
            new_pin
        )

        return True

    def set_pin(self, new_pin):

        if not self.validate_pin(new_pin):
            raise ValueError(
                "PIN must be exactly 4 digits."
            )

        self.__pin_hash = self._hash_pin(
            new_pin
        )

    # =====================================================
    # GETTERS
    # =====================================================

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_pin(self):
        return self.__pin_hash

    # =====================================================
    # TRANSACTIONS
    # =====================================================

    def add_transaction(self, transaction):

        self.__transactions.append(
            transaction
        )

    def get_transactions(self):

        return self.__transactions.copy()

    # =====================================================
    # MAGIC METHODS
    # =====================================================

    def __str__(self):

        return (
            f"Account #{self.__account_number} - "
            f"{self.__account_holder} - "
            f"{self.__class__.__name__}"
        )

    def __eq__(self, other):

        if not isinstance(other, BankAccount):
            return False

        return (
            self.get_account_number()
            == other.get_account_number()
        )

    # =====================================================
    # JSON SERIALIZATION
    # =====================================================

    def to_dict(self):

        return {
            "type": self.__class__.__name__,
            "account_number": self.__account_number,
            "account_holder": self.__account_holder,
            "pin_hash": self.__pin_hash,
            "balance": self.__balance,

            "transactions": [
                transaction.to_dict()
                for transaction in self.__transactions
            ]
        }

    # =====================================================
    # RESTORE ACCOUNT
    # =====================================================

    @classmethod
    def _restore_base_fields(cls, account, data):

        account._BankAccount__account_number = data[
            "account_number"
        ]

        account._BankAccount__account_holder = data[
            "account_holder"
        ]

        account._BankAccount__pin_hash = data[
            "pin_hash"
        ]

        account._BankAccount__balance = float(
            data["balance"]
        )

        account._BankAccount__transactions = []

        BankAccount.account_counter = max(
            BankAccount.account_counter,
            int(data["account_number"])
        )