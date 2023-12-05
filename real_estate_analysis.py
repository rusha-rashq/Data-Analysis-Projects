import pandas as pd

def read_data(file_path):
    """Read the real estate data from a CSV file."""
    return pd.read_csv(file_path)

def analyze_trends(data):
    """Analyze trends in property prices and identify high-demand areas."""
    trends = {}

    # Highest average prices by region
    trends['highest_avg_prices'] = data.groupby('Region')['Price'].mean().sort_values(ascending=False)

    # Average price per square foot by region
    data['Price per sq ft'] = data['Price'] / data['Size (sq ft)']
    trends['avg_price_per_sq_ft'] = data.groupby('Region')['Price per sq ft'].mean().sort_values(ascending=False)

    # Count of properties by type in each region
    trends['count_by_type'] = data.groupby(['Region', 'Type']).size()

    return trends

def calculate_average_prices(data):
    """Calculate average prices by region."""
    average_prices = data.groupby('Region')['Price'].mean()
    return average_prices

def generate_report(trends, average_prices, output_file):
    """Generate a detailed market analysis report."""
    with open(output_file, 'w') as file:
        file.write("Real Estate Market Analysis Report\n")
        file.write("==================================\n\n")

        # Write trends analysis
        file.write("Trends in Property Prices:\n")
        file.write("Highest Average Prices by Region:\n")
        file.write(trends['highest_avg_prices'].to_string())
        file.write("\n\nAverage Price per Square Foot by Region:\n")
        file.write(trends['avg_price_per_sq_ft'].to_string())
        file.write("\n\nCount of Properties by Type in Each Region:\n")
        file.write(trends['count_by_type'].to_string())

        # Write average prices by region
        file.write("\n\nAverage Prices by Region:\n")
        file.write(average_prices.to_string())

def main():
    data_file = "/Users/rushalidhar/Desktop/Invisible/Python/Real Estate/real_estate_data.csv"  # Update with the correct path
    report_file = "real_estate_market_report.txt"

    data = read_data(data_file)
    trends = analyze_trends(data)
    average_prices = calculate_average_prices(data)
    generate_report(trends, average_prices, report_file)

if __name__ == "__main__":
    main()
