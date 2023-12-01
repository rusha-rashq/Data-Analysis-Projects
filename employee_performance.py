import pandas as pd

def analyze_performance(data_file):
    # Read the data
    df = pd.read_csv(data_file)

    # Calculate the average score across all metrics for each employee
    df['Average Performance'] = df[['Sales Performance', 'Customer Satisfaction', 'Project Delivery']].mean(axis=1)

    # Identify top performers (above 90th percentile)
    top_performers = df[df['Average Performance'] > df['Average Performance'].quantile(0.9)]

    # Identify underperformers (below 10th percentile)
    underperformers = df[df['Average Performance'] < df['Average Performance'].quantile(0.1)]

    # Calculate average team performance
    team_performance = df.groupby('Team')['Average Performance'].mean().reset_index()

    # Writing results to a text file
    with open('employee_performance_report.txt', 'w') as file:
        file.write("Employee Performance Report\n")
        file.write("\nTop Performers:\n")
        file.write(top_performers.to_string(index=False))
        file.write("\n\nUnderperformers:\n")
        file.write(underperformers.to_string(index=False))
        file.write("\n\nAverage Team Performance:\n")
        file.write(team_performance.to_string(index=False))

    print("Report generated successfully.")

if __name__ == "__main__":
    # Replace 'employee_data.csv' with the path to your data file
    analyze_performance('/Users/rushalidhar/Desktop/Invisible/Python/Employee Performance/employee_data.csv')
    