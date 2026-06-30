from pawpal_system import Owner, Task, Scheduler

owner = Owner(
    owner_name="James",
    pet_name="Buddy",
    species="Dog"
)

scheduler = Scheduler(owner)

scheduler.add_task(Task("Morning Walk", 30, "High"))
scheduler.add_task(Task("Feed Breakfast", 10, "High"))
scheduler.add_task(Task("Brush Coat", 20, "Medium"))
scheduler.add_task(Task("Play Fetch", 45, "Low"))

scheduler.sort_tasks()

print(owner.get_pet_info())
scheduler.display_schedule()

