# Student Grade / Assignment Tracker

Programming 1 — Formative Project (Week 7).
Written in Python 3, runs in the command line.

## Project overview

This program lets a student record their homework and exam results during one
terminal session. You can add an assignment, list everything you have added,
filter the list, and see a summary of your grades. Nothing is saved to a file,
so when the program closes the data is gone.

### Features

- Add homework or an exam (subject, title, score, max score, due date)
- List all assignments with the percentage and a PASS / FAIL note
- Filter by type (homework / exam), by subject, or by month (e.g. 2026-0)
- Summary showing the overall average, the average of each subject, and the
  highest and lowest scoring assignment
- Input validation: scores must be numbers, a score cannot be bigger than the
  max score, the due date must look like YYYY-MM-DD, and invalid menu choices
  are refused instead of crashing the program
- Extra features: undo the last entry and a warning if the overall average
  drops below 50%

Homework and exams use different pass marks. A homework passes at 30% but an
exam needs 50%, so the same percentage can show PASS on one and FAIL on the
other.

## Files in this repository

| File | What it does |
|------|--------------|
| `main.py` | The menu, the questions asked to the user, and the printing |
| `assignment.py` | The Assignment class and the Homework / Exam subclasses |
| `tracker.py` | The GradeTracker class (add, list, filter, summarize, undo) |
| `test_tracker.py` | A few assert tests that check the classes work |
| `screenshots/` | Screenshots of the program running |
| `repo-link.txt` | The link to this repository |

## How to run it

You need Python 3 installed.

```bash
git clone https://github.com/abigailajohn/ProgrammingOneFormativeAssignment.git
cd ProgrammingOneFormativeAssignment
python main.py
```

To run the tests:

```bash
python test_tracker.py
```

## Menu structure

```
Welcome to the Grade Tracker!

========== GRADE TRACKER ==========
1) Add homework
2) Add exam
3) List assignments
4) Filter (by subject / type / month)
5) Show summary
6) Undo last entry
0) Exit
===================================
Choose an option:
```

Option 4 opens a small second menu:

```
Choose an option: 4

--- Filter Assignments ---
a) By type (homework or exam)
b) By subject
c) By month (example: 2026-07)
Your choice:
```

## Sample interactions

### Adding a homework

```
Choose an option: 1

--- Add a new homework ---
Subject     :Maths
Title       :Algebra sheet
Max Score   :10
Score       :8
Due date (YYYY-MM-DD)   :2026-07-14
Saved! Algebra sheet was added.
```

### Input validation

The program does not crash when the user types something wrong. It explains the
problem and asks again.

```
--- Add a new homework ---
Subject     :Chemistry
Title       :Titration lab
Max Score   :0
!! The max score must be bigger than 0.
Max Score   :30
Score       :abc
!! That is not a number. Type something like 15 or 15.5
Score       :-5
!! This cannot be negative. Please try again.
Score       :40
!! The score cannot be higher than the max score (30.0).
Score       :24
Due date (YYYY-MM-DD)   :14-10-2026
!! This is not a valid date. Please write it like 2025-10-14
Due date (YYYY-MM-DD)   :2026/08/14
!! This is not a valid date. Please write it like 2025-10-14
Due date (YYYY-MM-DD)   :2026-13-14
!! This is not a valid date. Please write it like 2025-10-14
Due date (YYYY-MM-DD)   :2026-08-16
Saved! Titration lab was added.
```

A wrong menu choice is also handled:

```
Choose an option: exit

!! 'exit' is not on the menu. Please choose 0 to 6.
```

### Listing the assignments

```
Choose an option: 3

---------------------------------------------
1. [HW] Algebra sheet (maths) - 8.0/10.0 = 80.0% - due 2026-07-14 - PASS
2. [EXAM] Mid term exam (maths) - 72.0/100.0 = 72.0% - due 2026-07-20 - PASS
3. [HW] Book report (english) - 11.0/20.0 = 55.0% - due 2026-08-11 - PASS
4. [EXAM] Poetry exam (english) - 18.0/50.0 = 36.0% - due 2026-08-20 - FAIL
5. [HW] Cell diagram (biology) - 7.0/25.0 = 28.0% - due 2026-08-01 - FAIL
---------------------------------------------
Total: 5 assignment(s)
```

Assignment 4 and 5 show why the two subclasses are useful. The exam failed at
36% because an exam needs 50%, but a homework at 36% would have passed.

### Filtering by month

```
Choose an option: 4

--- Filter Assignments ---
a) By type (homework or exam)
b) By subject
c) By month (example: 2026-07)
Your choice: c
Enter the month (YYYY-MM): 2026-08

---------------------------------------------
1. [HW] Book report (english) - 11.0/20.0 = 55.0% - due 2026-08-11 - PASS
2. [EXAM] Poetry exam (english) - 18.0/50.0 = 36.0% - due 2026-08-20 - FAIL
3. [HW] Cell diagram (biology) - 7.0/25.0 = 28.0% - due 2026-08-01 - FAIL
---------------------------------------------
Total: 3 assignment(s)
```

Filtering by subject is not case sensitive, so typing `MATHS` finds the same
assignments as `maths`. If nothing matches the program says so:

```
Enter the subject: history

No assignments matched your filter.
```

### The summary

```
Choose an option: 5

========== SUMMARY ==========
Assignments recorded: 5
Overall average     : 56.6%

Average per subject:
- maths : 72.7%
- english : 41.4%
- biology : 28.0%

Highest score : Algebra sheet (80.0%)
Lowest score  : Cell diagram (28.0%)
=================================
```

## A note on how the average is calculated

The overall average is **total score divided by total max score**, not the
average of the percentages. This means an exam out of 100 counts more than a
homework out of 10, which is fairer. For example 8/10 and 72/100 gives
80/110 = 72.7%, not (80% + 72%) / 2 = 76%.