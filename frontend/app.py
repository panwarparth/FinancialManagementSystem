import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.gsheet_connector import get_expense_data

st.title(" Financial Management System")

try:
    df = get_expense_data()
    st.success("✅ Connected to Google Sheets")
    st.write("### 📋 Expense Records")
    st.dataframe(df)

    if not df.empty:
        st.write("### 📊 Expense Summary by Category")
        st.bar_chart(df.groupby("Category")["Amount"].sum())
except Exception as e:
    st.error(f"❌ Error loading data:\n\n{e}")
