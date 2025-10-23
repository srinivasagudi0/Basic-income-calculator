# 💰 Sales and Income Calculator

A simple **Python console program** that helps you record item sales, calculate total income, subtract expenses, and display your final **net income** — all in a clean, step-by-step format.

---

## 🧾 Features

- Prompts for the number of items sold  
- Accepts each item’s name and earnings  
- Calculates and displays:
  - Each item’s earned amount
  - Total income
  - Staff and other expenses
  - Final **net income**
- Handles invalid input gracefully with error messages  
- Clean program termination message with a pause before exit

---

## 🖥️ Example Run

Enter the number of items you sold:

3

Enter name of item 1: Coffee
Earned from Coffee: $120
Enter name of item 2: Tea
Earned from Tea: $80
Enter name of item 3: Cake
Earned from Cake: $200

Earned amount:
Coffee $120.00
Tea $80.00
Cake $200.00

Total income: $400.00

Please enter the following expenses:
Staff expenses: $150
Other expenses: $50

✅ Net income: $200.00

--- Calculation complete ---
Press Enter to exit...

yaml
Copy code

---

## 🧠 How It Works

1. Asks how many items were sold.  
2. Stores each item’s name and earnings in a Python dictionary.  
3. Uses `sum()` to calculate total income.  
4. Prompts for two expense types: staff and other.  
5. Computes **net income = income − (staff + other)**.  
6. Displays formatted results with two decimal places.

---

## ⚙️ Requirements

- Python 3.6 or higher  
- No external libraries required (uses only built-in functions)

---

## 🚀 How to Run

1. Save the file as `income_calculator.py`.
2. Open a terminal or command prompt.
3. Run:

   ```bash
   python income_calculator.py
Follow the on-screen prompts.

🧩 Code Highlights
python
Copy code
# Calculate total income
income = sum(items.values())

# Display all earned amounts
for name, amount in items.items():
    print(f"{name:<15} ${amount:.2f}")

# Calculate and display net income
leftover = income - (staff + other)
print(f"\n✅ Net income:    ${leftover:.2f}")
🧱 Error Handling
If a user enters invalid input (like a letter instead of a number),
the program shows a friendly message and exits cleanly:

pgsql
Copy code
❌ Please enter valid numbers only.
--- Calculation complete ---
📜 License
This project is released under the MIT License.
Feel free to modify and use for personal or educational purposes.

👨‍💻 Author
Srinivasa
Built as part of a Python learning and practice exercise.
