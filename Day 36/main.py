menu = {
    "Espresso": 120,
    "Cappuccino": 180,
    "Latte": 200,
    "Brownie": 90,
    "Sandwich": 150
}
order = []

def show_menu():
    print("\n    MENU ")
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item:12} ₹{menu[item]}")

def add_item():
    show_menu()

    choice = int(input("Choose item number: "))
    quantity = int(input("Quantity: "))

    items = list(menu.keys())

    if 1 <= choice <= len(items):
        name = items[choice - 1]
        price = menu[name]
        order.append({
            "item": name,
            "qty": quantity,
            "price": price,
            "total": price * quantity
        })
        print(" Added to order")
    else:
        print("Invalid choice")


def generate_bill(customer):
    print("\n" + "=" * 34)
    print("         CAFÉ RECEIPT")
    print("=" * 34)
    print(f"Customer : {customer}\n")
    subtotal = 0
    print(f"{'Item':12}{'Qty':>5}{'Total':>10}")
    print("-" * 34)

    for item in order:
        subtotal += item["total"]
        print(f"{item['item']:12}{item['qty']:>5}{item['total']:>10}")

    gst = subtotal * 0.05
    grand = subtotal + gst
    print("-" * 34)
    print(f"{'Subtotal':17} ₹{subtotal:.2f}")
    print(f"{'GST (5%)':17} ₹{gst:.2f}")
    print(f"{'Grand Total':17} ₹{grand:.2f}")
    print("=" * 34)

customer = input("Customer Name: ")
while True:
    add_item()
    more = input("\nAdd another item? (y/n): ").lower()
    if more != "y":
        break

generate_bill(customer)