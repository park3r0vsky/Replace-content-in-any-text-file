import in_place
import pandas as pd

all_data = pd.read_excel(r'DataFile.xlsx')
file_toEdit = 'file_toEdit.cpp'

column1 = pd.DataFrame(all_data, columns= ['ENGLISH'])
column2 = pd.DataFrame(all_data, columns= ['POLISH'])

eng_list = column1['ENGLISH'].tolist()
pol_list = column2['POLISH'].tolist()

list_lenght = len(pol_list)

for number in range(list_lenght):
    text_original = '\"%s\"' % (eng_list[number])
    text_new = '\"%s\"' % (pol_list[number])
    with in_place.InPlace(file_toEdit) as file:
        for line in file:
            line = line.replace(text_original, text_new)
            file.write(line)
