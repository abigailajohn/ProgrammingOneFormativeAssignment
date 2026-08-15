class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, atype):
        self.subject = subject.lower().strip()
        self.title = title.strip()
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date
        self.type = atype #'homework' or 'exam'

    def percentage(self):
        return (self.score / self.max_score) * 100