import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from config.settings import SCOPES, CREDENTIALS_FILE, GOOGLE_SHEET_NAME, EXPENSES_SHEET_TAB

def get_expense_data():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(GOOGLE_SHEET_NAME).worksheet(EXPENSES_SHEET_TAB)
    data = sheet.get_all_records()
    return pd.DataFrame(data)
