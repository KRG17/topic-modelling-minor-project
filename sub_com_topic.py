from qpaper_preprocessing import qp_pre
from codes_to_sub_top import ext_cod

# print(qs)
# print(cd)

def com_sub(filename, codesx):
    common_words = []
    matched_subtitles = []
    qs = qp_pre(filename)
    cd = ext_cod(codesx)
    for q in qs:
        for words in q:
            for sub,top in cd.items():
                if words in top:
                    common_words.append(words)
                    # print(words)
                    # matched_subtitles.append(sub)

    remc = []
    [remc.append(x) for x in common_words if x not in remc]
    # print(remc)

    for words in remc:
        for sub, top in cd.items():
            if words in top:
                matched_subtitles.append(sub)
                break

    res = []
    [res.append(x) for x in matched_subtitles if x not in res]
    return remc, res

if __name__ == "__main__":
    # print(matched_subtitles)
    remc, res = com_sub("T1.docx", "codesx.docx")
    print(remc)
    print(res)