import gensim
import nltk
from nltk.stem import WordNetLemmatizer
import nltk as stemmer
# from textmining import stemmer

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


# Tokenize and lemmatize
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))

    return result

tx = 'Consider the data for attribute“weight”:   Partition the data using equal width partitioning. . Number of intervals = 3. Normalize the weight = 34 using min-max method (min=1, max=2)'
# tx = tx.translate({ord(i): '' for i in '—-:;'})
# # tx = ['What', 'Motivated', 'data', 'Mining']
# doc = gensim.utils.simple_preprocess(tx)
# print(doc)

processed_docs = preprocess(tx)

#Converting text to bag of words
dictionary = gensim.corpora.Dictionary(processed_docs)

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

print(bow_corpus)
