vault = []

def add_credential():
    website = input("\nWebsite: ").lower()
    username = input("Username: ")
    password = input("Password: ")

    vault.append({
        "website": website,
        "username": username,
        "password": password
    })

    print("Credential saved!")


def view_vault():

    if len(vault) == 0:
        print("\nVault is empty.")
        return

    print("\n========== PASSWORD VAULT ==========")

    for i in range(len(vault)):
        account = vault[i]

        hidden = "*" * len(account["password"])

        print(f"\n{i+1}. {account['website'].title()}")
        print(f"   Username : {account['username']}")
        print(f"   Password : {hidden}")


def search():

    site = input("\nSearch website: ").lower()

    found = False

    for account in vault:

        if account["website"] == site:

            print("\nFOUND")
            print(f"Website  : {account['website'].title()}")
            print(f"Username : {account['username']}")
            print(f"Password : {account['password']}")

            found = True

    if not found:
        print("No credential found.")


def delete():

    view_vault()

    if len(vault) == 0:
        return

    choice = int(input("\nDelete which entry?: ")) - 1

    if 0 <= choice < len(vault):

        removed = vault.pop(choice)

        print(f"{removed['website'].title()} removed.")

    else:
        print("Invalid choice.")


while True:

    print("""
==============================
      PASSWORD VAULT
==============================

1. Add Credential
2. View Vault
3. Search Website
4. Delete Credential
5. Exit
""")

    option = input("Choose: ")

    if option == "1":
        add_credential()

    elif option == "2":
        view_vault()

    elif option == "3":
        search()

    elif option == "4":
        delete()

    elif option == "5":
        print("\nVault Locked")
        break

    else:
        print("Invalid option.")