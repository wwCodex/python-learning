import random

parcels = []
statuses = [
    "Order Placed",
    "Dispatched",
    "In Transit",
    "Out for Delivery",
    "Delivered"
]

def generate_id():
    while True:
        tracking = "PK" + str(random.randint(10000, 99999))
        exists = False
        for parcel in parcels:
            if parcel["id"] == tracking:
                exists = True
        if not exists:
            return tracking

def create_parcel():
    sender = input("Sender: ").title()
    receiver = input("Receiver: ").title()
    city = input("Destination City: ").title()
    parcel = {
        "id": generate_id(),
        "sender": sender,
        "receiver": receiver,
        "city": city,
        "status": statuses[0]
    }
    parcels.append(parcel)
    print(f"\nParcel Created!")
    print(f"Tracking ID: {parcel['id']}")

def view_parcels():
    if len(parcels) == 0:
        print("\nNo parcels found.")
        return

    print("\nPARCELS")
    for parcel in parcels:
        print(f"\n{parcel['id']}")
        print(f"To     : {parcel['receiver']}")
        print(f"City   : {parcel['city']}")
        print(f"Status : {parcel['status']}")

def search_parcel():
    tracking = input("\nEnter Tracking ID: ").upper()

    for parcel in parcels:
        if parcel["id"] == tracking:
            print("\nPARCEL FOUND")
            print(f"Sender    : {parcel['sender']}")
            print(f"Receiver  : {parcel['receiver']}")
            print(f"City      : {parcel['city']}")
            print(f"Status    : {parcel['status']}")
            return
    print("Parcel not found.")

def update_status():
    tracking = input("\nTracking ID: ").upper()
    for parcel in parcels:
        if parcel["id"] == tracking:
            current = statuses.index(parcel["status"])
            if current == len(statuses) - 1:
                print("Parcel already delivered.")
                return
            parcel["status"] = statuses[current + 1]
            print(f"Updated to: {parcel['status']}")
            return
    print("Parcel not found.")

def statistics():
    delivered = 0
    transit = 0

    for parcel in parcels:
        if parcel["status"] == "Delivered":
            delivered += 1
        else:
            transit += 1

    print("\n STATISTICS ")
    print(f"Total Parcels : {len(parcels)}")
    print(f"Delivered     : {delivered}")
    print(f"In Progress   : {transit}")


while True:

    print("""

      PARCEL TRACK

1. Create Parcel
2. View Parcels
3. Search Parcel
4. Update Status
5. Statistics
6. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        create_parcel()
    elif choice == "2":
        view_parcels()
    elif choice == "3":
        search_parcel()
    elif choice == "4":
        update_status()
    elif choice == "5":
        statistics()
    elif choice == "6":
        print("\nSystem Closed")
        break
    else:
        print("Invalid option.")