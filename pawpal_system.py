from dataclasses import dataclass

@dataclass
class Owner:
    owner_name: str
    pet_name: str
    species: str

    def get_pet_info(self):
        return f"{self.pet_name} ({self.species}) belongs to {self.owner_name}"


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str

    def to_dict(self):
        return {
            "Title": self.title,
            "Duration": self.duration_minutes,
            "Priority": self.priority,
        }


class Scheduler:

    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def sort_tasks(self):
        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        self.tasks.sort(
            key=lambda task: (
                priority_order.get(task.priority, 99),
                task.duration_minutes
            )
        )

    def display_schedule(self):
        print("\nDaily Schedule")
        print("-" * 40)

        for task in self.tasks:
            print(
                f"{task.title} | "
                f"{task.duration_minutes} min | "
                f"{task.priority}"
            )

            