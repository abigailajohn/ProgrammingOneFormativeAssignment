## Programming 1 - Formative Project (Week 7)
## Student Grade / Assignment Tracker
## This file shows the menu, asks the questions and prints the results.

from assignment import Homework, Exam
from tracker import GradeTracker

def show_menu():
    """Prints the main menu."""
    print()
    print("========== GRADE TRACKER ==========")
    print("1) Add homework")
    print("2) Add exam")
    print("3) List assignments")
    print("4) Filter (by subject / type / month)")
    print("0) Exit")
    print("===================================")

def add_assignment(tracker, kind):
    """Asks the questions and then adds a Homework or an Exam.
    'kind' is either 'homework' or 'exam'."""
    print()
    print("--- Add a new {} ---".format(kind))

    subject = input("Subject     :")
    title = input("Title        :")
    max_score = float(input("Max Score   :"))
    score = float(input("Score       :"))
    due_date = input("Due Date (YYYY-MM-DD) :")

    if kind == "homework":
        new_item = Homework(subject, title, score, max_score, due_date)
    else:
        new_item = Exam(subject, title, score, max_score, due_date)

    tracker.add_assignment(new_item)
    print("Saved! {} was added.".format(title))

def print_assignments(items):
    """Prints the list of assignments."""
    print()
    if len(items) == 0:
        print("No assignments yet.")
        return

    print("---------------------------------------------")
    number = 1
    for item in items:
        print("{}. {}".format(number, item.display()))
        number = number + 1
    print("Total: {} assignment(s)".format(len(items)))

def main():
    """The main program loop."""
    tracker = GradeTracker()
    print("Welcome to the Grade Tracker!")

    running = True
    while running:
        show_menu()
        choice = input("Choose and option: ").strip()

        if choice == "1":
            add_assignment(tracker, "homework")
        elif choice == "2":
            add_assignment(tracker, "exam")
        elif choice == "3":
            print_assignments(tracker.list_assignments())
        elif choice == "4":
            do_filter(tracker)
        elif choice == "0":
            print("\nGoodbye! Nothing was saved because this is a session only progam")
            running = False
        else:
            print("\n!! '{}' is not on the menu. Please choose 0 to 4.".format(choice))

def do_filter(tracker):
    """Small menu for the filter option."""
    if len(tracker.list_assignments()) == 0:
        print("\nThere are no assignments to filter yet.")
        return

    print()
    print("--- Filter Assignments ---")
    print("a) By type (homework or exam)")
    print("b) By subject")
    print("c) By month (example: 2026-07)")
    choice = input("Your choice: ").strip().lower()

    if choice == "a":
        atype = input("Enter the type (homework or exam): ").strip().lower()
        if atype != "homework" and atype != "exam":
            print("\nInvalid type. Must be 'homework' or 'exam'.")
            return
        results = tracker.filter_assignments("type", atype)

    elif choice == "b":
        subject = input("Enter the subject: ")
        results = tracker.filter_assignments("subject", subject)

    elif choice == "c":
        month = input("Enter the month (YYYY-MM): ")
        results = tracker.filter_assignments("month", month)

    else:
        print("!! That is not a filter option.")
        return

    if len(results) == 0:
        print("\nNo assignments matched your filter.")
    else:
        print_assignments(results)


if __name__ == "__main__":
    main()
