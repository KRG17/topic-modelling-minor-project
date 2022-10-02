import gensim
import nltk
from nltk.stem import WordNetLemmatizer
import nltk as stemmer
# from textmining import stemmer
# nltk.download('omw-1.4')
def ls(text):
    return WordNetLemmatizer().lemmatize(text, pos='v')


# Tokenize and lemmatize
def pp(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(ls(token))

    return result

tx = 'Consider the data for attribute“weight”:   Partition the data using equal width partitioning. . Number of intervals = 3. Normalize the weight = 34 using min-max method (min=1, max=2)'
# tx = tx.translate({ord(i): '' for i in '—-:;'})
# # tx = ['What', 'Motivated', 'data', 'Mining']
# doc = gensim.utils.simple_preprocess(tx)
# print(doc)

processed_docs = pp(tx)
print(processed_docs)