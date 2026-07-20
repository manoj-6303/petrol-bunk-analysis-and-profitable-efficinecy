import streamlit as st
import pandas as pd
import plotly.express as px
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Petrol Bunk Dashboard", layout="wide")

st.title("⛽ Petrol Bunk Operations & Profitability Dashboard")

# Load data
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'fuel_station_data_500_rows.xlsx')
    try:
        df = pd.read_excel(data_path)
        df['Hour of Day'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# Create tabs
tab1, tab2 = st.tabs(["📊 Main Dashboard", "🤖 Predictive Analytics"])

with tab1:
    # Sidebar filters
    st.sidebar.header("Filters")
    selected_fuel = st.sidebar.multiselect("Select Fuel Type", options=df['Fuel_Type'].unique(), default=df['Fuel_Type'].unique())
    selected_shift = st.sidebar.multiselect("Select Shift", options=df['Shift'].unique(), default=df['Shift'].unique())

    # Filter data
    filtered_df = df[(df['Fuel_Type'].isin(selected_fuel)) & (df['Shift'].isin(selected_shift))]

    # Key Metrics
    st.markdown("### Key Performance Indicators (KPIs)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Profit (₹)", f"{filtered_df['Profit'].sum():,.2f}")
    col2.metric("Total Fuel Sold (Liters)", f"{filtered_df['Quantity_Liters'].sum():,.2f}")
    col3.metric("Total Transactions", f"{len(filtered_df)}")
    col4.metric("Avg Efficiency Score", f"{filtered_df['Efficiency_Score'].mean():.2f}")

    st.markdown("---")

    # Visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Profit by Fuel Type")
        fig_profit = px.box(filtered_df, x="Fuel_Type", y="Profit", color="Fuel_Type")
        st.plotly_chart(fig_profit, use_container_width=True)

    with col2:
        st.markdown("#### Transactions by Hour")
        fig_hour = px.histogram(filtered_df, x="Hour of Day", nbins=24, color_discrete_sequence=['skyblue'])
        st.plotly_chart(fig_hour, use_container_width=True)

    st.markdown("#### Sales & Profit Trend over Time")
    daily_trend = filtered_df.groupby('Date').agg({'Quantity_Liters': 'sum', 'Profit': 'sum'}).reset_index()
    fig_trend = px.line(daily_trend, x="Date", y=["Quantity_Liters", "Profit"], title="Daily Trends")
    st.plotly_chart(fig_trend, use_container_width=True)

    st.markdown("### Operational Recommendations")
    st.info("💡 **Tip**: Use the sidebar to drill down into specific shifts or fuel types. High transaction volume during specific hours suggests a need for increased staffing.")

with tab2:
    st.markdown("### Machine Learning: Profit Prediction")
    st.write("Using a **Random Forest Regressor** to predict transaction profit based on key operational features.")
    
    # ML Logic
    features = ['Quantity_Liters', 'Price_Per_Liter', 'Transaction_Duration_Seconds', 'Efficiency_Score']
    target = 'Profit'
    
    # Ensure no missing values for the model
    ml_df = df.dropna(subset=features + [target])
    
    X = ml_df[features]
    y = ml_df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    # Layout for ML results
    col_metrics, col_importance = st.columns([1, 2])
    
    with col_metrics:
        st.markdown("#### Model Performance")
        st.metric("Model Accuracy (R² Score)", f"{r2 * 100:.2f}%")
        st.metric("Mean Squared Error", f"{mse:.2f}")
        st.success("An R² score near 100% indicates the model is highly accurate at predicting profit.")

    with col_importance:
        st.markdown("#### Feature Importance")
        st.write("Which features impact your profit the most?")
        
        importance_df = pd.DataFrame({
            'Feature': features,
            'Importance (%)': model.feature_importances_ * 100
        }).sort_values(by='Importance (%)', ascending=True)
        
        fig_importance = px.bar(
            importance_df, 
            x='Importance (%)', 
            y='Feature', 
            orientation='h', 
            color='Importance (%)',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_importance, use_container_width=True)
        
    st.markdown("### Operational Insights")
    st.info("💡 **Insight**: Fuel quantity and price fundamentally drive profit. However, identifying how much efficiency scores and transaction durations play a role can help tweak on-the-ground operations. If transaction duration starts eating into volume during peak hours, profitability drops.")
