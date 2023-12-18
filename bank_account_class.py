import datetime as dt


class BankAccount:
    def __init__(self, number, password, user_identification_number):
        self.account_number = number
        self.account_password = password
        self.account_balance = 0
        self.account_user_identification_number = user_identification_number
        self.transaction_history_list = []
        # transaction history key => transfer amount, time of transfer, type of transfer, from, to, balance

    def update_account(self):
        pass

    def withdraw(self):
        amount_needed = int(input("Enter the amount you want: "))
        if self.check_enough_fund(amount_needed):
            self.account_balance -= amount_needed
            transfer_dictionary = {
                "Amount": amount_needed,
                "Balance": self.account_balance,
                "Time_of_transfer": self.date_time_finder(),
                "Type_of_transfer": "Withdrawl",
                "From": self.account_number,
                "To": None,
            }
            self.transaction_history_list.append(transfer_dictionary)
            print(f"Here is your money, {amount_needed} rupees.")
        else:
            print(f"No enough fund! Only {self.account_balance} is available. Try again!")
            self.withdraw()

    def transfer(self, account_object):
        money_demanded = int(input("Enter the amount that you want to transfer: "))
        if self.check_enough_fund(money_demanded):
            self.account_balance -= money_demanded
            account_object.account_balance += money_demanded
            transfer_dictionary = {
                "Amount": money_demanded,
                "Balance": self.account_balance,
                "Time_of_transfer": self.date_time_finder(),
                "Type_of_transfer": "Transfer",
                "From": self.account_number,
                "To": account_object.account_number,
            }
            receiver_dictionary = {
                "Amount": money_demanded,
                "Balance": account_object.account_balance,
                "Time_of_transfer": self.date_time_finder(),
                "Type_of_transfer": "Transfer",
                "From": self.account_number,
                "To": account_object.account_number,
            }
            account_object.transaction_history_list.append(receiver_dictionary)
            self.transaction_history_list.append(transfer_dictionary)
            print(f"Transfer of {money_demanded} rupees to account number {account_object} is successful.")
        else:
            print(f"No enough fund! Only {self.account_balance} is available. Try again!")
            self.transfer(account_object)

    def deposit(self, input_fund):
        self.account_balance += input_fund
        transfer_dictionary = {
            "Amount": input_fund,
            "Balance": self.account_balance,
            "Time_of_transfer": self.date_time_finder(),
            "Type_of_transfer": "Deposit",
            "From": None,
            "To": self.account_number,
        }
        print("Your money is successfully deposited!")

    def check_enough_fund(self, money_needed):
        return money_needed <= self.account_balance

    def date_time_finder(self):
        datetime = dt.datetime
        return datetime.now



