## Programming 1 - Formative Project (Week 7)
## Student Grade / Assignment Tracker
## This file shows the menu, asks the questions and prints the results.

from assignment import Homework, Exam
from tracker import GradeTracker

def ask_text(question):
    """Keeps asking until the user types somwthing that is not empty."""
    while True:
        answer = input(question).strip()
        if answer == "":
            print("!! This cannot be empty. Please try again.")
        else:
            return answer

def ask_number(question):
    """Keeps asking until the user types a number that is not negative."""
    while True:
        answer = input(question).strip()
        try:
            number = float(answer)
        except ValueError:
            print("!! That is not a number. Type something like 15 or 15.5")
            continue

        if number < 0:
            print("!! This cannot be negative. Please try again.")
            continue
        return number

def is_valid_date(date_text):
    """Checks if the date is in the correct format (YYYY-MM-DD)"""
    parts = date_text.split("-")
    if len(parts) != 3:
        return False

    year = parts[0]
    month = parts[1]
    day = parts[2]

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False
    if int(month) < 1 or int(month) > 12:
        return False   
    if int(day) < 1 or int(day) > 31:
        return False
    return True

def ask_date(question):
    """Keeps asking until the date is in the correct format (YYYY-MM-DD)"""
    while True:
        answer = input(question).strip()
        if is_valid_date(answer):
            return answer
        print("!! This is not a valid date. Please write it like 2025-10-14")

def ask_scores():
    """Asks for the max score and the score, and 
    makes sure the score is not higher than the max score."""
    while True:
        max_score = ask_number("Max Score   :")
        if max_score <= 0:
            print("!! The max score must be bigger than 0.")
            continue
        break

    while True:
        score = ask_number("Score       :")
        if score > max_score:
            print("!! The score cannot be higher than the max score ({}).".format(max_score))
            continue
        break

    return score, max_score

def show_menu():
    """Prints the main menu."""
    print()
    print("========== GRADE TRACKER ==========")
    print("1) Add homework")
    print("2) Add exam")
    print("3) List assignments")
    print("4) Filter (by subject / type / month)")
    print("5) Show summary")
    print("0) Exit")
    print("===================================")

def add_assignment(tracker, kind):
    """Asks the questions and then adds a Homework or an Exam.
    'kind' is either 'homework' or 'exam'."""
    print()
    print("--- Add a new {} ---".format(kind))

    subject = ask_text("Subject     :")
    title = ask_text("Title       :")
    score, max_score = ask_scores()
    due_date = ask_date("Due date (YYYY-MM-DD)   :")

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
    print("---------------------------------------------")
    print("Total: {} assignment(s)".format(len(items)))

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
    choice = ask_text("Your choice: ").strip().lower()

    if choice == "a":
        atype = ask_text("Enter the type (homework or exam): ").strip().lower()
        if atype != "homework" and atype != "exam":
            print("\nInvalid type. Must be 'homework' or 'exam'.")
            return
        results = tracker.filter_assignments("type", atype)

    elif choice == "b":
        subject = ask_text("Enter the subject: ")
        results = tracker.filter_assignments("subject", subject)

    elif choice == "c":
        month = ask_text("Enter the month (YYYY-MM): ")
        results = tracker.filter_assignments("month", month)

    else:
        print("!! That is not a filter option.")
        return

    if len(results) == 0:
        print("\nNo assignments matched your filter.")
    else:
        print_assignments(results)

def print_summary(tracker):
    """Prints the overall average, the subject averages and the best/worst."""
    summary = tracker.summarize()

    print()
    if summary is None:
        print("There are no assignments yet, so there is no summary.")
        return

    print()
    print("========== SUMMARY ==========")
    print("Assignments recorded: {}".format(summary["count"]))
    print("Overall average     : {:.1f}%".format(summary["overall"]))
    print()
    print("Average per subject:")
    for subject in summary["subjects"]:
        print("- {} : {:.1f}%".format(subject, summary["subjects"][subject]))
    print()
    print("Highest score : {} ({:.1f}%)".format(summary["best"].title, summary["best"].percentage()))
    print("Lowest score  : {} ({:.1f}%)".format(summary["worst"].title, summary["worst"].percentage()))

    if summary["overall"] < 50:
        print()
        print("WARNING: your overall average is under 50%.")
    print("=================================")

def main():
    """The main program loop."""
    tracker = GradeTracker()
    print("Welcome to the Grade Tracker!")

    running = True
    while running:
        show_menu()
        choice = ask_text("Choose an option: ").strip()

        if choice == "1":
            add_assignment(tracker, "homework")
        elif choice == "2":
            add_assignment(tracker, "exam")
        elif choice == "3":
            print_assignments(tracker.list_assignments())
        elif choice == "4":
            do_filter(tracker)
        elif choice == "5":
            print_summary(tracker)
        elif choice == "0":
            print("\nGoodbye! Nothing was saved because this is a session only progam")
            running = False
        else:
            print("\n!! '{}' is not on the menu. Please choose 0 to 5.".format(choice))

if __name__ == "__main__":
    main()
