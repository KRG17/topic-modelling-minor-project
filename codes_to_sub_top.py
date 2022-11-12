# import pandas as pd
from docx import Document
import gensim
from nltk.stem import WordNetLemmatizer

def prepro(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(token)

    return result
def ext_tab(filename):
    document = Document(filename)
    table = document.tables[3]

    data = []

    keys = None
    for i, row in enumerate(table.rows):
        text = (cell.text for cell in row.cells)

        if i == 0:
            keys = tuple(text)
            continue
        row_data = dict(zip(keys, text))
        data.append(row_data)

    # print(data)
    return data

def ext_cod(filename):
    data = ext_tab(filename)
    dict_subt_top = {}
    for dict in data:
        co = dict['Co’s']
        if len(co) == 0:
            continue
        sub = dict["Subtitle of the Module"]
        topics = dict["Topics in the module"]
        if len(topics) == 0:
            continue
        topics = prepro(topics)
        res = []
        [res.append(x) for x in topics if x not in res]
        topics = res
        dict_subt_top[sub] = topics
    return dict_subt_top

if __name__ == "__main__":
    dict_subt_top = ext_cod("codesx.docx")
    print(dict_subt_top)


