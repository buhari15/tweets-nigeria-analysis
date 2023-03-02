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
from nltk.stem.wordnet import WordNetLemmatizer
import spacy

english_s = spacy.load('en_core_web_sm')
spacy_stop = english_s.Defaults.stop_words
stop_words_en = nltk.corpus.stopwords.words('english')
base = os.path.dirname(os.path.abspath(__file__))


def remove_hashtags(filename):
    """
    This function remove hashtags from tweets.
    :param filename:
    :return: tweets without hashtags
    """
    hashtags = re.sub('#[A-Za-z0-9_]+', '', filename)
    return hashtags


def remove_urls(filename):
    """
    This function remove urls from tweets.
    :param filename:
    :return: tweets without any urls.
    """
    urls_remove = re.sub(r"http\S+", '', filename)
    return urls_remove


def remove_user_mentions(filename):
    """
    This function remove any user mentioned in tweets
    :param filename:
    :return: tweets without any user mentions.
    """
    user_m_remove = re.sub('@[A-Za-z0-9_]+', '', filename)
    return user_m_remove


def preprocessing_data(filename):
    """
    This function takes the filename/path as argument.
    The file is then read with pandas json module.
    With the pandas library text are extracted.
    The function also do basic preprocessing
    :param filename:
    :return: clean processed data.
    """
    remove_url = remove_urls(str(filename))
    remove_has = remove_hashtags(str(remove_url))
    remove_s_m = remove_user_mentions(remove_has)
    data = clean(remove_s_m, fix_unicode=True, to_ascii=True, lower=True, no_numbers=True, replace_with_number="",
                 no_emoji=True, no_line_breaks=True, no_punct=True, no_digits=True, replace_with_digit="",
                 no_phone_numbers=True, replace_with_phone_number="")
    remove_s_word = ' '.join([text for text in data.split() if text not in spacy_stop and len(text) > 3])
    lemma = english_s(remove_s_word)
    processed_data = " ".join([token.lemma_ for token in lemma])

    return processed_data


def hashtags_entities(filename):
    """
    This function takes the filename/path as argument.
    The file is then read with pandas json module.
    With the pandas library entities are extracted, then normalized.
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





