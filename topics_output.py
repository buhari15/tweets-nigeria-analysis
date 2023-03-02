import pandas as pd

from analysis import preprocessing_data
from models import count_vectorizer, tfidf_vectorizer
from models import lda_model, lsa_model


def topics_lsa_tfidf(model, vectorizer, words_top_n):
    """
    This function output top five topics from the corpus.
    :param model:
    :param vectorizer:
    :param words_top_n:
    :return:
    """
    with open('tfidf_lsa_topics.csv', 'a') as f:
        for ix, topic in enumerate(model.components_):
            out_put = [vectorizer.get_feature_names_out()[j] for j in topic.argsort()[:-words_top_n - 1:-1]]
            f.writelines(f"Important words in Topic {ix} \n")
            f.writelines(f' \n'.join(out_put) + "\n")


def topics_lda_tfidf(model, vectorizer, words_top_n):
    """
    This function output top five topics from the corpus.
    :param model:
    :param vectorizer:
    :param words_top_n:
    :return:
    """
    with open('tfidf_lda_topics.csv', 'a') as f:
        for ix, topic in enumerate(model.components_):
            out_put = [vectorizer.get_feature_names_out()[j] for j in topic.argsort()[:-words_top_n - 1:-1]]
            f.writelines(f"Important words in Topic {ix} \n")
            f.writelines(f' \n'.join(out_put) + "\n")


def topics_lda_CVectorizers(model, vectorizer, words_top_n):
    """
    This function output top five topics from the corpus.
    :param model:
    :param vectorizer:
    :param words_top_n:
    :return:
    """
    with open('cvect_lda_topics.csv', 'a') as f:
        for ix, topic in enumerate(model.components_):
            out_put = [vectorizer.get_feature_names_out()[j] for j in topic.argsort()[:-words_top_n - 1:-1]]
            f.writelines(f"Important words in Topic {ix} \n")
            f.writelines(f' \n'.join(out_put) + "\n")


