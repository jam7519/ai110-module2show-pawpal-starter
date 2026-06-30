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

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```text
Daily Schedule
----------------------------------------
Feed Breakfast | 10 min | High
Morning Walk | 30 min | High
Brush Coat | 20 min | Medium
Play Fetch | 45 min | Low

Buddy (Dog) belongs to James
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```text
============================= test session starts =============================
platform win32 -- Python 3.13
pytest-8.4.1

collected 0 items

============================ no tests ran ============================
``` 

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

```md
| Feature | Method(s) | Notes |
|---|---|---|
| Task sorting | `Scheduler.sort_tasks()` | Sorts tasks by priority first, then duration. High priority tasks appear before medium and low priority tasks. |
| Display schedule | `Scheduler.display_schedule()` | Prints a clean daily schedule in the terminal. |
| Owner information | `Owner.get_pet_info()` | Shows the pet name, species, and owner. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. The user enters owner information and pet information.
2. The user creates pet care tasks such as feeding, walking, brushing, and play.
3. The scheduler stores all tasks for the owner.
4. The scheduler sorts tasks by priority so important tasks happen first.
5. The app prints a clean daily schedule in the terminal.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
