
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_engagement_rates(df):
    df['engagement_rate'] = (df['likes'] + df['comments'] + df['shares']) / df['followers']

def track_follower_growth(df):
    df['follower_growth'] = df['followers'].diff().fillna(0)

def find_most_popular_posts(df):
    return df.sort_values(by='engagement_rate', ascending=False).head(5)

def generate_report(df, report_file_path):
    with open(report_file_path, 'w') as file:
        file.write("Social Media Analytics Report\n")
        file.write("================================\n\n")

        # Follower Growth
        total_growth = df['follower_growth'].sum()
        file.write(f"Total Follower Growth: {total_growth}\n")

        # Engagement Rates
        avg_engagement_rate = df['engagement_rate'].mean()
        file.write(f"Average Engagement Rate: {avg_engagement_rate:.2%}\n")

        # Most Popular Posts
        popular_posts = find_most_popular_posts(df)
        file.write("\nMost Popular Posts:\n")
        for _, row in popular_posts.iterrows():
            file.write(f"Post ID: {row['post_id']}, Engagement Rate: {row['engagement_rate']:.2%}\n")

def main():
    data_file = 'social_media_data.csv'
    report_file = 'social_media_report.txt'

    df = load_data(data_file)
    calculate_engagement_rates(df)
    track_follower_growth(df)

    generate_report(df, report_file)
    print("Report generated successfully.")

if __name__ == "__main__":
    main()
