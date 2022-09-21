# import pandas as pd
from docx import Document

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
# df = pd.DataFrame(data)
# print(df)

codict = {}
for dict in data:
    # print(dict)
    co = dict['Co’s']
    if len(co) == 0:
        continue
    if co in codict.keys():
        prevstr = codict[co]
        curstr = dict['Topics in the module']
        joinstr = prevstr + ', ' + curstr
        codict[co] = joinstr
        continue
    codict[co] = dict['Topics in the module']

for key,ele in codict.items():
    print(key, ' : ', ele)



# print(table.rows)        # return object of row
# df = pd.DataFrame(data)
# print(df)

# import textract
# doc = textract.process("codes.doc")
# print(doc)
# antiword
