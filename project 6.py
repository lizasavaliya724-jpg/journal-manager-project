from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("Enter your journal entry: ")

        try:
            with open(self.filename, "a") as file:
                timestamp = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as e:
            print("Error while saving entry:", e)

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if content.strip():
                print("\nYour Journal Entries:")
                print("------------------------------")
                print(content)
            else:
                print("No journal entries found.")

        except FileNotFoundError:
            print(
                "No journal entries found. "
                "Start by adding a new entry!"
            )

        except PermissionError:
            print("Error: Permission denied.")

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:
                content = file.read()

            entries = content.strip().split("\n\n")

            matches = [
                entry for entry in entries
                if keyword.lower() in entry.lower()
            ]

            if matches:
                print("\nMatching Entries:")
                print("------------------------------")

                for entry in matches:
                    print(entry)
                    print()
            else:
                print(
                    "No entries were found for the keyword:",
                    keyword
                )

        except FileNotFoundError:
            print(
                "Error: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("Error: Permission denied.")

    def delete_entries(self):
        confirm = input(
            "Are you sure you want to delete all entries? (yes/no): "
        )

        if confirm.lower() == "yes":
            try:
                with open(self.filename, "r"):
                    pass

                with open(self.filename, "w") as file:
                    file.truncate(0)

                print("All journal entries have been deleted.")

            except FileNotFoundError:
                print("No journal entries to delete.")

            except PermissionError:
                print("Error: Permission denied.")

        else:
            print("Deletion cancelled.")


def main():
    journal = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                journal.add_entry()

            elif choice == 2:
                journal.view_entries()

            elif choice == 3:
                journal.search_entry()

            elif choice == 4:
                journal.delete_entries()

            elif choice == 5:
                print(
                    "Thank you for using Personal Journal Manager."
                )
                print("Goodbye!")
                break

            else:
                print(
                    "Invalid option. Please select a valid option "
                    "from the menu."
                )

        except ValueError:
            print(
                "Invalid input. Please enter a number from 1 to 5."
            )


if __name__ == "__main__":
    main()