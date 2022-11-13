import os
from sub_com_topic import com_sub
# word, topic = com_sub('T1.docx', 'codesx.docx')
# print(word)
# print(topic)

print(os.getcwd())
list_of_folders = os.listdir('Tests')
print(list_of_folders)
os.chdir('Tests')

for fold in list_of_folders:
    files = os.listdir(fold)
    print(files)
    os.chdir(fold)
    for each_file in files:
        if each_file == 'codesx.docx':
            continue
        print(each_file)
        word, topic = com_sub(each_file, 'codesx.docx')
        print(word)
        print(topic)
        print()
