from assignment import Assignment

print("Student Grade Tracker starting...")

test = Assignment("Math", "Linear Algebra", 7, 10, "2024-06-15", "homework")
print(test.subject, test.title, test.percentage())
