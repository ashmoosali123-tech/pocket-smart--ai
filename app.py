import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st, pandas as pd
from datetime import date
from model.categorizer import predict
from model.forecaster import forecast_next_month
from llm.chat import ask
from app import db

st.set_page_config(page_title="POCKETsmart AI", page_icon="💰")
st.title("💰 POCKETsmart AI")
tab1, tab2, tab3 = st.tabs(["Add Expense", "Dashboard", "AI Chat"])

with tab1:
    desc = st.text_input("Description", placeholder="e.g. Swiggy dinner")
    amt = st.number_input("Amount", min_value=0.0, step=10.0)
    d = st.date_input("Date", date.today())
    if desc:
        cat = st.text_input("Category (auto-predicted, editable)", predict(desc))
        if st.button("Save") and amt > 0:
            db.add_expense(d, desc, amt, cat)
            st.success("Saved!")

df = db.get_expenses()

with tab2:
    if df.empty:
        st.info("No expenses yet.")
    else:
        df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
        st.metric("Total spent", f"{df['amount'].sum():,.0f}")
        st.bar_chart(df.groupby("category")["amount"].sum())
        monthly = df.groupby("month")["amount"].sum().sort_index()
        st.line_chart(monthly)
        st.metric("Forecast next month", f"{forecast_next_month(monthly.tolist()):,.0f}")
        st.dataframe(df.drop(columns=["month"]))

with tab3:
    q = st.text_input("Ask about your spending", placeholder="How can I save more?")
    if q:
        summary = "No data yet." if df.empty else df.groupby("category")["amount"].sum().to_string()
        st.write(ask(summary, q))
