import matplotlib.pyplot as plt
import sqlite3 as sql
import pandas as pd
import seaborn as sns

def generatebarChart(title, xlabel, ylabel, keys, values, filename):
    #Create plot
    plt.figure(figsize=(22, 6))
    plt.bar(keys, values, color='blue', alpha=0.7, edgecolor='black')

    # Add title and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Save the plot
    plt.grid(axis='y', alpha=0.75)
    fname = f"soejlediagram_{filename}.png"
    plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)

try:
    # connect to db
    conn = sql.connect('northwind.db')
    cursor = conn.cursor()
    conn.commit()

    # get customers
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    
    # Get country from customers
    df = pd.DataFrame(rows)
    country_counts = df[8].value_counts()

    generatebarChart('Distribution of Customers in countries','Countries','Number of customers',country_counts.index,country_counts.values,'customer_by_country')

    # get orders
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    
    # Get country from orders
    df = pd.DataFrame(rows)
    country_counts = df[13].value_counts()

    generatebarChart('Distribution of orders in countries','Countries','Number of orders',country_counts.index,country_counts.values,'orders_by_country')

    # get products
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)

    # Plot histogram with KDE for normal distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df[5], bins=30, kde=True, color='skyblue', edgecolor='black', alpha=0.7)
    
    plt.title('Normal Distribution of Unit Prices')
    plt.xlabel('Unit Price')
    plt.ylabel('Density')
    
    plt.grid(axis='y', alpha=0.75)
    fname = "histogram.png"
    plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)

except sql.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()

