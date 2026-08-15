from assignment import Homework, Exam
from tracker import GradeTracker

print("Student Grade Tracker starting...")

tracker = GradeTracker()
tracker.add_assignment(Homework("Math", "Linear Algebra", 7, 10, "2026-06-15"))
tracker.add_assignment(Exam("Math", "Mid Term", 41, 100, "2026-06-15"))

for item in tracker.list_assignments():
    print(item.display())
