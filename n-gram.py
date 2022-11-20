import re
from nltk.util import ngrams
from qpaper_preprocessing import qp_pre

ques = qp_pre("T1.docx")
for tokens in ques:
    print("New ques")
    print(tokens)
    output = list(ngrams(tokens, 5))
    for i in output:
        print(i)
    print(len(output))
    print()
    print()

# s = "Natural-language processing (NLP) is an area of computer science " \
#     "and artificial intelligence concerned with the interactions " \
#     "between computers and human (natural) languages."
#
# s = s.lower()
# s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
# tokens = [token for token in s.split(" ") if token != ""]
# output = list(ngrams(tokens, 5))
# for i in output:
#     print(i)
# print(len(output))
