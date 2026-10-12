# Task Allocation and Risks

| Member | Responsibilities |
|--------|------------------|
| Member 1 | Dataset, categorizer, forecaster |
| Member 2 | LLM chat, prompts |
| Member 3 | Streamlit UI, database |
| Member 4 | Testing, documentation, demo |

_(Replace with real names.)_

## Risk Plan
| Risk | Impact | Mitigation |
|------|--------|------------|
| Limited real data | Lower accuracy | Synthetic dataset now; retrain on real data later |
| LLM cost or rate limits | Chat unavailable | Short prompts, graceful fallback message |
| API key leak | Security | `.env` in `.gitignore`, `.env.example` only |
| Scope creep | Delay | Freeze MVP scope; extras listed as future work |
