# Dataset Details

| Item | Detail |
|------|--------|
| File | `5. Project Development/data/raw/expenses_dataset.csv` |
| Generator | `data/generate_dataset.py` (seed 42, reproducible) |
| Rows | 420 |
| Period | Jan 2026 – Aug 2026 |
| Columns | date, description, amount, category |

## Category Distribution
Food 103, Transport 70, Bills 61, Other 59, Shopping 58, Entertainment 37, Health 32.

## Notes
- The dataset is **synthetic**, built from realistic merchant names and amount ranges per category, with random suffixes ("upi", "online") to add variety.
- Because it is synthetic and merchant names repeat, reported accuracy is optimistic. For real deployment, retrain on real user or public transaction data (e.g. Kaggle) and expect lower scores.

## Preprocessing
1. Lowercase text
2. TF-IDF vectorization with unigrams and bigrams
3. Stratified 80/20 train-test split
