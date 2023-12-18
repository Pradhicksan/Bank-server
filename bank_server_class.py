import bank_account_class
import user_class


class BankServer:
    def __init__(self, list_1, list_2):
        self.users_list = list_1
        self.bank_accounts_list = list_2

    def user_info_updater(self):
        """checks whether the user is a valid one and helps make change their details"""
        identification_number = input("Enter user identification number: ")
        profile_password = input("Enter your profile password: ")
        match_found = False
        for user in self.users_list:
            if user.user_identification_number == identification_number:
                if user.user_profile_password == profile_password:
                    match_found = True
                    to_be_changed = input("What do you want to change? \n 1 for user first name \n"
                                          " 2 for user second name \n"
                                          "  3 for user age \n 4 for user occupation \n 5 for user profile password")
                    if to_be_changed == 1:
                        new_first_name = input("Enter the new first name: ")
                        user.user_first_name = new_first_name
                        print("\n")
                    elif to_be_changed == 2:
                        new_last_name = input("Enter the new last name: ")
                        print("\n")
                        user.user_last_name = new_last_name
                    elif to_be_changed == 3:
                        new_age = input("Enter the new age ")
                        user.user_age = new_age
                        print("\n")
                    elif to_be_changed == 5:
                        new_profile_password = input("Enter the new last name: ")
                        user.user_profile_password = new_profile_password
                        print("\n")
                    else:
                        new_occupation = input("Enter your new occupation: ")
                        user.user_occupation = new_occupation
                        print("\n")

                else:
                    print("Invalid password! Try again from the start.\n")
                    self.user_info_updater()
        if not match_found:
            print("No such user! Try again.")
            self.user_info_updater()
        print("Change has been done successfully!\n")

    def password_checker(self):
        """checks if the password entered matches with the confirmation password entered"""
        password = input("Enter your password:")
        confirmation_password = input("Renter your password: ")
        if password == confirmation_password:
            print("Passwords match. Password set!\n")
            return password
        else:
            print("Passwords don't match! Please try entering password again.\n")
            self.password_checker()

    def user_identification_number_creator(self):
        """checks how many users are there and creates a unique user number"""
        number_of_users = len(self.users_list)+1
        number_of_digits = len(f"{number_of_users}")
        identification_number = ""
        for i in range(16 - number_of_digits):
            identification_number += "0"
        identification_number = identification_number + f"{number_of_users}"
        return identification_number

    def want_to_create_account(self):
        """asks the user if they would want to create the bank account after creating user"""
        create_account = input("Do you want to proceed creating an account?(y/n)")
        if create_account == 'y':
            self.create_a_bank_account()
        elif create_account == 'n':
            pass
        else:
            print("Invalid response! Please type again!\n")
            self.want_to_create_account()

    def account_number_creator(self):
        """checks how many users are there and creates a unique user number"""
        number_of_users = len(self.bank_accounts_list)
        number_of_digits = len(f"{number_of_users}")
        account_number = ""
        for i in range(16-number_of_digits):
            account_number += "0"
        account_number = account_number + f"{number_of_users}"
        return account_number

    def create_a_user(self):
        """creates a user"""
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        occupation = input("Enter your occupation: ")
        print("CAUTION! \nYou are about to to set your user profile password. Please remember this password"
              " and don't share it with others.")
        profile_password = self.password_checker()
        user_identification_number = self.user_identification_number_creator()
        new_user = user_class.User(first_name, last_name, age, occupation, user_identification_number, profile_password)
        self.users_list.append(new_user)
        print(user_identification_number)
        print("User creation successful! It is recommended to create an account.")
        self.want_to_create_account()

    def create_a_bank_account(self):
        """Creates a bank account"""
        number = self.account_number_creator()
        print("CAUTION! \nYou are about to to set your user account password. Please remember this password"
              " and don't share it with others.")
        password = self.password_checker()
        user_identification_number = self.user_number_checker()
        new_account = bank_account_class.BankAccount(number, password, user_identification_number)
        self.bank_accounts_list.append(new_account)
        print("Your account was successfully created!\n")

    def account_details_authorizer(self, is_authorised):
        """Checks whether the entered account credentials and passwords match
        and return the account object in case of matching"""
        account_number_input = input("Enter your account number: ")
        account_password_input = input("Enter your account password: ")
        account_found = False
        account_object = ""
        for account in self.bank_accounts_list:
            if account.account_number == account_number_input:
                if account.account_password == account_password_input:
                    account_found = True
                    is_authorised = True
                    account_object = account
                else:
                    print("Wrong password! Try again from the start!")
                    self.account_details_authorizer(is_authorised)

        if not account_found:
            print("Invalid Account number. Please reenter your account details!")
            self.account_details_authorizer(is_authorised)
        if is_authorised and account_found:
            return is_authorised, account_object

    def home_service_provider(self):
        """Asks what service the user wants and directs them"""
        user_input_code = int(input("Hi! Welcome to Python bank! Our services are listed below:\n"
                                    "1 To withdraw money \n"
                                    "2 To transfer money\n"
                                    "3 To deposit money\n"
                                    "4 To add user name\n"
                                    "5 To add an account\n"
                                    "6 To update details of a username\n"
                                    "7 To check account history\n"
                                    "Please select the appropriate number:"))

        if user_input_code == 1:
            auth_status = False
            auth_status, account_object = self.account_details_authorizer(auth_status)
            account_object.withdraw()

        elif user_input_code == 2:
            auth_status = False
            auth_status, sender_account_object = self.account_details_authorizer(auth_status)
            receiver_account_object = self.account_number_checker()
            sender_account_object.transfer(receiver_account_object)

        elif user_input_code == 3:
            auth_status = False
            auth_status, account_object = self.account_details_authorizer(auth_status)
            amount_input = int(input("Enter the amount you are to deposit: "))
            account_object.deposit(amount_input)

        elif user_input_code == 4:
            self.create_a_user()

        elif user_input_code == 5:
            self.create_a_bank_account()

        elif user_input_code == 6:
            self.user_info_updater()

        elif user_input_code == 7:
            pass

        else:
            print("You entered an invalid service code! Please try again!\n")
            self.home_service_provider()

    def account_number_checker(self):
        """checks if the account number entered exists"""
        receiver_account_number = input("Enter your profile password: ")
        match_found = False
        for account in self.bank_accounts_list:
            if account.account_number == receiver_account_number:
                match_found = True
                return account
        if not match_found:
            print("Invalid bank account! Please enter your account number again.\n")
            self.account_number_checker()

    def user_number_checker(self):
        identification_number = input("Enter your user identification number: ")
        print(identification_number)
        match_found = False
        print(self.users_list)
        print(self.users_list[0].user_identification_number)
        for user in self.users_list:
            if user.user_identification_number == identification_number:
                match_found = True
                return identification_number
        if not match_found:
            print("Invalid user identification number. Please enter your user identification number again.\n")
            self.user_number_checker()





