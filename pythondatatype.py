"""
Module: Python Basics - Variables and Data Types
Description: Practicing variable assignment, basic data types, and type casting in Python.
Author: Sana Parveen
Date: 2026-11-10
"""

def main():
    # 1. Variables and basic data types
    learner_name = "Sana"
    total_steps = 10000
    daily_goal_met = True
    completion_rate = 95.5

    print(f"Learner: {learner_name}")
    print(f"Target Steps: {total_steps}")
    print(f"Goal Met: {daily_goal_met}")
    print(f"Completion Rate: {completion_rate}%")

    # 2. Checking types
    print("\nData Types:")
    print(type(learner_name))
    print(type(total_steps))
    print(type(daily_goal_met))

if __name__ == "__main__":
    main()
