import gensim
from nltk.stem import WordNetLemmatizer
from docs_to_ques import get_dict
# import nltk
# nltk.download('omw-1.4')
# nltk.download('wordnet')
def ls(text):
    return WordNetLemmatizer().lemmatize(text, pos='v')


# Tokenize and lemmatize
def pp(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(ls(token))

    return result

# print("\n")

def qp_pre(filename):
    prepro_data = []
    dict = get_dict(filename)
    for key,ele in dict.items():
        prepro_data.append(pp(ele))

    pre_with_no_dup = []

    for pre in prepro_data:
        res = []
        [res.append(x) for x in pre if x not in res]
        pre_with_no_dup.append(res)

    return prepro_data

if __name__ == "__main__":
    pre_data = qp_pre("1.docx")
    for pre in pre_data:
        print(pre)
