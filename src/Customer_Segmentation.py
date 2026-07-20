import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

def run_customer_segmentation():
    print("--- Customer Segmentation using K-Means Clustering ---")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'fuel_station_data_500_rows.xlsx')
    
    try:
        df = pd.read_excel(data_path)
    except FileNotFoundError:
        print(f"Dataset not found at {data_path}. Please make sure it exists.")
        return

    # Select features for clustering
    features = ['Quantity_Liters', 'Transaction_Duration_Seconds', 'Profit']
    X = df[features].dropna()
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Determine optimal clusters using Elbow Method (we'll just default to 3 for this example)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Customer_Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Analyze the clusters
    cluster_summary = df.groupby('Customer_Cluster')[features].mean().reset_index()
    print("\nCluster Profiles (Average Values):")
    print(cluster_summary)
    
    # Visualizing the clusters (Quantity vs Profit)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, 
        x='Quantity_Liters', 
        y='Profit', 
        hue='Customer_Cluster', 
        palette='viridis',
        size='Transaction_Duration_Seconds',
        sizes=(20, 200),
        alpha=0.7
    )
    plt.title('Customer Segments: Quantity vs Profit')
    plt.xlabel('Quantity (Liters)')
    plt.ylabel('Profit (₹)')
    plt.legend(title='Cluster')
    plt.grid(True)
    
    # Save the plot
    plot_path = os.path.join(current_dir, '..', 'data', 'cluster_plot.png')
    plt.savefig(plot_path)
    print(f"\nSegmentation plot saved to {plot_path}")
    
    print("\nOperational Insight:")
    print("Cluster 0 might represent your regular customers. Cluster 1 could be low-volume/high-duration transactions (inefficient). Cluster 2 might be high-volume commercial buyers. Target loyalty programs accordingly!")

if __name__ == "__main__":
    run_customer_segmentation()
