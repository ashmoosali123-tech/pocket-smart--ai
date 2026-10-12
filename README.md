# POCKETsmart AI – Your Smart Money Companion

> AI-ML and GenAI Track Project

POCKETsmart AI is an AI-powered personal finance assistant. It **auto-categorizes expenses** from plain-text descriptions, **forecasts next month's spending**, and lets users **chat with an LLM** about their own spending to get simple, practical budgeting advice.

## Problem Statement
Students and young professionals find manual expense tracking tedious and generic budgeting advice unhelpful, so they overspend and cannot see where their money goes.

## Key Features
| Feature | Description |
|---------|-------------|
| Smart categorization | TF-IDF + Logistic Regression predicts the category (Food, Transport, Shopping, Bills, Entertainment, Health, Other) |
| Dashboard | Total spend, category chart, monthly trend, expense table |
| Spending forecast | Linear-regression estimate of next month's spend |
| AI chat | LLM answers questions using a summary of the user's spending |
| Local storage | SQLite database; only aggregated summaries reach the LLM |

## Results
- Categorizer accuracy: **97.6%**, macro F1: **0.965** (84-sample held-out test set, synthetic data)
- 11 automated unit tests, all passing

## Tech Stack
Python 3.10+, pandas, scikit-learn, Streamlit, SQLite, matplotlib, any chat-completion LLM API

## Repository Structure
| Folder | Contents |
|--------|----------|
| 1. Brainstorming & Ideation | Problem statement, empathy map, idea selection |
| 2. Requirement Analysis | Functional and non-functional requirements, dataset, stack |
| 3. Project Design Phase | Architecture diagram, data flow, wireframes, database design |
| 4. Project Planning Phase | Timeline, task allocation, risk plan |
| 5. Project Development | Source code, dataset, tests |
| 6.Project Testing | Test cases, model evaluation, bug log |
| 7.Project Documentation | Final report, user guide, future scope |
| 8.Project Demonstration | Demo script, presentation outline, screenshots |

## How to Run
```bash
git clone https://github.com/<your-username>/POCKETsmart-AI.git
cd POCKETsmart-AI/"5. Project Development"
pip install -r requirements.txt
cp .env.example .env            # add LLM_API_KEY, LLM_API_URL, LLM_MODEL
python data/generate_dataset.py # optional: regenerate dataset
python model/categorizer.py     # trains the model and saves metrics
streamlit run app/app.py
```
Run tests: `python -m unittest tests.test_pocketsmart -v`

## Team
| Name | Role |
|------|------|
| _Add name_ | _Add role_ |

## Disclaimer
POCKETsmart AI gives general guidance only and is not a financial advisor.
