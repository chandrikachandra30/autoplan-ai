from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'

def create_calendar_event(task):
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': task['task'],
        'start': {'date': task['start_date']},
        'end': {'date': task['end_date']}
    }
    service.events().insert(calendarId='primary', body=event).execute()
