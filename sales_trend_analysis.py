def analyze_sales_data_with_month_names(file_path):
    import pandas as pd

    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    latest_year = data['Date'].dt.year.max()
    filtered_data = data[data['Date'].dt.year == latest_year]

    monthly_sales = filtered_data.groupby('Month')['Sales'].sum()
    best_month = monthly_sales.idxmax()
    worst_month = monthly_sales.idxmin()
    average_sales = monthly_sales.mean()

    report_file = 'annual_sales_report.txt'
    with open(report_file, 'w') as file:
        file.write(f"Annual Sales Report for {latest_year}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Best Performing Month: {best_month}\n")
        file.write(f"Worst Performing Month: {worst_month}\n")
        file.write(f"Average Monthly Sales: {average_sales:.2f}\n")

    return report_file

csv_file_path_with_month_names = ' '
report_file_path_with_month_names = analyze_sales_data_with_month_names(csv_file_path_with_month_names)
