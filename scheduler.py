import datetime
import json

def schedule_tasks(plan_json):
    today = datetime.date.today()
    plan = json.loads(plan_json)
    scheduled = []
    for i, t in enumerate(plan):
        start = today + datetime.timedelta(days=sum([p["duration_days"] for p in plan[:i]]))
        end = start + datetime.timedelta(days=t["duration_days"])
        t["start_date"] = str(start)
        t["end_date"] = str(end)
        scheduled.append(t)
    return scheduled
