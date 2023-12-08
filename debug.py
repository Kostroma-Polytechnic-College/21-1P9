import pandas as pd

remains_sheet = pd.read_excel(
    io='file.xlsx', 
    sheet_name='Остатки')
# print(remains_sheet)

discipline_sheet = pd.read_excel(
    io='file.xlsx', 
    sheet_name='Дисиплина')
# print(discipline_sheet)

teacher_sheet = pd.read_excel(
    io='file.xlsx', 
    sheet_name='Преподаватель')
# print(teacher_sheet)

group_sheet = pd.read_excel(
    io='file.xlsx', 
    sheet_name='Группа')
# print(group_sheet)

schedule = {}