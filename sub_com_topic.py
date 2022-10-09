from qpaper_preprocessing import pre_with_no_dup as qs
from codes_to_sub_top import dict_subt_top as cd

# print(qs)
# print(cd)

common_words = []
matched_subtitles = []
for q in qs:
    for words in q:
        for sub,top in cd.items():
            if words in top:
                common_words.append(words)
                # print(words)
                # matched_subtitles.append(sub)

remc = []
[remc.append(x) for x in common_words if x not in remc]
print(remc)

for words in remc:
    for sub, top in cd.items():
        if words in top:
            matched_subtitles.append(sub)
            break



res = []
[res.append(x) for x in matched_subtitles if x not in res]

if __name__ == "__main__":
    # print(matched_subtitles)
    print(res)