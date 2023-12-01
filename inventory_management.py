import pandas as pd

# Load inventory data
def load_inventory_data(file_path):
    return pd.read_csv(file_path)

# Identify low stock items
def identify_low_stock(inventory_df, threshold=100):
    return inventory_df[inventory_df['Current Stock'] < threshold]

# Forecast future inventory needs (simple heuristic)
def forecast_inventory(inventory_df, sales_multiplier=0.5):
    inventory_df['Forecasted Need'] = inventory_df['Historical Sales'] * sales_multiplier
    return inventory_df

# Generate report
def generate_report(inventory_df, file_path):
    with open(file_path, 'w') as file:
        file.write(inventory_df.to_string())

# Main function
def main():
    inventory_file = 'inventory_data.csv'
    report_file = 'inventory_report.txt'

    inventory_df = load_inventory_data(inventory_file)
    low_stock_items = identify_low_stock(inventory_df)
    forecasted_inventory = forecast_inventory(inventory_df)

    # Print low stock items
    print("Low Stock Items:")
    print(low_stock_items)

    # Generate report
    generate_report(forecasted_inventory, report_file)
    print(f"Inventory report generated: {report_file}")

if __name__ == "__main__":
    main()
