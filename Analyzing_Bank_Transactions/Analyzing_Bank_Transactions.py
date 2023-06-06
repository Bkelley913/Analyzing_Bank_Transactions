transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]

def print_transactions_between(transactions, min_value, max_value):
  filtered_transactions = [transaction for transaction in transactions if min_value <= transaction <= max_value]
  print("Transactions between", min_value, "and", max_value, ":")
  print(filtered_transactions)
  
print('Transactions (cents):')
print(transactions_in_cents)

transactions = [transactions / 100 for transactions in transactions_in_cents]
transactions.sort()

deposits = [deposits for deposits in transactions if deposits >= 0]
withdrawals = [withdrawals for withdrawals in transactions if withdrawals < 0]

print('Deposits:')
print(deposits)
print('Withdrawals:')
print(withdrawals)

def invert_negative_num(negative_num):
  positive_num = negative_num * -1
  return positive_num

withdrawals = [invert_negative_num(withdrawal) for withdrawal in withdrawals]

print("Withdrawals (positive values):")
print(withdrawals)

largest_withdrawals = withdrawals[0:5]

print("Largest Withdrawals:")
print(largest_withdrawals)

average_deposit = sum(deposits) / len(deposits)
average_deposit = int(average_deposit)

average_withdrawal = sum(withdrawals) / len(withdrawals)
average_withdrawal = int(average_withdrawal)

print("Average Deposit (int):")
print(average_deposit)
print("Average Withdrawal (int):")
print(average_withdrawal)

balance = sum(transactions)

print("Balance:")
print(balance)

final_balance = 0
running_balance = []

for transaction in transactions:
  final_balance += transaction
  running_balance.append(balance)

print("Running Balance:")
print(running_balance)
