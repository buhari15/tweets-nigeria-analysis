import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.decomposition import TruncatedSVD as LSA
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import nltk.corpus

import numpy as np
np.seterr(divide='ignore', invalid='ignore')

stop_words_en = nltk.corpus.stopwords.words('english')


def read_csv(filename):
    """
    This function read a text file using the pandas read_csv.
    :param filename:
    :return: the loaded file
    """
    read = pd.read_csv(filename)
    return read


def count_vectorizer(tweets):
    """
    This function act as vectorizer using the CountVectorizer.
    :param tweets:
    :return:
    """
    count_v = CountVectorizer(stop_words=stop_words_en, ngram_range=(2, 3))
    c_tweet = count_v.fit_transform(tweets)
    return count_v, c_tweet


def tfidf_vectorizer(tweets):
    """
    This function act as vectorizer using the TFIDF approach
    :param tweets:
    :return: vectorized text
    """
    tfidf_vect = TfidfVectorizer(stop_words=stop_words_en, use_idf=True, max_features=1000,  smooth_idf=True,  ngram_range=(2, 3))
    data = tfidf_vect.fit_transform(tweets)

    return tfidf_vect, data


def lsa_model(tfidf_vect, topics_n):
    """
    This function define the model for topic modelling using the Latent Semantic Analysis
    :param tfidf_vect:
    :param topics_n:
    :return: model
    """
    model = LSA(n_components=topics_n, algorithm='randomized', n_iter=5, random_state=42)
    model = model.fit(tfidf_vect)
    return model


def lda_model(data, topics_n):
    """
    This function define the model for topic modelling using the Latent Dirichlet Allocation
    :param data:
    :param topics_n:
    :return: the model
    """
    model = LDA(n_components=topics_n, n_jobs=-1, learning_method='online', random_state=42, max_iter=1)
    model = model.fit(data)
    return model



