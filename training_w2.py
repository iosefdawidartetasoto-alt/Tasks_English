import os

FILE_NAME = "database.txt"

# -------------------------------
# CREATE (Append - guardar blocker)
# -------------------------------
def add_blocker():
    blocker = input("Enter your daily blocker: ")

    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print(" Blocker saved successfully.\n")


# -------------------------------
# READ (Fetch - leer blockers)
# -------------------------------
def fetch_blockers():
    if not os.path.exists(FILE_NAME):
        print(" Error: File does not exist.\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

        if len(lines) == 0:
            print(" No blockers found.\n")
        else:
            print("\n Team Daily Blockers:")
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
            print()


# -------------------------------
# WARNING (Overwrite protection)
# -------------------------------
def overwrite_warning():
    if not os.path.exists(FILE_NAME):
        print(" File does not exist.\n")
        return

    confirm = input(" Warning: This will overwrite the file. Continue? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")
        print(" File overwritten successfully.\n")
    else:
        print(" Operation cancelled.\n")


# -------------------------------
# MENU
# -------------------------------
def menu():
    while True:
        print("=== Team Daily Status System ===")
        print("1. Add blocker")
        print("2. Fetch blockers")
        print("3. Overwrite file (danger)")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_blocker()
        elif option == "2":
            fetch_blockers()
        elif option == "3":
            overwrite_warning()
        elif option == "4":
            print(" Exiting program...")
            break
        else:
            print(" Invalid option.\n")


# Run program
menu()


# ----------------------------------------
# ENGLISH TASKS (Professional Communication)
# ----------------------------------------

# Protocol selection (3-C Rule)
# I will reach out to the team via Slack because the issue is an immediate blocker.
# Slack allows fast and clear communication with team members.
# This ensures the problem is resolved quickly and efficiently.

# Vocabulary integration
# This script demonstrates persistence by storing data in a text file.
# It allows the user to fetch saved blockers easily using file reading.
# The system prevents accidental overwrite by providing a warning message.
# If any issue occurs, I will reach out to the team to resolve it.