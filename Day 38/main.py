import random
import string
links = {}

def generate_code():
    characters = string.ascii_letters + string.digits
    while True:
        code = ""
        for _ in range(6):
            code += random.choice(characters)
        if code not in links:
            return code

def shorten_url():
    url = input("\nEnter URL: ")
    code = generate_code()
    links[code] = {
        "url": url,
        "clicks": 0
    }
    print(f"\nShort URL: ql/{code}")

def open_link():
    code = input("\nEnter short code: ")
    if code in links:
        links[code]["clicks"] += 1
        print("\nOpening...")
        print(links[code]["url"])
    else:
        print("Link not found.")

def search():
    keyword = input("\nSearch: ").lower()
    found = False
    for code, data in links.items():
        if keyword in data["url"].lower():
            print(f"ql/{code}  →  {data['url']}")
            found = True
    if not found:
        print("No matching links.")


def analytics():
    if len(links) == 0:
        print("\nNo links created.")
        return
    print("\nANALYTICS ")
    for code, data in links.items():
        print(f"ql/{code}")
        print(f"Clicks : {data['clicks']}")
        print()

while True:
    print("""

      QUICKLINK

1. Shorten URL
2. Open Link
3. Search URL
4. Analytics
5. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        shorten_url()
    elif choice == "2":
        open_link()
    elif choice == "3":
        search()
    elif choice == "4":
        analytics()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")