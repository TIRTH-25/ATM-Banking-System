from models.bank_account import BankAccount


class CurrentAccount(BankAccount):
    """
    Current account.

    Allows overdraft up to a fixed limit.
    """

    def __init__(
        self,
        account_holder,
        pin,
        initial_balance=0,
        overdraft_limit=5000
    ):

        if overdraft_limit < 0:
            raise ValueError(
                "Overdraft limit cannot be negative."
            )

        super().__init__(
            account_holder,
            pin,
            initial_balance
        )

        self.__overdraft_limit = float(
            overdraft_limit
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
            < -self.__overdraft_limit
        ):

            raise ValueError(
                f"Withdrawal denied. "
                f"Overdraft limit of ₹"
                f"{self.__overdraft_limit:.2f} "
                f"exceeded."
            )

        return self._apply_withdrawal(
            amount
        )

    # =====================================================
    # GETTER
    # =====================================================

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    # =====================================================
    # JSON
    # =====================================================

    def to_dict(self):

        data = super().to_dict()

        data["overdraft_limit"] = (
            self.__overdraft_limit
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

        account._CurrentAccount__overdraft_limit = (
            float(data["overdraft_limit"])
        )

        return account