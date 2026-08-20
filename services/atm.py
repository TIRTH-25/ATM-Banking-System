class ATM:

    def __init__(self, bank):

        self.__bank = bank

    # =====================================================
    # START
    # =====================================================

    def start(self):

        while True:

            self.show_welcome()

            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Login")
            print("4. Exit")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            try:

                if choice == "1":

                    self.create_savings_account()

                elif choice == "2":

                    self.create_current_account()

                elif choice == "3":

                    self.login()

                elif choice == "4":

                    self.__bank.save_accounts()

                    print(
                        "\nThank you for using "
                        "Fresher Bank!"
                    )

                    print(
                        "All data has been saved."
                    )

                    break

                else:

                    print(
                        "\nInvalid choice."
                    )

            except ValueError as error:

                print(
                    f"\n❌ Error: {error}"
                )

            except Exception as error:

                print(
                    f"\n❌ Unexpected error: "
                    f"{error}"
                )

    # =====================================================
    # WELCOME
    # =====================================================

    def show_welcome(self):

        print("\n" + "=" * 50)

        print(
            "       WELCOME TO FRESHER BANK"
        )

        print(
            "        ATM MANAGEMENT SYSTEM"
        )

        print("=" * 50)

    # =====================================================
    # CREATE SAVINGS
    # =====================================================

    def create_savings_account(self):

        print("\n" + "-" * 40)
        print("       CREATE SAVINGS ACCOUNT")
        print("-" * 40)

        name = input(
            "Enter account holder name: "
        ).strip()

        pin = input(
            "Create 4-digit PIN: "
        ).strip()

        initial_balance = self.get_amount(
            "Enter initial balance: ₹"
        )

        min_balance_input = input(
            "Minimum balance "
            "(default ₹1000): "
        ).strip()

        min_balance = (
            float(min_balance_input)
            if min_balance_input
            else 1000
        )

        account = (
            self.__bank.create_savings_account(
                name,
                pin,
                initial_balance,
                min_balance
            )
        )

        self.__bank.save_accounts()

        print(
            "\n✅ Savings account created!"
        )

        self.display_account_details(
            account
        )

    # =====================================================
    # CREATE CURRENT
    # =====================================================

    def create_current_account(self):

        print("\n" + "-" * 40)
        print("       CREATE CURRENT ACCOUNT")
        print("-" * 40)

        name = input(
            "Enter account holder name: "
        ).strip()

        pin = input(
            "Create 4-digit PIN: "
        ).strip()

        initial_balance = self.get_amount(
            "Enter initial balance: ₹"
        )

        overdraft_input = input(
            "Overdraft limit "
            "(default ₹5000): "
        ).strip()

        overdraft_limit = (
            float(overdraft_input)
            if overdraft_input
            else 5000
        )

        account = (
            self.__bank.create_current_account(
                name,
                pin,
                initial_balance,
                overdraft_limit
            )
        )

        self.__bank.save_accounts()

        print(
            "\n✅ Current account created!"
        )

        self.display_account_details(
            account
        )

    # =====================================================
    # ACCOUNT DETAILS
    # =====================================================

    def display_account_details(
        self,
        account
    ):

        print("\n" + "-" * 40)

        print(
            f"Account Number : "
            f"{account.get_account_number()}"
        )

        print(
            f"Account Holder : "
            f"{account.get_account_holder()}"
        )

        print(
            f"Account Type   : "
            f"{account.__class__.__name__}"
        )

        print(
            f"Balance        : "
            f"₹{account.get_balance():.2f}"
        )

        print("-" * 40)

    # =====================================================
    # LOGIN
    # =====================================================

    def login(self):

        print("\n" + "-" * 40)
        print("              LOGIN")
        print("-" * 40)

        try:

            account_number = int(
                input(
                    "Enter account number: "
                ).strip()
            )

        except ValueError:

            print(
                "\n❌ Account number must "
                "be numeric."
            )

            return

        pin = input(
            "Enter PIN: "
        ).strip()

        account = self.__bank.find_account(
            account_number
        )

        if account is None:

            print(
                "\n❌ Account not found."
            )

            return

        if not account.verify_pin(pin):

            print(
                "\n❌ Wrong PIN."
            )

            return

        print(
            "\n✅ Login successful!"
        )

        self.account_menu(account)

    # =====================================================
    # ACCOUNT MENU
    # =====================================================

    def account_menu(self, account):

        while True:

            print("\n" + "=" * 45)

            print(
                f"Welcome, "
                f"{account.get_account_holder()}"
            )

            print("=" * 45)

            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Transaction History")

            if account.__class__.__name__ == (
                "SavingsAccount"
            ):

                print("6. Add Interest")
                print("7. Logout")

            else:

                print("6. Logout")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            try:

                if choice == "1":

                    self.check_balance(
                        account
                    )

                elif choice == "2":

                    self.deposit(
                        account
                    )

                elif choice == "3":

                    self.withdraw(
                        account
                    )

                elif choice == "4":

                    self.change_pin(
                        account
                    )

                elif choice == "5":

                    self.show_transactions(
                        account
                    )

                elif (
                    choice == "6"
                    and account.__class__.__name__
                    == "SavingsAccount"
                ):

                    self.add_interest(
                        account
                    )

                elif (
                    choice == "7"
                    and account.__class__.__name__
                    == "SavingsAccount"
                ):

                    print(
                        "\n✅ Logged out."
                    )

                    break

                elif (
                    choice == "6"
                    and account.__class__.__name__
                    == "CurrentAccount"
                ):

                    print(
                        "\n✅ Logged out."
                    )

                    break

                else:

                    print(
                        "\n❌ Invalid choice."
                    )

            except ValueError as error:

                print(
                    f"\n❌ Error: {error}"
                )

    # =====================================================
    # BALANCE
    # =====================================================

    def check_balance(
        self,
        account
    ):

        print("\n" + "-" * 40)

        print(
            f"Current Balance: "
            f"₹{account.get_balance():.2f}"
        )

        print("-" * 40)

    # =====================================================
    # DEPOSIT
    # =====================================================

    def deposit(
        self,
        account
    ):

        amount = self.get_amount(
            "Enter deposit amount: ₹"
        )

        balance = self.__bank.deposit(
            account.get_account_number(),
            amount
        )

        print(
            f"\n✅ Deposit successful."
        )

        print(
            f"Current Balance: "
            f"₹{balance:.2f}"
        )

    # =====================================================
    # WITHDRAW
    # =====================================================

    def withdraw(
        self,
        account
    ):

        amount = self.get_amount(
            "Enter withdrawal amount: ₹"
        )

        balance = self.__bank.withdraw(
            account.get_account_number(),
            amount
        )

        print(
            f"\n✅ Withdrawal successful."
        )

        print(
            f"Current Balance: "
            f"₹{balance:.2f}"
        )

    # =====================================================
    # CHANGE PIN
    # =====================================================

    def change_pin(
        self,
        account
    ):

        old_pin = input(
            "Enter old PIN: "
        ).strip()

        new_pin = input(
            "Enter new PIN: "
        ).strip()

        self.__bank.change_pin(
            account.get_account_number(),
            old_pin,
            new_pin
        )

        print(
            "\n✅ PIN changed successfully."
        )

    # =====================================================
    # INTEREST
    # =====================================================

    def add_interest(
        self,
        account
    ):

        rate_input = input(
            "Interest rate "
            "(default 4%): "
        ).strip()

        rate = (
            float(rate_input)
            if rate_input
            else 4.0
        )

        interest = self.__bank.add_interest(
            account.get_account_number(),
            rate
        )

        print(
            f"\n✅ Interest added: "
            f"₹{interest:.2f}"
        )

        print(
            f"Current Balance: "
            f"₹{account.get_balance():.2f}"
        )

    # =====================================================
    # TRANSACTION HISTORY
    # =====================================================

    def show_transactions(
        self,
        account
    ):

        transactions = (
            account.get_transactions()
        )

        print("\n" + "=" * 80)

        print(
            "                  TRANSACTION HISTORY"
        )

        print("=" * 80)

        if not transactions:

            print(
                "No transactions found."
            )

            print("=" * 80)

            return

        for transaction in transactions:

            print(transaction)

        print("=" * 80)

    # =====================================================
    # INPUT HELPER
    # =====================================================

    @staticmethod
    def get_amount(message):

        try:

            amount = float(
                input(message).strip()
            )

        except ValueError:

            raise ValueError(
                "Please enter a valid amount."
            )

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        return amount