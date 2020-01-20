import pandas as pd


def main():
    df = pd.read_csv('toggl_report.csv', usecols=['Duration', 'Tags'])
    df.Duration = pd.to_timedelta(df.Duration)

    print(df.groupby('Tags').sum().sort_values('Duration', ascending=False))

    total_seconds = df.Duration.sum().total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    print(f'Overall total: {hours}h{minutes}m')


if __name__ == '__main__':
    main()

