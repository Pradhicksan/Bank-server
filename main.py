from bank_server_class import BankServer

# retrieving the stored bank accounts and users list using "" module.
users_list = []
bank_accounts_list = []

bank_server = BankServer(users_list, bank_accounts_list)
loop_on = True

while loop_on:
    bank_server.home_service_provider()











