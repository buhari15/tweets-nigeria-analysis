import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.casual import casual_tokenize
from collections import Counter


def read_pandas_csv(filename):
    data = pd.read_csv(filename)
    return data


def change_columns_name(data):
    columns_new = data.rename(
        columns={
            'created_at': 'Date',
        }
    )
    return columns_new


def entities_hashtag(data):
    df = data['Date']
    return df


if __name__ == "__main__":
    read_csv = read_pandas_csv('to_csv_data.csv')
    chanji = change_columns_name(read_csv)

    print(chanji[['Date']])
