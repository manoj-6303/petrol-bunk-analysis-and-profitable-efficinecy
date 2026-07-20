# Petrol Bunk Analysis for Operational Efficiency and Profitability

This repository contains a comprehensive data analysis script for evaluating the operational efficiency and profitability of a petrol bunk (fuel station) using Python. It uses a dataset of 500 transactions to generate various visualizations and insights.

## Project Structure
- `Data Analysis.py`: The main Python script that performs the data analysis and generates visualizations.
- `fuel_station_data_500_rows.xlsx`: The dataset containing 500 records of fuel station transactions.

## Technologies Used
- **Pandas & NumPy**: For data manipulation and numerical computations.
- **Matplotlib & Seaborn**: For static data visualizations.
- **Plotly Express**: For interactive and animated data visualizations.

## Key Insights and Visualizations
The script performs comprehensive exploratory data analysis (EDA) and generates the following key visualizations:

1. **Transactions by Hour**: A countplot to understand peak business hours.
2. **Daily Total Profit Trend**: A line plot showing how profitability fluctuates daily.
3. **Payment Method Distribution**: A pie chart revealing customer payment preferences (e.g., Cash, Card, UPI).
4. **Average Fuel Loss by Fuel Type**: A bar plot showing remaining stock levels after sales for different fuel types.
5. **Correlation Matrix**: A heatmap displaying the relationships between numerical variables like quantity, price, profit, and transaction duration.
6. **Profit Distribution by Fuel Type**: A boxplot highlighting which fuel types yield the highest profit margins.
7. **Customer Type Distribution**: A countplot detailing the distribution of different customer segments.
8. **Daily Total Sales Trend**: A line plot mapping the volume of fuel sold each day.
9. **Average Discount Applied by Payment Method**: A bar plot visualizing discount trends across payment methods.
10. **Sales Distribution by Shift and Fuel Type**: A FacetGrid histogram breaking down sales across different operational shifts and fuel types.
11. **Interactive Daily Sales & Profit Trend**: A Plotly interactive line chart combining sales and profit trends with hover functionalities.
12. **Pairwise Relationships of Numerical Features**: A Seaborn pairplot with regression lines to explore correlations across sample data.
13. **Hourly Profit Analysis by Fuel Type and Shift**: A complex multi-dimensional scatter plot highlighting profitable hours segmented by shift and fuel type.
14. **Sales Composition by Shift, Fuel Type, and Payment Method**: A Plotly sunburst chart mapping the hierarchical sales data.
15. **Transaction Patterns by Time of Day**: An animated scatter plot showing transaction volume and profit shifts dynamically across time bins.
16. **Average Transaction Size vs Profit by Customer Type**: A bubble plot to analyze which customer types bring in the largest transaction volume and profit.

## How to Run
Ensure you have the required Python libraries installed:
```bash
pip install pandas numpy matplotlib seaborn plotly openpyxl
```

Run the script:
```bash
python "Data Analysis.py"
```

## Dataset Columns
- `Time`, `Date`, `Hour of Day`
- `Profit`, `Quantity_Liters`, `Price_Per_Liter`
- `Payment_Method`, `Fuel_Type`
- `Stock_After`, `Customer_Type`, `Shift`
- `Transaction_Duration_Seconds`, `Efficiency_Score`, `Discount_Applied`
