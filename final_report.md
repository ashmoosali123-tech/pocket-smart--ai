# Final Report – POCKETsmart AI

## 1. Abstract
POCKETsmart AI is a personal finance assistant that classifies expenses automatically, forecasts monthly spending, and offers LLM-based budgeting advice. The categorizer reaches 97.6% accuracy on a synthetic test set, and the application is delivered as a Streamlit app with SQLite storage.

## 2. Introduction
Cashless payments make it hard to notice small recurring spends. Users need low-effort tracking and understandable advice rather than raw numbers.

## 3. Problem Statement and Objectives
See folder 1. Objectives: automate categorization, predict spending, and provide grounded conversational advice.

## 4. Existing Solutions and Gap
Most apps require manual tagging and provide static charts. POCKETsmart AI adds automatic categorization and natural-language explanations tied to the user's own data.

## 5. System Design
Architecture in `3. Project Design Phase/architecture.png`. Components: Streamlit UI, categorizer, forecaster, LLM chat, SQLite.

## 6. Implementation
- **Data:** 420 synthetic expenses across 7 categories
- **Categorizer:** TF-IDF (1-2 grams) + Logistic Regression
- **Forecaster:** linear regression over monthly totals
- **GenAI:** system prompt limits the LLM to the provided summary and prohibits investment recommendations
- **UI:** three tabs: Add Expense, Dashboard, AI Chat

## 7. Testing and Results
- 11/11 unit tests passed
- Accuracy 97.6%, macro F1 0.965 (see `6.Project Testing/model_evaluation.md`)

## 8. Limitations
- Synthetic data inflates accuracy
- Forecast is simple and needs several months of history
- Single user, no login
- Requires an external LLM API

## 9. Ethical and Privacy Considerations
Data stays local; only category totals are sent to the LLM. The app is not a licensed financial advisor and the prompt avoids investment recommendations.

## 10. Future Scope
Receipt OCR, bank/UPI sync, budget alerts, voice input, multi-language support, better forecasting models, multi-user accounts, cloud deployment.

## 11. Conclusion
The project shows that classical ML and GenAI can be combined into a practical, privacy-conscious finance helper. Training on real data is the main next step.

## 12. References
- scikit-learn documentation
- Streamlit documentation
- Provider documentation for the chosen LLM API
