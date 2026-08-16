class GradeTracker:

    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        """Adds one assignment object to the list."""
        self.assignments.append(assignment)

    def list_assignments(self):
        """Returns the list of assignments."""
        return self.assignments

    def filter_assignments(self, choice, value):
        """Filters assignments by type, subject or month.
        Choice can be 'type', 'subject' or 'month'.
        Returns a new list with only the assignments that match."""

        results = []
        value = value.lower().strip()

        for item in self.assignments:
            if choice == "type":
                if item.type == value:
                    results.append(item)
            elif choice == "subject":
                if item.subject == value:
                    results.append(item)
            elif choice == "month":
                if item.due_date[:7] == value:
                    results.append(item)

        return results

