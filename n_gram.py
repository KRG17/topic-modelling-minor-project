import re
from nltk.util import ngrams
from qpaper_preprocessing import qp_pre

def ng(filename):
    ques = qp_pre(filename)
    out = []
    for tokens in ques:
        # print("New ques")
        # print(tokens)
        output = list(ngrams(tokens, 2))
        for i in range(len(output)):
            output[i] = list(output[i])
            # print(output[i])
            output[i] = ' '.join(output[i])
        # print(output)
        out.append(output)
    return out

if __name__ == "__main__":
    output = ng("T1.docx")
    # print()
    # print(output)
    # print()
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
