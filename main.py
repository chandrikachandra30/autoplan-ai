from planner_agent import plan_tasks
from scheduler import schedule_tasks
from integrations.google_calendar import create_calendar_event
from integrations.notion import create_notion_task

def autoplan_ai(goal):
    plan = plan_tasks(goal)
    tasks = schedule_tasks(plan)
    for t in tasks:
        create_calendar_event(t)
        create_notion_task(t)
    return tasks

if __name__ == "__main__":
    result = autoplan_ai("Plan my marketing campaign for 30 days")
    print(result)
