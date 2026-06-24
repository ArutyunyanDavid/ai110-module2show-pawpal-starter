"""PawPal+ system classes.

This file defines the core classes for the PawPal+ pet care planner:
Owner, Pet, Task, and Scheduler.

The Scheduler turns each owner's pets and tasks into a daily plan that fits
the owner's available time, putting the most important tasks first.
"""

from dataclasses import dataclass, field

# Maps a priority word to a number. Higher number = more important.
# Used so we can sort tasks (high > medium > low).
PRIORITY_SCORES = {"low": 1, "medium": 2, "high": 3}


@dataclass
class Task:
    """A single pet care task, such as a walk, feeding, or meds.

    Attributes:
        title: Short name of the task (e.g. "Morning walk").
        duration_minutes: How long the task takes, in minutes.
        priority: How important the task is: "low", "medium", or "high".
        completed: Whether the task has been done yet (starts False).
    """

    title: str
    duration_minutes: int
    priority: str = "medium"
    completed: bool = False

    def priority_rank(self) -> int:
        """Turn the priority text into a number so tasks can be sorted.

        Higher number = more important (high=3, medium=2, low=1). Any
        unknown priority is treated as the lowest (0).
        """
        return PRIORITY_SCORES.get(self.priority, 0)

    def mark_complete(self) -> None:
        """Mark this task as done by setting completed to True."""
        self.completed = True


@dataclass
class Pet:
    """A pet owned by the user, along with its list of care tasks.

    Attributes:
        name: The pet's name (e.g. "Mochi").
        species: The kind of animal (e.g. "dog", "cat", "other").
        tasks: All care tasks that belong to this pet.
    """

    name: str
    species: str = "other"
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a new care task to this pet's task list."""
        self.tasks.append(task)

    def edit_task(self, index: int, task: Task) -> None:
        """Replace the task at the given position with an updated one."""
        self.tasks[index] = task


class Owner:
    """The person using PawPal+, who can own one or more pets.

    Responsibility: holds the owner's info and preferences, and keeps
    track of all the pets they care for.
    """

    def __init__(self, name: str, minutes_available: int = 60):
        # Owner's name.
        self.name = name
        # How many minutes the owner has for pet care today (a constraint).
        self.minutes_available = minutes_available
        # Free-text care preferences, e.g. "walks in the morning".
        self.preferences: list = []
        # Every pet this owner is responsible for.
        self.pets: list = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def total_tasks(self) -> int:
        """Count every task across all of this owner's pets."""
        return sum(len(pet.tasks) for pet in self.pets)


class Scheduler:
    """Builds and explains a daily care plan from Owner / Pet / Task data.

    Responsibility: this is the "brain" of the app. It looks at the owner's
    available time and each task's priority and duration, then decides which
    tasks fit, in what order, and why.
    """

    def __init__(self, owner: Owner):
        # The owner (and through them, the pets and tasks) to plan for.
        self.owner = owner

    def _all_tasks(self) -> list:
        """Collect every task from all of the owner's pets into one list."""
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return tasks

    def generate_plan(self) -> list:
        """Build today's plan: pick and order tasks that fit the time budget.

        Steps:
        1. Gather every task across all pets.
        2. Sort them so higher-priority tasks come first.
        3. Add tasks one by one, skipping any that would push the total
           past the owner's available minutes.

        Returns an ordered list of the Tasks that made it into the plan.
        """
        # Sort by priority, highest first. reverse=True puts the biggest rank on top.
        sorted_tasks = sorted(
            self._all_tasks(), key=lambda task: task.priority_rank(), reverse=True
        )

        plan = []
        minutes_used = 0
        for task in sorted_tasks:
            # Only add the task if it still fits in the remaining time.
            if minutes_used + task.duration_minutes <= self.owner.minutes_available:
                plan.append(task)
                minutes_used += task.duration_minutes
        return plan

    def explain_plan(self, plan: list) -> str:
        """Return a short, human-readable explanation of the plan.

        Describes how much time the plan uses and why each task was chosen.
        """
        if not plan:
            return (
                f"No tasks fit into {self.owner.minutes_available} available minutes."
            )

        minutes_used = sum(task.duration_minutes for task in plan)
        lines = [
            f"{self.owner.name} has {self.owner.minutes_available} minutes available.",
            f"Chose {len(plan)} task(s) using {minutes_used} minute(s), "
            "highest priority first:",
        ]
        for position, task in enumerate(plan, start=1):
            lines.append(
                f"  {position}. {task.title} "
                f"({task.duration_minutes} min, {task.priority} priority)"
            )
        return "\n".join(lines)
