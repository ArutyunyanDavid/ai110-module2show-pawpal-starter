"""Basic tests for the PawPal+ core system."""

from pawpal_system import Owner, Pet, Task, Scheduler


def test_priority_rank_high_beats_low():
    """A high-priority task should rank higher than a low-priority one."""
    high = Task("Walk", duration_minutes=30, priority="high")
    low = Task("Grooming", duration_minutes=30, priority="low")
    assert high.priority_rank() > low.priority_rank()


def test_adding_task_increases_count():
    """Adding a task to a pet should grow its task list by one."""
    pet = Pet(name="Biscuit", species="dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task("Feeding", duration_minutes=10, priority="high"))
    assert len(pet.tasks) == 1


def test_plan_does_not_exceed_available_minutes():
    """The generated plan must fit within the owner's available minutes."""
    owner = Owner(name="Jordan", minutes_available=40)
    pet = Pet(name="Mochi", species="cat")
    pet.add_task(Task("Walk", duration_minutes=30, priority="high"))
    pet.add_task(Task("Grooming", duration_minutes=25, priority="medium"))
    pet.add_task(Task("Feeding", duration_minutes=10, priority="high"))
    owner.add_pet(pet)

    plan = Scheduler(owner).generate_plan()
    total_minutes = sum(task.duration_minutes for task in plan)
    assert total_minutes <= owner.minutes_available
