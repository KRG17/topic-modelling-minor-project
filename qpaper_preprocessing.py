import gensim
from nltk.stem import WordNetLemmatizer
from docs_to_ques import dict
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

# print("\n")
prepro_data = []
for key,ele in dict.items():
    prepro_data.append(pp(ele))

if __name__ == "__main__":
    print(prepro_data)