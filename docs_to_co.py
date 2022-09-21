import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        # print(para.text)
        fullText.append(para.text)
    return '\n'.join(fullText), fullText

doc, dlist = getText("T1.docx")
# print(doc)
# print(dlist[0])
# print(dlist)
dict = {}
# print(type(dict))
# print(len(dlist[5]))
flag = 0   # for checking whether the previous was the question or not
ques = ''
co = ''
for eachl in dlist:
    if len(eachl) == 0:
        continue

    if eachl[0] == 'Q':
        co = eachl.split('[')[1][:3]
        if co in dict.keys():
            prevstr = dict[co]
            curstr = eachl.split(']')[2]
            joinstr = prevstr + ' ' + curstr
            dict[co] = joinstr
            continue
        dict[co] = eachl.split(']')[2]
        flag = 1
    elif flag == 1:
        prevstr = dict[co]
        curstr = eachl
        joinstr = prevstr + ' ' + curstr
        dict[co] = joinstr

for key,ele in dict.items():
    print(key, ' : ', ele)
