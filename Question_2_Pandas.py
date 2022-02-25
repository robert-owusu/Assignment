# Importing Pandas
from pandas import *
options.display.width=0
set_option('display.max_rows',3000)
set_option('display.max_columns',3000)

# Question_2.A
# Creating_List
Stu_Names = ['Asare Samuel', 'James Quansah', 'Emmanuel Ayew', 'Sarpong Vannessa', 'Owusu Robert']
Stu_Col = ['Names']
# Creating_DataFrame from 1 to 5
students = DataFrame(data=Stu_Names, columns=Stu_Col, index=(range(1, 6)))
print(students)

# Question_2.B
# Creating_list
Names = ['Asante Kotoko', 'Hearts of Oak', 'Dreams F.C', 'Bechem United F.C']
Match1 = [2, 4, 4, 2]
Match2 = [2, 1, 3, 2]
Match3 = [4, 3, 3, 1]
Match4 = [3, 5, 6, 7]
Match5 = [2, 5, 8, 4]
# Creating_DataFrame
teams = DataFrame(data=[Match1] + [Match2] + [Match3] + [Match4] + [Match5], columns=Names,
                  index=('Match1', 'Match2', 'Match3', 'Match4', 'Match5'))
print(teams)

# Question_2.C
# Creating_Dictionary
West_African_Countries = {
    'Names': ['Ghana', 'Nigeria', 'Togo', 'Benin', 'Ivory Coast', 'Liberia', 'Senegal', 'Mali', 'Niger', 'Guinea'],
    'Capital': ['Accra', 'Abuja', 'Lome', 'Ouagadougou', 'Yamoussoukro', 'Monrovia', 'Dakar', 'Bamako', 'Niamey',
                'Conakry'],
    'Population': ["31 Million", '206 Million', '8 Million', '12 Million', '26 Million', '5 Million', '16 Million',
                   '20 Million', '24 Million', '13 Million']
}
# Creating_DataFrame from Index 1 to 10
countries = DataFrame(West_African_Countries, index=(range(1, 11)))
print(countries)

# Question_2.D
#Importing the Data
Football=read_csv("Team_Goals&Points.csv")

# Question_2.D(i)
#Team_Names,GA,GF,PTS
Football1=(Football[['Team','GF','GA','PTS']])
print(Football1)

#Question_2.D(ii,1)_Considered_more_than_30
print(Football1.loc[Football1.GA>30, :])

# Question_2.D(ii,2)_Goals_Scored_less than 80
print(Football1.loc[Football1.GF<80, :])

# Question_2.D(ii,3)_Points Less than 60
print(Football1.loc[Football1.PTS<60, :])







