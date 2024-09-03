import numpy as np
import pandas as pd
ci= pd.read_csv('/adult.data.csv')

race = ci['race'].value_counts()
print(race)

men=ci[ci['sex']=='Male']
avg_age=round(men['age'].mean(),1)
print("Average age of Men :",avg_age)

bd=(ci['education']=="Bachelors").value_counts()
print("Percentage Of Bachelors Degree :",round(bd[True]/bd.sum()*100),"%")


highedu=ci[ci['education'].isin(["Bachelors" , "Masters" , "Doctorate" ])]
lowedu=ci[~ci['education'].isin(["Bachelors" , "Masters" , "Doctorate" ])]
high_mrtan50=(highedu[highedu['salary']==">50K"])
low_mrtan50=(lowedu[lowedu['salary']==">50K"])
print("Percentage of people with advanced education make more than 50K : ",round(len(high_mrtan50)/len(highedu)*100),"%")
print("Percentage of people without advanced education make more than 50K : ",round(len(low_mrtan50)/len(lowedu)*100),"%")

min_work=ci["hours-per-week"].min()
print("Minimum Number Of Hours A Person Works Per Week :",min_work)

#sample=(ci[ci['education'].isin(["Bachelors" and "Masters"])]) + (ci[ci['education'].isin(["Doctorate"])]) + (ci[ci['education'].isin(["Masters"])]) + (ci[ci['education'].isin(["Bachelors"])]) + (ci[ci['education'].isin(["Bachelors" and "Doctorate"])]) + (ci[ci['education'].isin(["Masters" and "Doctorate"])])

min_work=ci[ci['hours-per-week']==min_work] 
min_work_rich=(min_work[min_work['salary']=='>50K'])
print("Percentage Of People Who Work Minimum Hours And Make More Than 50K : ",round(len(min_work_rich)/len(min_work)*100),"%")

rich_salary_country=ci[ci['salary']=='>50K']
maxim=rich_salary_country["native-country"].value_counts()
print(maxim.index[maxim.argmax()],"has the highest percentage of people that earn >50K and the percentage is",round(maxim.max()/len(rich_salary_country)*100),"%")

high_salary_India= ci[(ci['salary'] == ">50K") & (ci['native-country'] == "India")]['occupation'].value_counts()
top_in_work= high_salary_India_occ.idxmax()
print("Top Occupation in India of above 50k is : ",top_in_work)

