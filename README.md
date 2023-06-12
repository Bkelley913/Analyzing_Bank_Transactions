# Analyzing_Bank_Transactions

This code performs analysis on a list of bank transactions. It calculates various statistics such as deposits, withdrawals, largest withdrawals, average deposit, average withdrawal, balance, and running balance. Below is an overview of the code and its functionality.

# Code Overview
## Transaction Data
The code begins by defining a list 'transactions_in_cents' that represents the bank transactions in cents.

## Printing Transactions within a Range
The 'print_transactions_between' function is defined to print the transactions that fall within a specified range. It filters the transactions based on the given range and prints the filtered transactions.

## Converting and Sorting Transactions
The original transactions are in cents, so the code converts them to dollars by dividing each transaction by 100. The converted transactions are then sorted in ascending order.

## Separating Deposits and Withdrawals
The code separates the transactions into two lists: 'deposits' and 'withdrawals'. Deposits are transactions with a value greater than or equal to 0, and withdrawals are transactions with a negative value.

## Inverting Negative Numbers
The 'invert_negative_num' function is defined to invert negative numbers. It takes a negative number as input and returns its positive counterpart. This function is used to invert the negative values in the 'withdrawals' list.

## Printing Deposits and Withdrawals
The code prints the lists of deposits and withdrawals.

## Finding Largest Withdrawals
The code selects the five largest values from the 'withdrawals' list and stores them in the 'largest_withdrawals' list.

## Calculating Average Deposit and Withdrawal
The code calculates the average deposit by summing all the deposits and dividing by the number of deposits. Similarly, it calculates the average withdrawal by summing all the positive withdrawals (inverted negative values) and dividing by the number of withdrawals. The calculated averages are then converted to integers.

## Calculating Balance and Running Balance
The code calculates the balance by summing all the transactions. It also calculates the running balance by iterating over the transactions and appending the running balance at each step to a 'running_balance' list.

## Usage
To use this code, simply run the script. It will display the output for the various calculations and print the results to the console.

Feel free to modify the 'transactions_in_cents' list or customize the code to suit your specific needs.
