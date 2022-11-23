import gensim
from gensim import corpora
from qpaper_preprocessing import qp_pre

prepro_data = qp_pre("T1.docx")
dict_ = corpora.Dictionary(prepro_data)

# print(dict_)

# for i,j in dict_.items():
#     print(i, " ", j)
#
#
doc_term_matrix = [dict_.doc2bow(i) for i in prepro_data]
# print(doc_term_matrix)
#
Lda = gensim.models.ldamodel.LdaModel

ldamodel = Lda(doc_term_matrix, num_topics=6, id2word = dict_, passes=1, random_state=0, eval_every=None)

print(ldamodel.print_topics())

for i in ldamodel.print_topics(num_topics=len(prepro_data), num_words=5):
    print(i)

count = 0
for i in ldamodel[doc_term_matrix]:
    print("doc : ",count,i)
    count += 1

# lda_model =  gensim.models.LdaMulticore(doc_term_matrix, num_topics = 8, id2word = dict_, passes = 10, workers = 2)
# print(lda_model.print_topic())

topicwise_words = []
topics = ldamodel.show_topics(formatted=False)
print(topics)
# print(type(topics))

for i in range(len(topics)):
    topic_words = dict(topics[i][1])
    word = []
    for ky in topic_words:
        word.append(ky)
    topicwise_words.append(word)

print(topicwise_words)