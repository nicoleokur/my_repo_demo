from bank_account import BankAccount

account1 = BankAccount(123, 100) # bank account, balance
account2 = BankAccount(1234, 101) # bank account, balance

print(account1)
print(account2)

account1.deposit(10)
account2.withdraw(20)

print(account1)
print(account2)

total = account1.balance + account2.balance

print(f"total: {total}")