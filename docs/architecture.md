# Architecture

## Data Flow
Google Sheets (Expenses tab) --> gspread --> DataFrame --> Streamlit Dashboard

## Modules
- gsheet_connector.py: Fetches data
- expenses.py: Processes expenses
- app.py: Frontend interface
