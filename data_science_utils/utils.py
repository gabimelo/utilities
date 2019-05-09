import pandas as pd


def string_br_monetary_series_to_float(series):
    return series.str.replace(',', '.').astype(float)


def generate_date_and_time_columns(df):
    df['month'] = df.datetime.apply(lambda x: x.month)
    df['day'] = df.datetime.apply(lambda x: x.day)
    df['day_of_week'] = df.datetime.apply(lambda x: x.dayofweek)  # day of the week with Monday=0, Sunday=6
    df['hour'] = df.datetime.apply(lambda x: x.hour)

    return df


def filter_df(df, column_name, column_value):
    return df[df[column_name] == column_value]


def turn_columns_to_categorical(df, column_list):
    for col in column_list:
        try:
            df[col] = pd.Categorical(df[col])
        except KeyError:
            pass
    return df


def remove_unused_categories_in_df(df):
    cat_cols = df.select_dtypes(include='category').columns
    for col in cat_cols:
        df[col] = df[col].cat.remove_unused_categories()

    return df


def get_list_of_missing_columns_in_df(df, required_cols):
    return list([col for col in required_cols if col not in df.columns])


def get_list_of_missing_keys_in_dict(dictionary, required_fields):
    return list([field for field in required_fields if field not in dictionary])
