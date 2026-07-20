import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os

def run_prediction_model():
    print("--- Predictive Modeling: Sales and Profit ---")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'fuel_station_data_500_rows.xlsx')
    
    try:
        df = pd.read_excel(data_path)
    except FileNotFoundError:
        print(f"Dataset not found at {data_path}. Please make sure it exists.")
        return

    # Select relevant features
    features = ['Quantity_Liters', 'Price_Per_Liter', 'Transaction_Duration_Seconds', 'Efficiency_Score']
    target = 'Profit'
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Model Performance Metrics:")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R^2 Score: {r2:.4f}")
    
    # Feature Importance
    print("\nFeature Importances:")
    importances = model.feature_importances_
    for feature, importance in zip(features, importances):
        print(f"- {feature}: {importance:.4f}")
        
    print("\nOperational Insight: You can use these features to forecast expected profit on a given transaction and prioritize resources accordingly.")

if __name__ == "__main__":
    run_prediction_model()
