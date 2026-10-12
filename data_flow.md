# Data Flow and Design

## Architecture
See `architecture.png`. Flow: User → Streamlit UI → backend logic → (Categorizer | Forecaster | LLM Chat | SQLite).

## Add-Expense Flow
1. User types description, amount, date
2. Categorizer predicts category; user can edit it
3. Record saved to SQLite

## Dashboard Flow
1. App reads all expenses from SQLite
2. Groups by category and by month
3. Charts totals; forecaster predicts next month from monthly totals

## Chat Flow
1. User asks a question
2. App builds a **category-wise spending summary** (no raw descriptions)
3. Summary + question are sent with a system prompt to the LLM
4. Reply is shown; if the LLM is not configured, a setup message appears

## Database Design
Table `expenses`

| Column | Type | Note |
|--------|------|------|
| id | INTEGER | Primary key, autoincrement |
| date | TEXT | ISO date |
| description | TEXT | User text |
| amount | REAL | Amount spent |
| category | TEXT | Predicted or edited |

## Model Design
- **Categorizer:** TF-IDF (1-2 grams) → Logistic Regression (C=5)
- **Forecaster:** Linear Regression on monthly totals, floored at 0
- **Prompt design:** system prompt restricts the LLM to the given summary and forbids investment recommendations
