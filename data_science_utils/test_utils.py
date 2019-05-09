import datetime

import pandas as pd
from pandas.testing import assert_series_equal, assert_frame_equal
from numpy.testing import assert_array_equal

from utils import (
    string_br_monetary_series_to_float, generate_date_and_time_columns, filter_df, turn_columns_to_categorical,
    remove_unused_categories_in_df, get_list_of_missing_columns_in_df, get_list_of_missing_keys_in_dict
)


class TestUtils(object):
    def test_string_br_monetary_series_to_float(self):
        assert_series_equal(string_br_monetary_series_to_float(pd.Series(['12,98', '1,92'])), pd.Series([12.98, 1.92]))

    def test_generate_date_and_time_columns(self):
        now = datetime.datetime.now()
        assert_frame_equal(generate_date_and_time_columns(pd.DataFrame([now], columns=['datetime'])),
                           pd.DataFrame({'datetime': [now],
                                         'month': [now.month],
                                         'day': [now.day],
                                         'day_of_week': [now.weekday()],
                                         'hour': [now.hour]}))

    def test_filter_df(self):
        assert_frame_equal(filter_df(pd.DataFrame([4, 4, 4, 5, 5, 5, 6, 6, 6], columns=['month']), 'month', 4),
                           pd.DataFrame({'month': [4, 4, 4]}))

    def test_turn_columns_to_categorical(self):
        df = turn_columns_to_categorical(pd.DataFrame({'month': [4, 4, 4],
                                                       'day': [5, 6, 7],
                                                       'day_of_week': [1, 2, 3]}), ['month', 'day'])
        assert df.dtypes['month'] == 'category'
        assert df.dtypes['day'] == 'category'
        assert df.dtypes['day_of_week'] == 'int'

    def test_remove_unused_categories_in_df(self):
        df = turn_columns_to_categorical(pd.DataFrame({'month': [4, 4, 4],
                                                       'day': [5, 6, 7],
                                                       'day_of_week': [1, 2, 3]}), ['month', 'day'])
        assert_array_equal(df.day.cat.categories.values, [5, 6, 7])
        df = filter_df(df, 'day', 5)
        assert_array_equal(df.day.cat.categories.values, [5, 6, 7])
        df = remove_unused_categories_in_df(df)
        assert_array_equal(df.day.cat.categories.values, [5])

    def test_get_list_of_missing_columns_in_df(self):
        assert get_list_of_missing_columns_in_df(pd.DataFrame({'a': [1], 'b': [2]}), ['b', 'c']) == ['c']


    def test_get_list_of_missing_keys_in_dict(self):
        assert get_list_of_missing_keys_in_dict({'a': 1, 'b': 2}, ['b', 'c']) == ['c']
