from models.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    Savings account.

    Rule:
    Minimum balance must always be maintained.
    """

    def __init__(
        self,
        account_holder,
        pin,
        initial_balance=0,
        min_balance=1000
    ):

        if min_balance < 0:
            raise ValueError(
                "Minimum balance cannot be negative."
            )

        if initial_balance < min_balance:
            raise ValueError(
                f"Initial balance must be at least "
                f"₹{min_balance}."
            )

        super().__init__(
            account_holder,
            pin,
            initial_balance
        )

        self.__min_balance = float(
            min_balance
        )

    # =====================================================
    # METHOD OVERRIDING
    # =====================================================

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if (
            self.get_balance() - amount
            < self.__min_balance
        ):

            raise ValueError(
                f"Withdrawal denied. "
                f"Minimum balance of ₹"
                f"{self.__min_balance:.2f} "
                f"must be maintained."
            )

        return super().withdraw(amount)

    # =====================================================
    # INTEREST
    # =====================================================

    def add_interest(self, rate=4.0):

        if rate <= 0:
            raise ValueError(
                "Interest rate must be greater than zero."
            )

        interest = (
            self.get_balance()
            * rate
            / 100
        )

        self.deposit(interest)

        return interest

    # =====================================================
    # GETTER
    # =====================================================

    def get_min_balance(self):
        return self.__min_balance

    # =====================================================
    # JSON
    # =====================================================

    def to_dict(self):

        data = super().to_dict()

        data["min_balance"] = (
            self.__min_balance
        )

        return data

    # =====================================================
    # RESTORE
    # =====================================================

    @classmethod
    def from_dict(cls, data):

        account = cls.__new__(cls)

        BankAccount._restore_base_fields(
            account,
            data
        )

        account._SavingsAccount__min_balance = (
            float(data["min_balance"])
        )

        return account