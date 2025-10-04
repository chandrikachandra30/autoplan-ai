from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_TOKEN"))

def create_notion_task(task):
    notion.pages.create(
        parent={"database_id": "your_database_id"},  # <-- Replace with your Notion database ID!
        properties={
            "Name": {"title": [{"text": {"content": task["task"]}}]},
            "Priority": {"select": {"name": task["priority"]}},
            "Start Date": {"date": {"start": task["start_date"]}},
            "End Date": {"date": {"start": task["end_date"]}},
        },
    )
