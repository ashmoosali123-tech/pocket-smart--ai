# Bug Log

| ID | Description | Severity | Status | Fix |
|----|-------------|----------|--------|-----|
| B1 | Model trained on the train split only when saved | Medium | Fixed | Final model is refit on the full dataset after evaluation |
| B2 | Chat crashed with no API key | High | Fixed | Returns a configuration message |
| B3 | Forecast could go negative on falling trends | Low | Fixed | Floored at 0 |
| B4 | Entertainment subscriptions sometimes labelled Bills | Low | Open | Needs real data / more features |
