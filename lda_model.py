import pandas as pd
from models import read_csv, tfidf_vectorizer, count_vectorizer, lda_model
from topics_output import topics_lda_tfidf, topics_lda_CVectorizers

"""
   In this file, two vectorizers are used, the TFIDF vectorizer and the count vectorizer.
   If this file is run, it will save the topics in a csv file as defined in the topics_output.py
"""

if __name__ == "__main__":
    tweets = read_csv('data.csv')
    number_topics = 10

    """
    Here the TFIDF is initialised, then the LDA model is loaded.
    To save the generated topics to a file, the topics_lda_tfidf is called.
    """
    (vectorizer, tf) = tfidf_vectorizer(tweets)
    lda_model_tfidf = lda_model(tf, number_topics)
    topics_lda_tfidf(lda_model_tfidf, vectorizer, 10)

    """
    Here the CountVectorizer is initialised, then the LDA model is loaded.
    To save the generated topics to a file, the topics_lda_CVectorizers is called.
    """

    (c_v, data) = count_vectorizer(tweets)
    lda_model_cVect = lda_model(data, number_topics)
    topics_lda_CVectorizers(lda_model_cVect, c_v, 10)


