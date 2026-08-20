from services.bank import Bank
from services.atm import ATM


def main():

    bank = Bank("Fresher Bank")

    # Load previous data
    bank.load_accounts()

    atm = ATM(bank)

    try:

        atm.start()

    except KeyboardInterrupt:

        print(
            "\n\nProgram interrupted."
        )

        bank.save_accounts()

        print(
            "✅ Progress saved."
        )

    except Exception as error:

        bank.save_accounts()

        print(
            f"\nUnexpected error: {error}"
        )


if __name__ == "__main__":
    main()