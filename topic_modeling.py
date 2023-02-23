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
    read = pd.read_csv(filename)
    return read


def vectorized_topic(tweets):
    vectorizer = TfidfVectorizer(stop_words=stop_words_en, ngram_range=(2, 3))
    tf = vectorizer.fit_transform(tweets)

    return vectorizer, tf


def topic_model(tf, topics_n):
    model = LDA(n_components=topics_n, n_jobs=-1)
    model = model.fit(tf)
    return model


def top_five(model, vectorizer, words_top_n):
    for ix, topic in enumerate(model.components_):
        print(f"Important words in Topic {ix}:")
        print([vectorizer.get_feature_names_out()[j] for j in topic.argsort()[:-words_top_n - 1:-1]])
        print('\t')


if __name__ == "__main__":
    tweets = read_csv('text_tokens.csv')
    number_topics = 5
    (vectorizer, tf) = vectorized_topic(tweets)
    lda_model = topic_model(tf, number_topics)
    top_five(lda_model, vectorizer, 10)


