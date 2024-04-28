'''
This study is done on a set of social interactions limited to the first two days of December 2015, as these were
the worst days of the crisis. The analysis was restricted to a set of 6000 tweets, for want of computing power.
The tweets were extracted by looking for the hashtag #ChennaiFloods.

https://www.analyticsvidhya.com/blog/2016/07/capstone-project/
'''

import pandas as pd
from pymongo import MongoClient
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

df = pd.read_csv('data/output_got.csv')
# client = MongoClient('localhost', 27017)
# db = client['twitter_db']
# collection = db['twitter_collection']
# df = pd.DataFrame(list(collection.find()))

# # Get the hashtags and find most used
# hashtags = []
# for hs in df["hashtags"]: # Each entry may contain multiple hashtags. Split.
#     hashtags += hs.split(" ")
#
# fdist1 = FreqDist(hashtags)
# fdist1.plot(10)
#
# # Get the users and find most used
# users = df["user"].tolist()
# fdist2 = FreqDist(users)
# fdist2.plot(10)

# Text analysis
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re, string, operator
import nltk

tweets_texts = df["text"].tolist()
stopwords=stopwords.words('english')
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

def process_tweet_text(tweet):
    if tweet.startswith('@null'):
        return "[Tweet not available]"
    tweet = re.sub(r'\$\w*','',tweet) # Remove tickers
    tweet = re.sub(r'https?:\/\/.*\/\w*','',tweet) # Remove hyperlinks
    tweet = re.sub(r'['+string.punctuation+']+', ' ',tweet) # Remove puncutations like 's
    tweet = tweet.encode("ascii", "ignore")
    twtok = TweetTokenizer(strip_handles=True, reduce_len=True)
    tokens = twtok.tokenize(tweet)
    tokens = [i.lower() for i in tokens if i not in stopwords and len(i) > 2 and i in english_vocab]

    return tokens

words = []
for tw in tweets_texts:
    words += process_tweet_text(tw)

#print(words)

# fdist3 = FreqDist(words)
# sorted_freqdist = sorted(fdist3.items(), key=operator.itemgetter(1),reverse=True)
#fdist3.plot(10)
# most_freq_w = sorted_freqdist[:5]
# print(most_freq_w)
# least_freq_w = sorted_freqdist[len(sorted_freqdist)-5:]
# print(least_freq_w)

# # Collocations
# from nltk.collocations import *
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# finder = BigramCollocationFinder.from_words(words, 5)
# finder.apply_freq_filter(5)
# print(finder.nbest(bigram_measures.likelihood_ratio, 10))

# Clustering
cleaned_tweets = []
for tw in tweets_texts:
    words = process_tweet_text(tw)
    cleaned_tweet = " ".join(w for w in words if len(w) > 2 and w.isalpha()) #Form sentences of processed words
    cleaned_tweets.append(cleaned_tweet)
df['CleanTweetText'] = cleaned_tweets


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(use_idf=True, ngram_range=(1,3))
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_tweets)
feature_names = tfidf_vectorizer.get_feature_names() # NUm column or num phrases

from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)
# # Multi Dimensional Scaling
# from sklearn.manifold import MDS
# mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
# pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
# xs, ys = pos[:, 0], pos[:, 1]


# K-Means Clustering
from sklearn.cluster import KMeans
num_clusters = 3
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()
df['ClusterID'] = clusters
# print(df['ClusterID'].value_counts())

# # Top 10 words used in each clusters
# #sort cluster centers by proximity to centroid
# order_centroids = km.cluster_centers_.argsort()[:, ::-1]
# for i in range(num_clusters):
#     print("Cluster {} : Words :".format(i))
#     for ind in order_centroids[i, :10]:
#         print(' %s' % feature_names[ind])

from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
texts = [text for text in cleaned_tweets if len(text) > 2]
doc_clean = [clean(doc).split() for doc in texts]
dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
ldamodel = models.ldamodel.LdaModel(doc_term_matrix, num_topics=6, id2word = dictionary, passes=5)
for topic in ldamodel.show_topics(num_topics=6, formatted=False, num_words=6):
    print("Topic {}: Words: ".format(topic[0]))
    topicwords = [w for (w, val) in topic[1]]
    print(topicwords)




