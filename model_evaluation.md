# Model Evaluation

## Categorizer (TF-IDF + Logistic Regression)
| Metric | Value |
|--------|-------|
| Train size | 336 |
| Test size | 84 |
| Accuracy | 97.6% |
| Macro F1 | 0.965 |

## Classification Report
```
               precision    recall  f1-score   support

        Bills       0.86      1.00      0.92        12
Entertainment       1.00      0.71      0.83         7
         Food       1.00      1.00      1.00        21
       Health       1.00      1.00      1.00         6
        Other       1.00      1.00      1.00        12
     Shopping       1.00      1.00      1.00        12
    Transport       1.00      1.00      1.00        14

     accuracy                           0.98        84
    macro avg       0.98      0.96      0.97        84
 weighted avg       0.98      0.98      0.98        84

```

## Observations
- Food, Transport, Shopping, Health and Other are classified perfectly on the test set.
- Weakest class is Entertainment (recall 0.71): some entertainment descriptions were confused with Bills because subscriptions (Netflix, Spotify) resemble recurring bills.
- Results come from **synthetic** data with repeated merchant names, so real-world accuracy will be lower.

## Improvements
- Train on real transactions
- Add character n-grams for unseen merchant spellings
- Add a "confidence" score and ask the user when confidence is low

## Forecaster
Linear regression on monthly totals; verified by unit tests (perfect linear trend gives exact next value, never negative). With only a few months of data it is a rough estimate.
