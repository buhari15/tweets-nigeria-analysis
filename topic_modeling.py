import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.casual import casual_tokenize
from collections import Counter
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import nltk.corpus

stop_words_en = nltk.corpus.stopwords.words('english')


def read_csv(filename):
    """
    This function read a text file using the pandas read_csv.
    :param filename:
    :return: the loaded file
    """
    read = pd.read_csv(filename)
    return read

def c_vectorizer(tweets):
    c_v = CountVectorizer(stop_words=stop_words_en, ngram_range=(2,3))
    return

def vectorized_topic(tweets):
    """
    This function act as vectorizer using the TFIDF approach
    :param tweets:
    :return: vectorized text
    """
    vectorizer = TfidfVectorizer(stop_words=stop_words_en, ngram_range=(2, 3))
    tf = vectorizer.fit_transform(tweets)

    return vectorizer, tf


def topic_model(tf, topics_n):
    """
    This function define the model for topic modelling using the Latent Dirichlet Allocation
    :param tf:
    :param topics_n:
    :return: the model
    """
    model = LDA(n_components=topics_n, n_jobs=-1)
    model = model.fit(tf)
    return model


def top_five(model, vectorizer, words_top_n):
    """
    This function output top five topics from the corpus.
    :param model:
    :param vectorizer:
    :param words_top_n:
    :return:
    """
    for ix, topic in enumerate(model.components_):
        print(f"Important words in Topic {ix}:")
        print([vectorizer.get_feature_names_out()[j] for j in topic.argsort()[:-words_top_n - 1:-1]])
        print('\t')


if __name__ == "__main__":
    tweets = read_csv('text_tokens_updated.csv')
    number_topics = 5
    (vectorizer, tf) = vectorized_topic(tweets)
    lda_model = topic_model(tf, number_topics)
    top_five(lda_model, vectorizer, 10)
