import sys

import pandas as pd
import math
import numpy as np
from gensim import corpora, models
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk import word_tokenize

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

from nltk import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

stopwords = set(nltk.corpus.stopwords.words('english'))
# path_to_text = 'supremecourt_1_.txt'
# path_to_cues = "legalstopwords.txt"

path_to_text = 'buscrash_foxnews.txt'
path_to_cues = "imp_words.txt"

# path_to_text = 'sometext.txt'
# path_to_cues = "blankfile.txt"

# path_to_text = 'poem.txt'
# path_to_cues = "blankfile.txt"

custom_keywords = set(line.strip() for line in open(path_to_cues))



def normalize(array):
    max_value = max(array)
    min_value = min(array)
    range = max_value - min_value
    array = [(value - min_value)/range for value in array]
    return array

def extract_sentences(text):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(text)
    sentences = [sent.lstrip(' ') for sent in sentences if len(sent) > 3]
    return sentences

def clean_sentences(sentences):
    result = []
    for sent in sentences:
        #clean_sent = [porter_stemmer.stem(word.lower()) for word in word_tokenize(sent) if word not in stopwords and len(word) > 3]
        clean_sent = [wordnet_lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sent) if
                      word not in stopwords and len(word) > 3]
        result.append(clean_sent)
    return result

# Computes "term frequency" which is the number of times a word appears in a document,
# normalized by the total number of words in blob.
def tf(word, doc):
    count = doc.count(word)
    total = len(doc)
    tf_score = count / float(total)
    return tf_score

# returns the number of documents containing word. A generator expression is passed to the sum() function.
def n_containing(word, docs):
    count = 0
    for doc in docs:
        if doc.count(word) > 0:
            count += 1
    return count

def idf(word, docs):
    doc_count = n_containing(word, docs)
    ratio = len(docs) / float(1 + doc_count )
    return math.log(ratio)

def tfidf(word, doc, docs):
    tf_score = tf(word, doc)
    idf_score = idf(word, docs)
    return tf_score * idf_score

def compute_length_scores(sentences):
    lengths = [len(sent) for sent in sentences]
    return normalize(lengths)

def compute_position_scores(sentences):
    n = len(sentences)
    position_scores = np.zeros(n)
    midpoint = int(n/2)
    for ind in range(0,midpoint):
        position_scores[ind] = position_scores[-ind] = 1 - ind/midpoint
    return position_scores

def compute_tfisf_scores(sentences):
    tfisf_scores = []
    for sent in sentences:
        sentence_score = 0
        for word in sent:
            sentence_score += tfidf(word,sent,sentences)
        sentence_score /= float(len(sent))
        tfisf_scores.append(sentence_score)
    return normalize(tfisf_scores)

def count_proper_nouns(sentences):
    proper_nouns = []
    for sent in sentences:
        tokens = nltk.word_tokenize(sent)
        pos_tagged_words = nltk.pos_tag(tokens)
        nnp_count = 0
        for word, type in pos_tagged_words:
            if type == "NNP":
                nnp_count += 1
        proper_nouns.append(nnp_count)
    return normalize(proper_nouns)

def count_cue_words(sentences):
    cue_words_count = np.zeros(len(sentences))
    if len(custom_keywords) < 1:
        return cue_words_count

    for i, sent in enumerate(sentences):
        cue_count = 0
        tokens = nltk.word_tokenize(sent)
        for word in tokens:
            if word in custom_keywords:
                cue_count += 1
        cue_words_count[i] = cue_count
    return normalize(cue_words_count)

def count_topic_words(sentences, topic_names):
    topic_words_count = []
    for sent in sentences:
        topic_count = 0
        tokens = nltk.word_tokenize(sent)
        for word in tokens:
            if word in topic_names:
                topic_count += 1
        topic_words_count.append(topic_count)
    return normalize(topic_words_count)

def identify_lda_topics(cleaned_sentences):
    dictionary = corpora.Dictionary(cleaned_sentences)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in cleaned_sentences]
    ldamodel = models.ldamodel.LdaModel(doc_term_matrix, num_topics=6, id2word=dictionary, passes=5)
    topics = ldamodel.show_topics(num_topics=1, formatted=False, num_words=6)
    # topic_names = [tp for tp, score in topics[0][1]]
    # print(topic_names)
    topic_names = []
    for topic in ldamodel.show_topics(num_topics=6, formatted=False, num_words=6):
        # print("Topic {}: Words: ".format(topic[0]))
        topicwords = [w for (w, val) in topic[1]]
        topic_names += topicwords
    return list(set(topic_names))

def compute_similarity(sent1, sent2):
    sentences = [sent1, sent2]

    from sklearn.feature_extraction.text import CountVectorizer
    c = CountVectorizer()
    bow_matrix = c.fit_transform(sentences)  # rows are sentences and the columns are words

    from sklearn.feature_extraction.text import TfidfTransformer
    normalized_matrix = TfidfTransformer().fit_transform(bow_matrix)
    similarity_graph = normalized_matrix * normalized_matrix.T
    return 1 - (similarity_graph[0,1])

def build_summary(sentences,summary_length = 5):
    summary = []
    first_sentence = sentences[0]
    summary.append(first_sentence) # FIRST IS A MUST
    for sent in sentences:
        similarity_score = compute_similarity(sent, first_sentence)
        if similarity_score > 0.7 and len(summary) + 1 < summary_length:
            summary.append(sent)
    return "\n".join(summary)

from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
def classification_model(model, data, predictors, outcome):
    kf = KFold(data.shape[0], n_folds=5)
    scores = []
    for train, test in kf:
        train_predictors = (data[predictors].iloc[train, :])
        train_target = data[outcome].iloc[train]

        model.fit(train_predictors, train_target)

        test_predictors = (data[predictors].iloc[test, :])
        test_target = data[outcome].iloc[test]

        # # Print accuracy
        # predictions = model.predict(test_predictors)
        # accuracy = metrics.accuracy_score(predictions, test_target)
        # print("Accuracy : %s" % "{0:.3%}".format(accuracy))

        score = model.score(test_predictors, test_target)
        scores.append(score)

    mean_score = np.mean(scores)
    print("Accuracy : {0:4.2f}".format(mean_score))
    return mean_score

def build_df(sentences):

    df = pd.DataFrame()#.from_dict({'Senetence': sentences})

    tfisf_scores = compute_tfisf_scores(sentences)
    df['TfIsf'] = tfisf_scores

    length_scores = compute_length_scores(sentences)
    df['Length'] = length_scores

    position_scores = compute_position_scores(sentences)
    df['Position'] = position_scores

    propernouns_scores = count_proper_nouns(sentences)
    df['ProperNouns'] = propernouns_scores

    cleaned_sentences = clean_sentences(sentences)
    topic_names = identify_lda_topics(cleaned_sentences)
    topic_words_scores = count_topic_words(sentences, topic_names)
    df['TopicWords'] = topic_words_scores

    return df

from bs4 import BeautifulSoup

import re
def read_uci_ml_case(filename):
    cleaned_sentences = []
    with open(filename) as rf:
        for line in rf:
            cleaned_sentences.append(re.sub('\s+', ' ', line.rstrip()).strip())
    page = " ".join(cleaned_sentences)
    soup = BeautifulSoup(page, "html.parser")
    catchphrases = [ctph.text for ctph in soup.findAll('catchphrase')]
    sentences = [sent.text for sent in soup.findAll('sentence')]
    return catchphrases, sentences

if __name__ == "__main__":
    master_df = pd.read_csv("master_df.csv")
    training_sentences =  master_df['Sentence'].tolist()
    training_df = build_df(training_sentences)
    predictor_variables = ['TfIsf', 'Length', 'Position', 'ProperNouns','TopicWords']
    outcome_variable = 'Important'
    training_df['Important'] = master_df['Important']

    model = LogisticRegression()
    mean_score = classification_model(model,training_df,predictor_variables,outcome_variable)
    print(mean_score)

    model.fit(training_df[predictor_variables], training_df[outcome_variable])

    catchphrases, testing_sentences = read_uci_ml_case('06_21.xml')
    testing_df = build_df(testing_sentences)
    testing_df[outcome_variable] = model.predict(testing_df[predictor_variables])
    testing_df.to_csv('results.csv')


