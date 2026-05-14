import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_future_demand(sales_history_records):
    """
    sales_history_records: list of dictionaries with 'date' and 'quantity_sold'
    """
    if not sales_history_records or len(sales_history_records) < 7:
        return 0 # Not enough data

    df = pd.DataFrame(sales_history_records)
    
    # Convert date to datetime if it's not already
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Create feature: days since start
    start_date = df['date'].min()
    df['days_since_start'] = (df['date'] - start_date).dt.days
    
    X = df[['days_since_start']]
    y = df['quantity_sold']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict for the next 7 days
    last_day = df['days_since_start'].max()
    future_days = np.array([[last_day + i] for i in range(1, 8)])
    
    predictions = model.predict(future_days)
    
    # Total predicted demand for next 7 days
    total_predicted_demand = int(np.sum(np.maximum(0, predictions)))
    
    return total_predicted_demand
