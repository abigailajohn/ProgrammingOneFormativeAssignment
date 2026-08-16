# Simple tests with assert to check my classes work.
# Run it with:  python test_tracker.py

from assignment import Homework, Exam
from tracker import GradeTracker

def test_percentage():
    hw = Homework("Math", "Algebra sheet", 8, 10, "2026-08-04")
    assert hw.percentage() == 80.0
    print("test_percentage() passed")

def test_inheritance():
    hw = Homework("Math", "Algebra sheet", 8, 10, "2026-08-04")
    ex = Exam("Math", "Mid terms", 30, 100, "2026-08-10")
    assert hw.type == "homework"
    assert ex.type == "exam"
    assert ex.is_passing() == False
    print("test_inheritance() passed")


def test_filter_and_summary():
    tracker = GradeTracker()
    tracker.add_assignment(Homework("Math", "Algebra sheet", 8, 10, "2026-08-04"))
    tracker.add_assignment(Exam("english", "Essay exam", 40, 50, "2026-09-15"))

    assert len(tracker.filter_assignments("type", "exam")) == 1
    assert len((tracker.filter_assignments("month", "2026-09"))) == 1
    assert len(tracker.filter_assignments("subject", "Math")) == 1

    summary = tracker.summarize()
    assert summary["count"] == 2
    assert round(summary["overall"], 1) == 80.0
    print("test_filter_and_summary() passed")

def test_undo():
    tracker = GradeTracker()
    tracker.add_assignment(Homework("maths", "Sheet 1", 5, 10, "2026-08-01"))
    tracker.undo_last()
    assert len(tracker.list_assignments()) == 0
    assert tracker.undo_last() is None
    print("test_undo passed")

test_percentage()
test_inheritance()
test_filter_and_summary()
test_undo()
print("All tests passed!")