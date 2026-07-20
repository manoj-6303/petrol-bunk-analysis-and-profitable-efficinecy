import streamlit as st
import pandas as pd
import plotly.express as px
import os

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
