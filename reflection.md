# PawPal+ Project Reflection

# System Design

PawPal+ supports three core user actions for a busy pet owner:

1. **Add owner and pet info.** The user enters their own name plus basic details
   about their pet (name, species, and any care preferences). This gives the app
   the context it needs before any planning can happen.
2. **Add/edit pet care tasks.** The user adds tasks such as walks, feeding, meds,
   or grooming. Every task has at least a title, a duration (in minutes), and a
   priority (low / medium / high) so the scheduler knows how important it is and
   how much time it needs.
3. **Generate and view today's daily plan.** The user asks PawPal+ to build a plan
   for the day. The scheduler looks at the available time and each task's priority,
   chooses which tasks fit, orders them, and explains why it made those choices.

## 1a. Initial design

My initial UML uses four classes, each with a clear responsibility:

- **Owner** — represents the person using the app. Stores the owner's name,
  available time, and preferences, and owns one or more pets.
- **Pet** — represents a single pet. Stores the pet's name and species and holds
  the list of care tasks that belong to that pet.
- **Task** — represents one unit of pet care. Stores a title, duration (minutes),
  and priority; it is the data the scheduler sorts and selects.
- **Scheduler** — the "brain" of the app. It reads Owner / Pet / Task data and
  produces an ordered daily plan plus a short explanation of its choices.

The relationships are: an Owner *has many* Pets, a Pet *has many* Tasks, and the
Scheduler *uses* Owner / Pet / Task data to generate the plan.

## 1b. Design changes

After reviewing the class skeleton, no major structural changes were needed — the
four-class design (Owner / Pet / Task / Scheduler) stayed simple on purpose, which
keeps it beginner-friendly and easy to implement in Phase 2. The one refinement
made during cleanup was copying the UML draft from `diagrams/uml_draft.mmd` to
`diagrams/uml.mmd` so the filename matches the project/grading expectations. Any
further design changes will be documented here after the scheduling logic is built.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers three things: the owner's available minutes for the day,
each task's priority (high > medium > low), and each task's scheduled time. Time
budget and priority mattered most, so `generate_plan()` sorts by priority first
(then by time as a tie-breaker) and adds tasks only while they still fit within
`owner.minutes_available`. Completed tasks are skipped entirely.

**b. Tradeoffs**

The main Phase 4 tradeoff is in conflict detection. `detect_conflicts()` uses
**simple exact-time matching** rather than advanced overlapping-duration
detection. It only flags tasks that share the exact same `"HH:MM"` start time.

This keeps the project beginner-friendly and easy to explain, but it means a
9:00–9:30 task and a 9:15–9:45 task will **not** be flagged as a conflict unless
they happen to start at the same minute. For this simple planning app that
tradeoff is reasonable: the goal is a clear, understandable warning system, not a
full calendar engine. Adding true overlap detection (comparing start + duration)
would be the natural next improvement.

Recurring tasks make a similar simplicity tradeoff: instead of tracking real
calendar dates, `handle_recurring_task()` returns a copied, incomplete task with a
`"(next daily)"` / `"(next weekly)"` note. This is easy to reason about but does
not compute an actual next date.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
