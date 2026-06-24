# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Running `python main.py` builds an example owner with two pets and four tasks,
then prints today's plan and the scheduler's explanation:

```
Today's Schedule
================
1. Morning walk (30 min) [priority: high]
2. Feeding (10 min) [priority: high]
3. Play time (15 min) [priority: medium]

Explanation
===========
Jordan has 60 minutes available.
Chose 3 task(s) using 55 minute(s), highest priority first:
  1. Morning walk (30 min, high priority)
  2. Feeding (10 min, high priority)
  3. Play time (15 min, medium priority)
```

Note how the low-priority "Grooming" (25 min) task was skipped: the two
high-priority tasks plus the medium one already used 55 of the 60 minutes,
so grooming would not fit.

## 🧪 Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

The tests in `tests/test_pawpal.py` cover the most important behaviors:

- **Priority ranking** — a high-priority task ranks higher than a low-priority one.
- **Adding tasks** — adding a task to a pet increases that pet's task count.
- **Task completion** — calling `mark_complete()` flips a task's `completed` flag to True.
- **Time budget** — the generated plan never exceeds the owner's available minutes.

Passing output:

```
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\aruty\Desktop\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 4 items

tests\test_pawpal.py ....                                                [100%]

============================== 4 passed in 0.04s ==============================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Start the app with:

```bash
streamlit run app.py
```

Then follow these steps in the browser:

1. **Enter owner info** — type your name and how many minutes you have today, then click **Save owner**.
2. **Add a pet** — enter a pet name and species and click **Add pet**. Repeat for more pets.
3. **Add tasks** — pick which pet a task is for, set its title, duration, and priority, then click **Add task**.
4. **Generate the schedule** — click **Generate schedule** to see today's plan.
5. **Read the plan** — the plan is sorted by priority (high → medium → low) and limited by your available time, so lower-priority tasks are skipped once time runs out. An explanation shows why each task was chosen.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
