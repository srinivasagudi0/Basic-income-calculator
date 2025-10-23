print("Enter the number of items you sold:")
try:
    num_items = int(input("> "))
    if num_items <= 0:
        raise ValueError

    items = {}
    for i in range(num_items):
        name = input(f"\nEnter name of item {i + 1}: ").strip().title()
        amount = float(input(f"  Earned from {name}: $"))
        items[name] = amount

    # Calculate total income
    income = sum(items.values())

    # Display all earned amounts
    print("\nEarned amount:")
    for name, amount in items.items():
        print(f"{name:<15} ${amount:.2f}")
    print(f"\nTotal income:     ${income:.2f}\n")

    # Get expenses
    print("Please enter the following expenses:")
    staff = float(input("  Staff expenses: $"))
    other = float(input("  Other expenses: $"))

    # Calculate and display net income
    leftover = income - (staff + other)
    print(f"\n✅ Net income:    ${leftover:.2f}")

except ValueError:
    print("\n❌ Please enter valid numbers only.")
finally:
    print("\n--- Calculation complete ---")
    input("\nPress Enter to exit...")
