import os
from qpaper_preprocessing import qp_pre

def get_whole_data(folder):
    data = []
    print(os.getcwd())
    list_of_files = os.listdir(folder)
    print(list_of_files)
    os.chdir(folder)

    for files in list_of_files:
        if files == 'codesx.docx':
            continue
        pre_data = qp_pre(files)
        for ques in pre_data:
            data.append(ques)
    return data
if __name__ == "__main__":
    data = get_whole_data('Science')
    print(data)
