import pandas as pd
from backend.expenses import process_expenses

def test_process_expenses():
    df = pd.DataFrame({
        "Category": ["Rent", "Utilities", "Rent"],
        "Amount": [1000, 200, 1500]
    })
    result = process_expenses(df)
    assert result["Rent"] == 2500
