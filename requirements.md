# Requirement Analysis

## Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| FR1 | User can add an expense (date, description, amount) | High |
| FR2 | System predicts category from description; user can edit it | High |
| FR3 | Expenses are stored persistently | High |
| FR4 | Dashboard shows total, category breakdown, monthly trend | High |
| FR5 | System forecasts next month's spending | Medium |
| FR6 | User can ask questions in an AI chat about their spending | High |
| FR7 | App works with missing LLM configuration without crashing | Medium |

## Non-Functional Requirements
| ID | Requirement |
|----|-------------|
| NFR1 | Category prediction under 1 second |
| NFR2 | Data stored locally; only aggregated summaries sent to the LLM |
| NFR3 | Simple, mobile-friendly interface |
| NFR4 | Categorization accuracy of at least 85% |
| NFR5 | API keys kept in `.env`, never committed |

## Assumptions and Constraints
- Users write short descriptions such as "Swiggy dinner"
- Single-user, local deployment for the MVP
- LLM needs an external API key and internet
- Currency-agnostic amounts
