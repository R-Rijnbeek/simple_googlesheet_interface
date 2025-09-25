



import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


SCOPES = ["https://spreadsheets.google.com/feeds"]

SERVICE_ACCOUNT_FILE = "applied-primacy-289510-73b0cec868d7.json"

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)


service = build("sheets", "v4", credentials=credentials)

sheet = service.spreadsheets()

sheet_id ="1OckYU4X_owgTRYMsZS4wP-5lJSeYLHqrFg631fY8XFw" 

range = 'A1:B5'

# read

sheet_read = sheet.values().get(spreadsheetId=sheet_id,range=range).execute()

values = sheet_read.get("values", [])
for row in values:
    print(row)

# write


values = [
    ["hello", "world"],
    ["hola", "mundo"],
    ["hola", "mundo"],
    ["hola", "mundo"],
    ["hola", "mundo"]
]  

body = {"values": values}

sheet_write = sheet.values().update(spreadsheetId=sheet_id,range='A1:B5',valueInputOption='RAW', body=body).execute()

sheet_read = sheet.values().get(spreadsheetId=sheet_id,range=range).execute()

values = sheet_read.get("values", [])
for row in values:
    print(row)

# delete

#sheet_clear = sheet.values().clear(spreadsheetId=sheet_id,range='A1:B2').execute()
#sheet_read = sheet.values().get(spreadsheetId=sheet_id,range=range).execute()

values = sheet_read.get("values", [])
for row in values:
    print(row)