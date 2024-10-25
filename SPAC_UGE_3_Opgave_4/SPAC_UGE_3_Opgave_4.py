import matplotlib.pyplot as plt
import sqlite3 as sql
import pandas as pd
import seaborn as sns

def generatebarChart(title, xlabel, ylabel, keys, values, filename):
    plt.figure(figsize=(22, 6))
    plt.bar(country_counts.index, country_counts.values, color='blue', alpha=0.7, edgecolor='black')

    # Add title and labels
    plt.title('Distribution of Customers in countries')
    plt.xlabel('Countries')
    plt.ylabel('Number of customers')
    
    # Show the plot
    plt.grid(axis='y', alpha=0.75)
    fname = "soejlediagram_customer_by_country.png"
    plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)

try:
    conn = sql.connect('northwind.db')
    cursor = conn.cursor()
    conn.commit()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    
    df = pd.DataFrame(rows)

    country_counts = df[8].value_counts()
    plt.figure(figsize=(22, 6))
    plt.bar(country_counts.index, country_counts.values, color='blue', alpha=0.7, edgecolor='black')

    # Add title and labels
    plt.title('Distribution of Customers in countries')
    plt.xlabel('Countries')
    plt.ylabel('Number of customers')
    
    # Show the plot
    plt.grid(axis='y', alpha=0.75)
    fname = "soejlediagram_customer_by_country.png"
    plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)

    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    
    df = pd.DataFrame(rows)
    country_counts = df[13].value_counts()
    plt.figure(figsize=(22, 6))
    plt.bar(country_counts.index, country_counts.values, color='blue', alpha=0.7, edgecolor='black')

    # Add title and labels
    plt.title('Distribution of orders from countries')
    plt.xlabel('Countries')
    plt.ylabel('Number of orders')
    
    # Show the plot
    plt.grid(axis='y', alpha=0.75)
    fname = "soejlediagram_orders_by_country.png"
    plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)


    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)

    # Plot histogram with KDE for normal distribution
    plt.figure(figsize=(10, 6))  # Set figure size
    sns.histplot(df[5], bins=30, kde=True, color='skyblue', edgecolor='black', alpha=0.7)
    
    # Add title and labels
    plt.title('Normal Distribution of Unit Prices')
    plt.xlabel('Unit Price')
    plt.ylabel('Density')
    
    # Show the plot
    plt.grid(axis='y', alpha=0.75)
    fname = "histogram.png"
    plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)



except sql.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()

