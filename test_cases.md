# Test Cases

Automated tests: `5. Project Development/tests/test_pocketsmart.py`
Run: `python -m unittest tests.test_pocketsmart -v`

| ID | Module | Scenario | Input | Expected | Result |
|----|--------|----------|-------|----------|--------|
| T1 | Categorizer | Food | "Zomato dinner order" | Food | Pass |
| T2 | Categorizer | Transport | "Uber ride to office" | Transport | Pass |
| T3 | Categorizer | Bills | "Electricity bill" | Bills | Pass |
| T4 | Categorizer | Health | "Apollo pharmacy medicines" | Health | Pass |
| T5 | Categorizer | Entertainment | "Netflix subscription" | Entertainment | Pass |
| T6 | Forecaster | Empty list | [] | 0.0 | Pass |
| T7 | Forecaster | Single month | [500] | 500 | Pass |
| T8 | Forecaster | Linear trend | [100,200,300] | 400 | Pass |
| T9 | Forecaster | Falling trend | [300,200,100] | >= 0 | Pass |
| T10 | Database | Add then read | one expense | 1 row, category Food | Pass |
| T11 | Chat | No API key | any question | "not configured" message | Pass |

**Summary:** 11 run, 11 passed, 0 failed.

## Manual UI Checks (to perform before demo)
| ID | Scenario | Expected |
|----|----------|----------|
| M1 | Save expense with amount 0 | Not saved |
| M2 | Open dashboard with no data | "No expenses yet" message |
| M3 | Type description | Category auto-fills and is editable |
| M4 | Ask chat question with valid key | Relevant advice |
