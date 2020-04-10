import pandas as pd


def string_br_monetary_series_to_float(series):
    return series.str.replace(',', '.').astype(float)


def generate_date_and_time_columns(df_in):
    df_out = df_in.copy()
    df_out['month'] = df_out.datetime.apply(lambda x: x.month)
    df_out['day'] = df_out.datetime.apply(lambda x: x.day)
    df_out['day_of_week'] = df_out.datetime.apply(lambda x: x.dayofweek)  # day of the week with Monday=0, Sunday=6
    df_out['hour'] = df_out.datetime.apply(lambda x: x.hour)
    return df_out


def filter_df(df_in, column_name, column_value):
    df_out = df_in.copy()
    return df_out[df_out[column_name] == column_value]


def turn_columns_to_categorical(df_in, column_list):
    df_out = df_in.copy()
    for col in column_list:
        try:
            df_out[col] = pd.Categorical(df_out[col])
        except KeyError:
            pass
    return df_out


def remove_unused_categories_in_df(df_in):
    df_out = df_in.copy()
    cat_cols = df_out.select_dtypes(include='category').columns
    for col in cat_cols:
        df_out[col] = df_out[col].cat.remove_unused_categories()
    return df_out


def get_list_of_missing_columns_in_df(df, required_cols):
    return list([col for col in required_cols if col not in df.columns])


def get_list_of_missing_keys_in_dict(dictionary, required_fields):
    return list([field for field in required_fields if field not in dictionary])
