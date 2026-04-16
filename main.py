from agents import planner_agent, executor_agent, manager_agent
from memory import Memory


def main():
    goal = input("Enter your goal: ")

    print("\n[Planner] Generating tasks...\n")
    tasks = planner_agent(goal)

    for t in tasks:
        print("-", t)

    memory = Memory()

    print("\n[Execution Started]\n")

    while True:
        next_task = manager_agent(goal, tasks, str(memory))

        if "DONE" in next_task.upper():
            print("\n✅ Goal Completed!")
            break

        print(f"\n[Manager] Next Task: {next_task}")

        result = executor_agent(next_task, str(memory))

        print(f"[Executor Result]: {result}")

        memory.add(next_task, result)


if __name__ == "__main__":
    main()
