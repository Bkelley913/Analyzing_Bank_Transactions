# Define a list of transactions in cents
transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]

# Function to print transactions based on the given range
def print_transactions_between(transactions, min_value, max_value):
  # Filter transactions based on the given range
  filtered_transactions = [transaction for transaction in transactions if min_value <= transaction <= max_value]
  
  # Print the filtered transactions
  print("Transactions between", min_value, "and", max_value, ":")
  print(filtered_transactions)

# Print the original transactions in cents  
print('Transactions (cents):')
print(transactions_in_cents)

# Convert transactions to dollars and sort them
transactions = [transactions / 100 for transactions in transactions_in_cents]
transactions.sort()

# Separate deposits and withdrawals
deposits = [deposits for deposits in transactions if deposits >= 0]
withdrawals = [withdrawals for withdrawals in transactions if withdrawals < 0]

# Print deposits and withdrawals
print('Deposits:')
print(deposits)
print('Withdrawals:')
print(withdrawals)

# Function to invert negative numbers
def invert_negative_num(negative_num):
  positive_num = negative_num * -1
  return positive_num

# Invert negative numbers in withdrawals list
withdrawals = [invert_negative_num(withdrawal) for withdrawal in withdrawals]

# Print withdrawals with positive values
print("Withdrawals (positive values):")
print(withdrawals)

# Get the largest withdrawals
largest_withdrawals = withdrawals[0:5]

# Print the largest withdrawals
print("Largest Withdrawals:")
print(largest_withdrawals)

# Calculate average deposit
average_deposit = sum(deposits) / len(deposits)
average_deposit = int(average_deposit)

# Calculate average withdrawals
average_withdrawal = sum(withdrawals) / len(withdrawals)
average_withdrawal = int(average_withdrawal)

# Print the average deposit and withdrawal as integers
print("Average Deposit (int):")
print(average_deposit)
print("Average Withdrawal (int):")
print(average_withdrawal)

# Calculate the balance
balance = sum(transactions)

# Print the balance
print("Balance:")
print(balance)

# Calculate the running balance
final_balance = 0
running_balance = []

for transaction in transactions:
  final_balance += transaction
  running_balance.append(balance)

# Print the running balance
print("Running Balance:")
print(running_balance)
