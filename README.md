# Petrol Bunk Analysis for Operational Efficiency and Profitability

This repository contains a comprehensive data analysis, machine learning models, and an interactive dashboard for evaluating the operational efficiency and profitability of a petrol bunk (fuel station) using Python.

## Project Structure
- `data/`: Contains the datasets and generated plots.
- `src/Data Analysis.py`: The main Python script that performs the exploratory data analysis and generates visualizations.
- `src/Predictive_Modeling.py`: Uses Random Forest to predict transaction profitability and extracts feature importances.
- `src/Customer_Segmentation.py`: Uses K-Means clustering to identify different customer groups and their purchasing behaviors.
- `src/dashboard.py`: An interactive Streamlit dashboard summarizing KPIs, sales trends, and profit margins dynamically.
- `requirements.txt`: Python dependencies needed for the project.

## Technologies Used
- **Pandas & NumPy**: For data manipulation and numerical computations.
- **Matplotlib & Seaborn**: For static data visualizations.
- **Plotly Express**: For interactive and animated data visualizations.
- **Scikit-Learn**: For Predictive Modeling (Random Forest) and Clustering (K-Means).
- **Streamlit**: For the interactive web dashboard.

## How to Run

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run Exploratory Data Analysis:**
```bash
python "src/Data Analysis.py"
```

3. **Run Predictive Modeling:**
```bash
python "src/Predictive_Modeling.py"
```

4. **Run Customer Segmentation:**
```bash
python "src/Customer_Segmentation.py"
```

5. **Launch the Interactive Dashboard:**
```bash
streamlit run "src/dashboard.py"
```

## Key Insights and Features
- **Predictive Analytics**: Forecast expected profit using `Quantity_Liters`, `Price_Per_Liter`, and `Efficiency_Score`.
- **Customer Segmentation**: Grouping customers allows tailored marketing (e.g., identifying regular bulk buyers versus infrequent visitors).
- **Interactive Dashboard**: Quickly filter insights by shift and fuel type for rapid decision making.
