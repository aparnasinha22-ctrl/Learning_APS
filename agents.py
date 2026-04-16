# All Agents
from llm import call_llm


def planner_agent(goal):
    prompt = f"""
    You are a planner.

    Break this goal into 5-7 simple actionable steps.

    Goal: {goal}

    Return only a numbered list.
    """
    response = call_llm(prompt)

    tasks = [t.strip() for t in response.split("\n") if t.strip()]
    return tasks


def executor_agent(task, memory):
    prompt = f"""
    You are an executor.

    Previously completed work:
    {memory}

    Now execute this task step-by-step:
    {task}

    Be concise and practical.
    """
    return call_llm(prompt)


def manager_agent(goal, tasks, memory):
    prompt = f"""
    You are a manager.

    Goal: {goal}

    Completed tasks:
    {memory}

    Remaining tasks:
    {tasks}

    Decide the next best task to execute.
    If everything is done, reply ONLY with: DONE
    Otherwise return the exact task.
    """
    return call_llm(prompt).strip()
