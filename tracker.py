#file for GradeTracker class. Keeps all the assignments in a list

class GradeTracker:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        """Adds one assignment object to the list."""
        self.assignments.append(assignment)

    def list_assignments(self):
        """Returns the list of assignments."""
        return self.assignments