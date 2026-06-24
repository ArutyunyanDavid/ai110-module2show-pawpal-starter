"""Command-line demo for PawPal+.

Builds a small example (one owner, two pets, several tasks), generates
today's plan with the Scheduler, and prints the schedule plus an explanation.
Run it with:  python main.py
"""

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # 1. Create an owner with a limited time budget for the day.
    owner = Owner(name="Jordan", minutes_available=60)

    # 2. Create two pets.
    dog = Pet(name="Biscuit", species="dog")
    cat = Pet(name="Mochi", species="cat")

    # 3. Add tasks with different priorities and durations.
    dog.add_task(Task("Morning walk", duration_minutes=30, priority="high"))
    dog.add_task(Task("Grooming", duration_minutes=25, priority="low"))
    cat.add_task(Task("Feeding", duration_minutes=10, priority="high"))
    cat.add_task(Task("Play time", duration_minutes=15, priority="medium"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    # 4. Generate today's plan.
    scheduler = Scheduler(owner)
    plan = scheduler.generate_plan()

    # 5. Print a readable schedule.
    print("Today's Schedule")
    print("================")
    if plan:
        for position, task in enumerate(plan, start=1):
            print(
                f"{position}. {task.title} "
                f"({task.duration_minutes} min) [priority: {task.priority}]"
            )
    else:
        print("No tasks fit into the available time.")

    # 6. Print the scheduler's explanation.
    print("\nExplanation")
    print("===========")
    print(scheduler.explain_plan(plan))


if __name__ == "__main__":
    main()
