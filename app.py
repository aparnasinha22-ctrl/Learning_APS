import streamlit as st
from agents import planner_agent, executor_agent, manager_agent
from memory import Memory

st.set_page_config(page_title="Autonomous Task Planner", layout="wide")

st.title("🧠 Autonomous Task Planner")
st.write("Enter a goal and watch AI agents plan and execute it.")

# Session state (important)
if "memory" not in st.session_state:
    st.session_state.memory = Memory()

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "running" not in st.session_state:
    st.session_state.running = False


# Input
goal = st.text_input("Enter your goal:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Planning"):
        if goal:
            st.session_state.tasks = planner_agent(goal)
            st.session_state.memory = Memory()
            st.session_state.running = True

with col2:
    if st.button("🛑 Stop"):
        st.session_state.running = False


# Display tasks
if st.session_state.tasks:
    st.subheader("📋 Planned Tasks")
    for t in st.session_state.tasks:
        st.write(f"- {t}")


# Execution loop (step-by-step UI)
if st.session_state.running:

    st.subheader("⚙️ Execution")

    next_task = manager_agent(
        goal,
        st.session_state.tasks,
        str(st.session_state.memory)
    )

    if "DONE" in next_task.upper():
        st.success("✅ Goal Completed!")
        st.session_state.running = False
    else:
        st.info(f"👉 Next Task: {next_task}")

        result = executor_agent(
            next_task,
            str(st.session_state.memory)
        )

        st.write("**Result:**")
        st.write(result)

        st.session_state.memory.add(next_task, result)


# Show memory
if str(st.session_state.memory):
    st.subheader("🧠 Memory")
    st.text(str(st.session_state.memory))
