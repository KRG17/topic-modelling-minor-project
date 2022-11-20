# importing libraries
import pandas as pd
import numpy as np
import gensim
from gsdmm import MovieGroupProcess
from qpaper_preprocessing import qp_pre

docs = qp_pre("T1.docx")
# df = pd.DataFrame(pre_data)

# cast tweets to numpy array
# docs = df.tweet_text.to_numpy()

# create dictionary of all words in all documents
dictionary = gensim.corpora.Dictionary(docs)
# print(dictionary)
# print(len(docs[0]) + len(docs[1]) + len(docs[2]) + len(docs[3]) + len(docs[4]))

# filter extreme cases out of dictionary
# dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

# create variable containing length of dictionary/vocab
vocab_length = len(dictionary)
# print(vocab_length)

# create BOW dictionary
bow_corpus = [dictionary.doc2bow(doc) for doc in docs]
# print(bow_corpus)

# initialize GSDMM
gsdmm = MovieGroupProcess(K=10, alpha=0.1, beta=0.3, n_iters=10)
# print(gsdmm)

# fit GSDMM model
y = gsdmm.fit(docs, vocab_length)
# print(y)

# print number of documents per topic
doc_count = np.array(gsdmm.cluster_doc_count)
# print(gsdmm.cluster_doc_count)
print('Number of documents per topic :', doc_count)

# Topics sorted by the number of document they are allocated to
top_index = doc_count.argsort()[-15:][::-1]
# print(doc_count.argsort())
print('Most important clusters (by number of docs inside):', top_index)

# define function to get top words per topic
for_wcloud = []
def top_words(cluster_word_distribution, top_cluster, values):
    for cluster in top_cluster:
        sort_dicts = sorted(cluster_word_distribution[cluster].items(), key=lambda k: k[1], reverse=True)[:values]
        sort_dicts = dict(sort_dicts)
        sum = 0
        for ky in sort_dicts:
            sum += sort_dicts[ky]
        for ky in sort_dicts:
            sort_dicts[ky] /= sum
            sort_dicts[ky] = round(sort_dicts[ky], 2)

        if len(sort_dicts) == 0:
            continue
        for_wcloud.append(sort_dicts)
        print("\nCluster %s : %s"%(cluster, sort_dicts))

# get top words in topics
top_words(gsdmm.cluster_word_distribution, top_index, 8)
# print(gsdmm.cluster_word_distribution)