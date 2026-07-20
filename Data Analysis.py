import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df = pd.read_excel('C:\\Users\\MANOJ\\Downloads\\Project\\fuel_station_data_500_rows.xlsx')

print("This is DataSet :\n ",pd.DataFrame(df))

print("The First Five Rows of DataSet : \n",df.head())

print("The Summary of Dataset : \n",df.describe())

print("The Missing on DataSet : \n",df.isnull().sum())

print("The information of Dataset : \n",df.info())

# 1. Countplot: Transactions by Hour
df['Hour of Day'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
plt.figure(figsize=(10, 4))
sns.countplot(data=df, x='Hour of Day', color='skyblue')
plt.title('Number of Transactions by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.show()

# 2. Line Plot: Daily Total Profit Trend
daily_profit = df.groupby('Date')['Profit'].sum().reset_index()
plt.figure(figsize=(12, 5))
sns.lineplot(data=daily_profit, x='Date', y='Profit', marker='o')
plt.title('Daily Total Profit Trend')
plt.xlabel('Date')
plt.ylabel('Total Profit (₹)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 3. Pie Chart: Payment Method Distribution
plt.figure(figsize=(6, 6))
payment_counts = df['Payment_Method'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Payment Method Distribution')
plt.axis('equal')
plt.show()

# 4. Barplot: Average Fuel Loss by Fuel Type
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Fuel_Type', y='Stock_After', estimator='mean', ci=None, palette='Set2')
plt.title('Average Stock After Sales by Fuel Type')
plt.ylabel('Average Stock After (Litres)')
plt.xlabel('Fuel Type')
plt.show()

# 5. Heatmap: Correlation Matrix
plt.figure(figsize=(10, 8))
# Exclude non-numeric columns before calculating correlation
numeric_df = df.select_dtypes(include=np.number)
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

# 6. Boxplot: Profit Distribution by Fuel Type
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Fuel_Type', y='Profit', palette='pastel')
plt.title('Profit Distribution by Fuel Type')
plt.ylabel('Profit (₹)')
plt.xlabel('Fuel Type')
plt.show()

# 7. Countplot: Customer Type Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Customer_Type', palette='Set1')
plt.title('Customer Type Distribution')
plt.xlabel('Customer Type')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.show()

# 8. Line Plot: Daily Total Sales Trend
daily_sales = df.groupby('Date')['Quantity_Liters'].sum().reset_index()
plt.figure(figsize=(12, 5))
sns.lineplot(data=daily_sales, x='Date', y='Quantity_Liters', marker='o', color='orange')
plt.title('Daily Total Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales (Litres)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 9. Barplot: Average Discount Applied by Payment Method
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Payment_Method', y='Discount_Applied', estimator='mean', ci=None, palette='Set2')
plt.title('Average Discount Applied by Payment Method')
plt.ylabel('Average Discount (₹)')
plt.xlabel('Payment Method')
plt.show()

# 10. FacetGrid: Sales Distribution by Shift and Fuel Type
g = sns.FacetGrid(df, col='Shift', row='Fuel_Type', margin_titles=True, height=4)
g.map(sns.histplot, 'Quantity_Liters', bins=10, kde=True)
g.set_axis_labels('Daily Sales (Litres)', 'Frequency')
g.set_titles(col_template='{col_name}', row_template='{row_name}')
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Sales Distribution by Shift and Fuel Type')
plt.show()


# 11. Interactive daily sales and profit
fig = px.line(df.groupby('Date').agg({'Quantity_Liters':'sum', 'Profit':'sum'}).reset_index(), 
             x='Date', y=['Quantity_Liters', 'Profit'],
             title='Daily Sales & Profit Trend',
             labels={'value': 'Amount', 'variable': 'Metric'},
             hover_data={'Date': '|%B %d, %Y'})
fig.update_layout(hovermode='x unified')
fig.show()

# 12. Pairplot with Regression for Feature Relationships
numerical_cols = ['Quantity_Liters', 'Price_Per_Liter', 'Profit', 
                 'Transaction_Duration_Seconds', 'Efficiency_Score']
sns.pairplot(df[numerical_cols].sample(100), kind='reg', diag_kind='kde',
             plot_kws={'scatter_kws': {'alpha': 0.5}})
plt.suptitle('Pairwise Relationships of Numerical Features', y=1.02)
plt.show()


# 13. Advanced Profit Analysis by Multiple Dimensions
# Trellis plot showing profit by hour, segmented by fuel type and shift
g = sns.FacetGrid(df, col='Fuel_Type', row='Shift', height=4, margin_titles=True)
g.map(sns.scatterplot, 'Hour of Day', 'Profit', alpha=0.6)
g.set_axis_labels('Hour of Day', 'Profit (₹)')
g.set_titles(col_template='{col_name}', row_template='{row_name}')
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Hourly Profit Analysis by Fuel Type and Shift')
plt.show()



# 14. Sunburst Chart for Hierarchical Data
# Multi-level hierarchy analysis
fig = px.sunburst(df, path=['Shift', 'Fuel_Type', 'Payment_Method'], 
                 values='Quantity_Liters',
                 title='Sales Composition by Shift, Fuel Type and Payment Method')
fig.show()


# 15. Animated Scatter Plot
# Create bins for time of day
df['Time_Bin'] = pd.cut(df['Hour of Day'], bins=range(6,24,2), 
                       labels=[f"{i}-{i+2}H" for i in range(6,22,2)])

fig = px.scatter(df, x='Quantity_Liters', y='Profit', 
                animation_frame='Time_Bin', animation_group='Fuel_Type',
                color='Fuel_Type', size='Price_Per_Liter',
                hover_name='Customer_Type', facet_col='Shift',
                range_x=[0, df['Quantity_Liters'].max()*1.1],
                range_y=[0, df['Profit'].max()*1.1],
                title='Transaction Patterns by Time of Day')
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
fig.show()




# 16. Bubble Plot of Sales vs Profit by Customer Type
agg_data = df.groupby(['Customer_Type', 'Fuel_Type']).agg({
    'Quantity_Liters':'mean',
    'Profit':'mean',
    'Transaction_ID':'count'
}).reset_index()

plt.figure(figsize=(12,8))
sns.scatterplot(data=agg_data, x='Quantity_Liters', y='Profit',
               size='Transaction_ID', hue='Customer_Type',
               sizes=(100, 1000), alpha=0.7, palette='viridis')

plt.title('Average Transaction Size vs Profit by Customer Type')
plt.xlabel('Average Quantity (Liters)')
plt.ylabel('Average Profit (₹)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


