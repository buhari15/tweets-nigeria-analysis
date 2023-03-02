import pandas as pd
from analysis import preprocessing_data
from models import tfidf_vectorizer, count_vectorizer, lsa_model
from topics_output import topics_lsa_tfidf

"""
   In this file, only one vectorizers are is, the TFIDF vectorizer and the count vectorizer.
   If this file is run, it will save the topics in a csv file as defined in the topics_output.py
"""

if __name__ == "__main__":

    df = pd.read_json("tweets_ng.jsonl", lines=True)
    tweets = df['text'].apply(preprocessing_data)

    number_topics = 10

    """
    Here the TFIDF is initialised, then the LSA model is loaded.
    To save the generated topics to a file, the topics_lsa_tfidf is called.
    """
    (vectorizer, tf) = tfidf_vectorizer(tweets)
    lda_model_tfidf = lsa_model(tf, number_topics)
    topics_lsa_tfidf(lda_model_tfidf, vectorizer, 10)




