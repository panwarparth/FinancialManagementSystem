def process_expenses(df):
    # Example logic: sum by category
    return df.groupby("Category")["Amount"].sum()
