# User Guide

## Installation
1. Install Python 3.10+
2. `cd "5. Project Development"` and run `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your LLM details
4. Run `streamlit run app/app.py`

## Using the App
**Add Expense:** enter a description (e.g. "Swiggy dinner") and amount. The category is predicted automatically; edit it if wrong, then press Save.

**Dashboard:** view total spend, spend by category, monthly trend, next-month forecast, and the expense table.

**AI Chat:** ask things like "Where am I overspending?" or "How can I save more?"

## Troubleshooting
| Problem | Fix |
|---------|-----|
| "LLM not configured" | Add `LLM_API_KEY` and `LLM_API_URL` in `.env` |
| Wrong category | Edit the category before saving |
| Model file missing | It trains automatically on first use, or run `python model/categorizer.py` |
