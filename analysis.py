import nltk.corpus
import pandas as pd
import re
import os
from cleantext import clean
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.casual import casual_tokenize
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from spacy.lang.en import English
from nltk.stem.wordnet import WordNetLemmatizer

stop_words_en = nltk.corpus.stopwords.words('english')
base = os.path.dirname(os.path.abspath(__file__))


def remove_hashtags(tweets):
    """
    This function remove hashtags from tweets.
    :param tweets:
    :return: tweets without hashtags
    """
    hashtags = re.sub('#[A-Za-z0-9_]+', '', tweets)
    return hashtags


def remove_urls(tweets):
    """
    This function remove urls from tweets.
    :param tweets:
    :return: tweets without any urls.
    """
    urls_remove = re.sub(r"http\S+", '', tweets)
    return urls_remove


def remove_user_mentions(tweets):
    """
    This function remove any user mentioned in tweets
    :param tweets:
    :return: tweets without any user mentions.
    """
    user_m_remove = re.sub('@[A-Za-z0-9_]+', '', tweets)
    return user_m_remove


def preprocessing_data(tweets):
    """
    This function takes the filename/path as argument.
    The file is then read with pandas json module
    With the pandas text are extracted.
    The function also do basic preprocessing, it removed.
    The most frequent hashtags are counted and save to a csv file.
    :param tweets:
    :return: clean processed data.
    """
    lemma = WordNetLemmatizer()
    df = pd.read_json(tweets, lines=True)
    tweets = df['text'].astype(str).str.lower()
    remove_stop_w = [stw for stw in tweets if stw not in stop_words_en]
    remove_url = remove_urls(str(remove_stop_w))
    remove_has = remove_hashtags(str(remove_url))
    remove_s_m = remove_user_mentions(remove_has)
    data = clean(remove_s_m, no_emoji=True, no_line_breaks=True, no_punct=True,
                 no_phone_numbers=True, replace_with_phone_number="")

    clean_data = "".join(lemma.lemmatize(text, pos='v') for text in data)

    return clean_data


def hashtags_entities(filename):
    """
    This function takes the filename/path as argument.
    The file is then read with pandas json module
    With the pandas entities are extracted, then normalized.
    The most frequent hashtags are counted and save to a csv file.
    :param filename:
    :return: most frequent hashtags.
    """
    read_data = pd.read_json(filename, lines=True)
    entities = read_data['entities']
    normalized = pd.json_normalize(entities, record_path=['hashtags'])
    hashtags = normalized.drop(['indices'], axis=1)
    hashtags = hashtags.rename(
        columns={
            'text': 'hashtags'
        }
    )
    most_freq = hashtags.value_counts()
    most_freq.to_csv('most_freq.csv')
    return most_freq


def most_active_users(filename):
    """
    This function takes the filename/path as argument.
    The file is then read with pandas json module
    With the pandas user data are extracted, then normalized.
    The most active users are counted and save to a csv file.
    :param filename:
    :return: most active users.
    """
    read_data = pd.read_json(filename, lines=True)
    user = read_data['user']
    normalized_user = pd.json_normalize(user)
    screen_name = normalized_user['screen_name']
    most_active = screen_name.value_counts()
    most_active.to_csv('most_active.csv')
    return most_active


if __name__ == "__main__":
    # tweet_data = hashtags_entities(base + '/tweets_ng.jsonl')
    # user_active = most_active_users(base + '/tweets_ng.jsonl')
    tweets_d = preprocessing_data(base + '/tweets_ng.jsonl')
    print(tweets_d)
    print(len(tweets_d))

    with open('text_tokens.csv', 'w') as w:
        write = w.write(str(tweets_d))
        print('data saved', write)
