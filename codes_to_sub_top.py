# import pandas as pd
from docx import Document

def prepro(txt):


document = Document('codesx.docx')
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


dict_subt_top = {}
for dict in data:
    co = dict['Co’s']
    sub = dict["Subtitle of the Module"]
    topics = dict["Topics in the module"]
    if len(topics) == 0:
        continue
    dict_subt_top[sub] = topics

print(dict_subt_top)

