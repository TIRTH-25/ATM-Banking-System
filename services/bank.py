import json
import os

from models.bank_account import BankAccount
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.transaction import Transaction


class Bank:

    DATA_FILE = "data/accounts.json"

    def __init__(self, name):

        self.__name = name
        self.__accounts = []

    # =====================================================
    # BANK NAME
    # =====================================================

    def get_name(self):
        return self.__name

    # =====================================================
    # CREATE SAVINGS ACCOUNT
    # =====================================================

    def create_savings_account(
        self,
        account_holder,
        pin,
        initial_balance,
        min_balance=1000
    ):

        account = SavingsAccount(
            account_holder,
            pin,
            initial_balance,
            min_balance
        )

        self.__accounts.append(account)

        return account

    # =====================================================
    # CREATE CURRENT ACCOUNT
    # =====================================================

    def create_current_account(
        self,
        account_holder,
        pin,
        initial_balance,
        overdraft_limit=5000
    ):

        account = CurrentAccount(
            account_holder,
            pin,
            initial_balance,
            overdraft_limit
        )

        self.__accounts.append(account)

        return account

    # =====================================================
    # FIND ACCOUNT
    # =====================================================

    def find_account(self, account_number):

        for account in self.__accounts:

            if (
                account.get_account_number()
                == account_number
            ):
                return account

        return None

    # =====================================================
    # DEPOSIT
    # =====================================================

    def deposit(
        self,
        account_number,
        amount
    ):

        account = self.find_account(
            account_number
        )

        if account is None:
            raise ValueError(
                "Account not found."
            )

        balance = account.deposit(
            amount
        )

        transaction = Transaction(
            "DEPOSIT",
            amount,
            balance
        )

        account.add_transaction(
            transaction
        )

        self.save_accounts()

        return balance

    # =====================================================
    # WITHDRAW
    # =====================================================

    def withdraw(
        self,
        account_number,
        amount
    ):

        account = self.find_account(
            account_number
        )

        if account is None:
            raise ValueError(
                "Account not found."
            )

        # Polymorphism happens here
        #
        # If SavingsAccount:
        #     SavingsAccount.withdraw()
        #
        # If CurrentAccount:
        #     CurrentAccount.withdraw()

        balance = account.withdraw(
            amount
        )

        transaction = Transaction(
            "WITHDRAW",
            amount,
            balance
        )

        account.add_transaction(
            transaction
        )

        self.save_accounts()

        return balance

    # =====================================================
    # CHANGE PIN
    # =====================================================

    def change_pin(
        self,
        account_number,
        old_pin,
        new_pin
    ):

        account = self.find_account(
            account_number
        )

        if account is None:
            raise ValueError(
                "Account not found."
            )

        account.change_pin(
            old_pin,
            new_pin
        )

        self.save_accounts()

        return True

    # =====================================================
    # INTEREST
    # =====================================================

    def add_interest(
        self,
        account_number,
        rate=4.0
    ):

        account = self.find_account(
            account_number
        )

        if account is None:
            raise ValueError(
                "Account not found."
            )

        if not isinstance(
            account,
            SavingsAccount
        ):

            raise ValueError(
                "Interest is available only "
                "for Savings Accounts."
            )

        interest = account.add_interest(
            rate
        )

        transaction = Transaction(
            "INTEREST",
            interest,
            account.get_balance()
        )

        account.add_transaction(
            transaction
        )

        self.save_accounts()

        return interest

    # =====================================================
    # GET ACCOUNTS
    # =====================================================

    def get_accounts(self):

        return self.__accounts.copy()

    # =====================================================
    # SAVE
    # =====================================================

    def save_accounts(self):

        directory = os.path.dirname(
            self.DATA_FILE
        )

        if directory:
            os.makedirs(
                directory,
                exist_ok=True
            )

        data = [
            account.to_dict()
            for account in self.__accounts
        ]

        with open(
            self.DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # =====================================================
    # LOAD
    # =====================================================

    def load_accounts(self):

        if not os.path.exists(
            self.DATA_FILE
        ):
            return

        try:

            with open(
                self.DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

        except (
            json.JSONDecodeError,
            IOError
        ):

            print(
                "Warning: Could not read "
                "accounts.json."
            )

            return

        self.__accounts.clear()

        for entry in data:

            account_type = entry.get(
                "type"
            )

            if account_type == "SavingsAccount":

                account = (
                    SavingsAccount.from_dict(
                        entry
                    )
                )

            elif account_type == "CurrentAccount":

                account = (
                    CurrentAccount.from_dict(
                        entry
                    )
                )

            else:

                print(
                    f"Skipping unknown account "
                    f"type: {account_type}"
                )

                continue

            # -----------------------------------------
            # Restore transaction history
            # -----------------------------------------

            transactions = entry.get(
                "transactions",
                []
            )

            for transaction_data in transactions:

                transaction = (
                    Transaction.from_dict(
                        transaction_data
                    )
                )

                account.add_transaction(
                    transaction
                )

            self.__accounts.append(
                account
            )