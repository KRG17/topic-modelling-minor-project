# import pandas as pd
from docx import Document

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
    return data
# directly making new dictionary in the form of CO:List of topics

def ext_cod(filename):
    data = ext_tab(filename)
    codict = {}
    for dict in data:
        co = dict['Co’s']
        if len(co) == 0:
            continue
        if co in codict.keys():
            prevstr = codict[co]
            curstr = dict['Topics in the module'].split(',')
            joinstr = prevstr + curstr
            codict[co] = joinstr
            continue
        codict[co] = dict['Topics in the module'].split(',')
    return codict

if __name__ == "__main__":
    codict = ext_cod('codesx.docx')
    for key,ele in codict.items():
        print(key, ' : ', ele)

# making new dictionary in the form of CO:List of topics

# codictlist = {}
# for key,ele in codict.items():
#     codictlist[key] = ele.split(',')
#     print(key, ' : ', codictlist[key])


