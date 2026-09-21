"""
Author: Gerard Ortiz
Date: 9/20/2026
Tier Level: Base

Description:
This program saves expense records to a plain text file and reads them back. 
Each record will store a date, a short description, a dollar amount, and a category
"""

import os
import datetime

"""
creates a record with date(datetime), description, amount to 2 decimal places, and categeory
joined using ","
"""
def build_record(description, amount, category):
    record_date = str(datetime.date.today())
    sliced_description = description[:30]
    formated_amount = f"{amount:.2f}"
    record = ",".join([record_date, sliced_description, "$"+formated_amount, category])
    return record
"""
Opens expenses.txt(expense report) in read mode and returns the lines as expense records
"""
def load_records():
    records = []
    try:
        file = open("expenses.txt", 'r')
        for record in file.readlines():
            record_lines = record.strip().split(",")
            records.append(record_lines)
    except FileNotFoundError:
        records = []
    return records

"""
takes the records list formats and display's all expense records in a readable, aligned format
"""
def display_records(records):
    print("\n"+"="*5, " Your Expense Records ", "="*5, "\n")
    if records != []:
        print(f"{'Date':<12}{'Description':<30}{'Amount':>10}  {'Category':<15}")
        print("-"*67)
        for record in records:
            date = record[0]
            description = record[1]
            amount = record[2]
            category = record[3]
            print(f"{date:<12}{description:<30}{amount:>10}  {category:<15}")
        print("\n"+"="*5,"end of expense record", "="*5, "\n")
    else:
        print("No expenses on record yet")

#print(os.getcwd())
"""
Main body. displays existing expense reports. asks the user to input number of expenses to be added.
Loops through until all lines are added.
"""
records = load_records()
display_records(records)
record_count = int(input("How many expenses do want to add? "))
expense_count = 1
for i in range (record_count):
    print("\nExpense ", expense_count)
    description = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category: ").title()
    new_expense_record = build_record(description, amount, category)
    records = open("expenses.txt", 'a')
    records.write(new_expense_record+ "\n")
    expense_count = expense_count + 1
records.close()

updated_expenses = load_records()
display_records(updated_expenses)
