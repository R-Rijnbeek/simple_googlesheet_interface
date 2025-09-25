from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource


SCOPES = ["https://spreadsheets.google.com/feeds"]
SERVICE_ACCOUNT_FILE = "KEY\\applied-primacy-289510-73b0cec868d7.json"

class GoogleSheetInterface():
    def __init__(self,SheetID):
        self.SCOPES = SCOPES 
        self.SERVICE_ACCOUNT_FILE = SERVICE_ACCOUNT_FILE
        self.SHEET_ID = SheetID
        self.CREDENTIALS = Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes = self.SCOPES)
        self.SERVICE: Resource = build("sheets", "v4", credentials=self.CREDENTIALS)
        self.SHEET = self.SERVICE.spreadsheets()

    def read(self,RANGE):
        sheet_read = self.SHEET.values().get(spreadsheetId=self.SHEET_ID ,range=RANGE).execute()
        return sheet_read.get("values", [])
    
    def write(self,RANGE,VALUES):
        body = {"values": VALUES}
        return self.SHEET.values().update(spreadsheetId=self.SHEET_ID, range=RANGE, valueInputOption='USER_ENTERED', body=body).execute()
    
    def clear(self,RANGE):
         return self.SHEET.values().clear(spreadsheetId=self.SHEET_ID ,range=RANGE).execute()

    # =============== EXECUTE TEST CODE ===============

if __name__ == "__main__":
    
    sheet_id ="1OckYU4X_owgTRYMsZS4wP-5lJSeYLHqrFg631fY8XFw" 
    interface = GoogleSheetInterface(sheet_id)

    read = interface.read('A1:B5')

    print(read)

    values = [
                ["hello", "world"],
                ["hola", "mundo"],
                ["hola", "mundo"],
                ["hola", "mundo"],
                ["hola", "=max(9,6)"]
    ]  

    write = interface.write('A1:B5',values)

    print(write)

    clear = interface.clear("A1:B2")

    print(clear)