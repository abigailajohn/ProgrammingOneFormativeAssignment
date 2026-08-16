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

    def summarize(self):
        """Works out the overall average, the average of every subject and 
        the best and worst assigment. Returns everything in a dictionary.
        """

        if len(self.assignments) == 0:
            return None

        total_score = 0
        total_max = 0
        subjects = {}

        best = self.assignments[0]
        worst = self.assignments[0]

        for item in self.assignments:
            total_score = total_score + item.score
            total_max = total_max + item.max_score

            if item.subject not in subjects:
                subjects[item.subject] = [0, 0]
            subjects[item.subject][0] = subjects[item.subject][0] + item.score
            subjects[item.subject][1] = subjects[item.subject][1] + item.max_score

            if item.percentage() > best.percentage():
                best = item
            if item.percentage() < worst.percentage():
                worst = item
        overall = (total_score / total_max) * 100

        subject_averages = {}
        for name in subjects:
            marks = subjects[name]
            subject_averages[name] = (marks[0] / marks[1]) * 100

        summary = {
            "count": len(self.assignments),
            "overall": overall,
            "subjects": subject_averages,
            "best": best,
            "worst": worst,
        }
        return summary


            
