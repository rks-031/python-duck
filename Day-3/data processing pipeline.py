"""
Data Processing Pipeline:
1. Data source: A CSV file containing sales data with columns: 'Date', 'Product', 'Quantity', 'Price'.
2. Data processing steps:   
    - Read the CSV file.
    - Filter out rows where 'Quantity' is less than 10.
    - Calculate total sales for each product (Quantity * Price).
    - Group by 'Product' and sum the total sales.
3. Output: A new CSV file with columns: 'Product', 'Total Sales'.
"""

import pandas as pd

def process_sales_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Filter out rows where 'Quantity' is less than 10
    df_filtered = df[df['Quantity'] >= 10].copy()

    # Calculate total sales for each product
    df_filtered['Total Sales'] = df_filtered['Quantity'] * df_filtered['Price']

    # Group by 'Product' and sum the total sales
    df_grouped = df_filtered.groupby('Product', as_index=False)['Total Sales'].sum()

    # Output to a new CSV file
    df_grouped.to_csv(output_file, index=False)

# Example usage
if __name__ == "__main__":
    input_file = 'D:\\python-prac\\Day-3\\sales_data.csv'  
    output_file = 'D:\\python-prac\\Day-3\\processed_sales_data.csv'  
    process_sales_data(input_file, output_file)
    print(f"Processed data saved to {output_file}")