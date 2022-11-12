"""This is for the LDA to let it decide what will be the topics from a string
collective of topics without comma"""
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
def ext_cod(filename):
    data = ext_tab(filename)
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
    return codict

if __name__ == "__main__":
    codict = ext_cod('codesx.docx')
    for key,ele in codict.items():
        # ele = ele.replace(',', '')
        ele = ele.translate({ord(i): None for i in ',?:;'})     # can use None or ''
        ele = ele.translate({ord(i): ' ' for i in '—-'})     # — and - are different
        print(key, ' : ', ele)