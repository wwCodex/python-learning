playlist = []


def add_song():

    title = input("\nSong title: ").title()
    artist = input("Artist: ").title()

    song = {
        "title": title,
        "artist": artist
    }

    playlist.append(song)

    print("\nSong added successfully!")


def view_playlist():

    if len(playlist) == 0:
        print("\nYour playlist is empty.")
        return

    print("\n========== YOUR PLAYLIST ==========")

    for i in range(len(playlist)):
        print(f"{i + 1}. {playlist[i]['title']} - {playlist[i]['artist']}")


def search_song():

    search = input("\nEnter song title: ").lower()

    found = False

    for song in playlist:

        if song["title"].lower() == search:
            print(f"\nFound: {song['title']} - {song['artist']}")
            found = True

    if found == False:
        print("Song not found.")


def remove_song():

    view_playlist()

    if len(playlist) == 0:
        return

    choice = int(input("\nEnter song number to remove: "))

    if 1 <= choice <= len(playlist):

        removed = playlist.pop(choice - 1)

        print(f"{removed['title']} removed.")

    else:
        print("Invalid song number.")


def menu():

    while True:

        print("""
============================
    PLAYLIST MANAGER
============================

1. Add Song
2. View Playlist
3. Search Song
4. Remove Song
5. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            add_song()

        elif choice == "2":
            view_playlist()

        elif choice == "3":
            search_song()

        elif choice == "4":
            remove_song()

        elif choice == "5":
            print("\nThanks for using Playlist Manager!")
            break

        else:
            print("Invalid choice.")


menu()