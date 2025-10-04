import streamlit as st
from planner_agent import plan_tasks
from scheduler import schedule_tasks

st.title("🧭 AutoPlanner.AI")
goal = st.text_area("Enter your goal:", placeholder="Plan my marketing campaign for 30 days...")

if st.button("Generate Plan"):
    plan = plan_tasks(goal)
    tasks = schedule_tasks(plan)
    st.json(tasks)
