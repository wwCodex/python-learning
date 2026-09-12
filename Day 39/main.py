sessions = []

def add_session():
    song = input("\nSong: ").title()
    instrument = input("Instrument: ").title()
    minutes = int(input("Minutes practiced: "))
    bpm = int(input("BPM: "))
    session = {
        "song": song,
        "instrument": instrument,
        "minutes": minutes,
        "bpm": bpm
    }
    sessions.append(session)
    print("✓ Session recorded!\n")

def view_sessions():
    if len(sessions) == 0:
        print("\nNo practice history.\n")
        return

    print("\n STATISTICS")
    for i in range(len(sessions)):
        s = sessions[i]
        print(f"{i+1}. {s['song']}")
        print(f"   {s['instrument']} | {s['minutes']} min | {s['bpm']} BPM\n")

def search_song():
    name = input("\nSearch song: ").lower()
    found = False
    for s in sessions:
        if name in s["song"].lower():
            print(f"\n{s['song']}")
            print(f"Instrument : {s['instrument']}")
            print(f"Duration   : {s['minutes']} min")
            print(f"BPM        : {s['bpm']}")
            found = True
    if not found:
        print("Song not found.\n")

def statistics():
    if len(sessions) == 0:
        print("\nNo statistics available.\n")
        return

    total_time = 0
    total_bpm = 0
    drums = 0
    guitar = 0
    other = 0

    for s in sessions:
        total_time += s["minutes"]
        total_bpm += s["bpm"]
        if s["instrument"].lower() == "drums":
            drums += 1
        elif s["instrument"].lower() == "guitar":
            guitar += 1
        else:
            other += 1
    average_bpm = total_bpm / len(sessions)

    print("\n STATISTICS")
    print(f"Total Sessions : {len(sessions)}")
    print(f"Total Time     : {total_time} minutes")
    print(f"Average BPM    : {average_bpm:.1f}")
    if drums >= guitar and drums >= other:
        favourite = "Drums"
    elif guitar >= drums and guitar >= other:
        favourite = "Guitar"
    else:
        favourite = "Other"
    print(f"Most Practiced : {favourite}\n")


while True:
    print("""
      PRACTICE TRACKER

1. Add Practice Session
2. View History
3. Search Song
4. Statistics
5. Exit
""")

    choice = input("Choose: ")
    if choice == "1":
        add_session()
    elif choice == "2":
        view_sessions()
    elif choice == "3":
        search_song()
    elif choice == "4":
        statistics()
    elif choice == "5":
        print("\nKeep the groove alive")
        break
    else:
        print("Invalid option.\n")