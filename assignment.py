class Assignment:
    """One assignment (homework or exam)"""

    pass_mark = 50

    def __init__(self, subject, title, score, max_score, due_date, atype):
        self.subject = subject.lower().strip()
        self.title = title.strip()
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date
        self.type = atype #'homework' or 'exam'

    def percentage(self):
        return (self.score / self.max_score) * 100

    def is_passing(self):
        return self.percentage() >= self.pass_mark

    def label(self):
        return "ASSIGNMENT"


class Homework(Assignment):
    """A homework. Uses super() so it reuses the Assignment constructor."""
    
    pass_mark = 30

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "homework")

    def label(self):
        return "HW"

class Exam(Assignment):
    """An Exam. Same idea as Homework but with a higher pass mark"""

    pass_mark = 50

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "exam")

    def label(self):
        return "EXAM"