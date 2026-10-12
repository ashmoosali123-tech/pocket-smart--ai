"""Train and use the expense categorizer (TF-IDF + Logistic Regression)."""
import json, joblib, pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, f1_score

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data/raw/expenses_dataset.csv"
MODEL = BASE / "model/categorizer.joblib"
METRICS = BASE / "model/metrics.json"

def _pipe():
    return make_pipeline(TfidfVectorizer(ngram_range=(1, 2), lowercase=True),
                         LogisticRegression(max_iter=2000, C=5))

def train():
    df = pd.read_csv(DATA)
    X, y = df["description"], df["category"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe = _pipe().fit(Xtr, ytr)
    pred = pipe.predict(Xte)
    report = classification_report(yte, pred, zero_division=0)
    print(report)
    METRICS.write_text(json.dumps({
        "accuracy": round(accuracy_score(yte, pred), 4),
        "macro_f1": round(f1_score(yte, pred, average="macro"), 4),
        "train_size": len(Xtr), "test_size": len(Xte), "report": report}, indent=2))
    final = _pipe().fit(X, y)
    joblib.dump(final, MODEL)
    return final

def predict(description: str) -> str:
    if not MODEL.exists():
        train()
    return joblib.load(MODEL).predict([description])[0]

if __name__ == "__main__":
    train()
