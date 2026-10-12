"""Simple next-month spending forecast using linear regression on monthly totals."""
import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_next_month(monthly_totals):
    if len(monthly_totals) < 2:
        return float(monthly_totals[0]) if monthly_totals else 0.0
    X = np.arange(len(monthly_totals)).reshape(-1, 1)
    model = LinearRegression().fit(X, monthly_totals)
    return float(max(model.predict([[len(monthly_totals)]])[0], 0))
