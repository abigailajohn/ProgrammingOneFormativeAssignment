from assignment import Homework, Exam

print("Student Grade Tracker starting...")

hw = Homework("Math", "Linear Algebra", 7, 10, "2026-06-15")
ex = Exam("Math", "Mid Term", 41, 100, "2026-06-15")

print(hw.label(), hw.type, hw.percentage(), hw.is_passing())
print(ex.label(), ex.type, ex.percentage(), ex.is_passing())
