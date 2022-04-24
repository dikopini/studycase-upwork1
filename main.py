from bs4 import BeautifulSoup
import pandas as pd
import os

with open('data.xml','r') as f:
    data = f.read()

bs = BeautifulSoup(data, 'xml')
forms = bs.findAll('Form990PartVIISectionAGrp')

data = []
for form in forms:
    name = form.find('PersonNm').text
    #print(name)

    position = form.find('TitleTxt').text
    #print(position)

    income = form.find('AverageHoursPerWeekRt').text
    #print(income)

    dict_data={
        'name':name,
        'position':position,
        'income':income
    }
    data.append(dict_data)

try:
    os.mkdir('data_result')
except FileExistsError:
    pass
filename = 'data_final'
df = pd.DataFrame(data)
df.to_csv(f'data_result/{filename}.csv', index=False)