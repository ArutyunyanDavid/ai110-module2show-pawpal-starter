"""PawPal+ system classes (Phase 1 skeleton).

This file defines the core classes for the PawPal+ pet care planner:
Owner, Pet, Task, and Scheduler.

For now these are STUBS only -- attributes plus method signatures with
short explanations. The real scheduling logic gets filled in during Phase 2.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single pet care task, such as a walk, feeding, or meds.

    Attributes:
        title: Short name of the task (e.g. "Morning walk").
        duration_minutes: How long the task takes, in minutes.
        priority: How important the task is: "low", "medium", or "high".
    """

    title: str
    duration_minutes: int
    priority: str = "medium"

    def priority_rank(self) -> int:
        """Turn the priority text into a number so tasks can be sorted.

        Higher number = more important. The Scheduler will use this to
        decide which tasks come first. (Logic added in Phase 2.)
        """
        ...


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
        ...

    def edit_task(self, index: int, task: Task) -> None:
        """Replace the task at the given position with an updated one."""
        ...


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
        ...

    def total_tasks(self) -> int:
        """Count every task across all of this owner's pets."""
        ...


class Scheduler:
    """Builds and explains a daily care plan from Owner / Pet / Task data.

    Responsibility: this is the "brain" of the app. It looks at the owner's
    available time and each task's priority and duration, then decides which
    tasks fit, in what order, and why.
    """

    def __init__(self, owner: Owner):
        # The owner (and through them, the pets and tasks) to plan for.
        self.owner = owner

    def generate_plan(self) -> list:
        """Build today's plan: pick and order tasks that fit the time budget.

        Returns an ordered list of Tasks. Higher-priority tasks come first,
        and tasks are dropped once the owner runs out of available minutes.
        (Logic added in Phase 2.)
        """
        ...

    def explain_plan(self, plan: list) -> str:
        """Return a short, human-readable explanation of the plan.

        Describes why each task was included and the order it was placed in.
        (Logic added in Phase 2.)
        """
        ...
