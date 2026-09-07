invoice = []
def add_item():
    name = input("Item name: ").title()
    qty = int(input("Quantity: "))
    price = float(input("Price: ₹"))

    invoice.append({
        "name": name,
        "qty": qty,
        "price": price,
        "total": qty * price
    })

def subtotal():
    total = 0
    for item in invoice:
        total += item["total"]
    return total

def print_invoice(customer):
    print("          INVOICE")
    print(f"Customer : {customer}\n")
    print(f"{'Item':15}{'Qty':>6}{'Total':>10}")
    for item in invoice:
        print(f"{item['name']:15}{item['qty']:>6}{item['total']:>10.2f}")
    sub = subtotal()
    gst = sub * 0.18
    grand = sub + gst
    print(f"{'Subtotal':21}₹{sub:.2f}")
    print(f"{'GST (18%)':21}₹{gst:.2f}")
    print(f"{'Grand Total':21}₹{grand:.2f}")
customer = input("Customer name: ")

while True:
    add_item()
    more = input("\nAdd another item? (y/n): ").lower()
    if more != "y":
        break
print_invoice(customer)