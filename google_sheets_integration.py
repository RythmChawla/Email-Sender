from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your downloaded credentials.json file
credentials_file = "client-server.json"
credentials = service_account.Credentials.from_service_account_file(
    credentials_file,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

# Initialize the Google Sheets API
service = build("sheets", "v4", credentials=credentials)

# Example of accessing a specific sheet
spreadsheet_id = "your-spreadsheet-id"  # Replace with your Google Sheet ID
range_name = "Sheet1!A1:D5"  # Adjust range as needed
sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get("values", [])

if not values:
    print("No data found.")
else:
    for row in values:
        print(row)
