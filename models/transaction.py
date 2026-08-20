from datetime import datetime


class Transaction:

    transaction_counter = 0

    def __init__(
        self,
        transaction_type,
        amount,
        balance_after
    ):

        Transaction.transaction_counter += 1

        self.__transaction_id = (
            Transaction.transaction_counter
        )

        self.__transaction_type = (
            transaction_type
        )

        self.__amount = float(amount)

        self.__balance_after = float(
            balance_after
        )

        self.__timestamp = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

    # =====================================================
    # GETTERS
    # =====================================================

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_balance_after(self):
        return self.__balance_after

    def get_timestamp(self):
        return self.__timestamp

    # =====================================================
    # STRING
    # =====================================================

    def __str__(self):

        return (
            f"#{self.__transaction_id:<4} | "
            f"{self.__transaction_type:<10} | "
            f"₹{self.__amount:<10.2f} | "
            f"Balance: ₹{self.__balance_after:<10.2f} | "
            f"{self.__timestamp}"
        )

    # =====================================================
    # JSON
    # =====================================================

    def to_dict(self):

        return {
            "transaction_id":
                self.__transaction_id,

            "transaction_type":
                self.__transaction_type,

            "amount":
                self.__amount,

            "balance_after":
                self.__balance_after,

            "timestamp":
                self.__timestamp
        }

    # =====================================================
    # RESTORE
    # =====================================================

    @classmethod
    def from_dict(cls, data):

        transaction = cls.__new__(cls)

        transaction._Transaction__transaction_id = (
            int(data["transaction_id"])
        )

        transaction._Transaction__transaction_type = (
            data["transaction_type"]
        )

        transaction._Transaction__amount = float(
            data["amount"]
        )

        transaction._Transaction__balance_after = float(
            data["balance_after"]
        )

        transaction._Transaction__timestamp = (
            data["timestamp"]
        )

        # VERY IMPORTANT
        # Prevent duplicate transaction IDs
        Transaction.transaction_counter = max(
            Transaction.transaction_counter,
            int(data["transaction_id"])
        )

        return transaction