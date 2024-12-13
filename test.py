import pandas as pd
df = pd.read_csv('C:/Users/Arshpreet/Desktop/dataproject.csv', delimiter=',',header=0)
#df = df.rename(columns={' race ': 'category'})
#print(df)
#race_count = df.category.value_counts().tolist()
#print(race_count)
#df = df.rename(columns={' sex  ': 'sex'})
#print(df.columns)
#print(df.sex)
#avg_age=round((df[df.sex=="female"].age.mean()),1)
#print(avg_age)
#print(df.age.mean())
df=df.rename(columns={'education ':'education'})
#print(df)
#print(df.education)
#per= round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)
#print("per is",per)
#print(df.columns)
df=df.rename(columns={'salary ':'salary'})
#higher_education =  df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
#lower_education =  df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
#print(df.salary)
#higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50k']) / len(higher_education) * 100, 1)
#lower_education_rich =round(len(lower_education[lower_education['salary'] == '>50k']) / len(lower_education) * 100, 1)
#print(higher_education_rich)
#print(lower_education_rich)
df=df.rename(columns={' hours-per-week':"hoursperweek"})
#print(df)
#print(df.hoursperweek)
min_work_hours = df['hoursperweek'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = len(df[df['hoursperweek'] == min_work_hours])
rich_percentage = round(len(df[(df['hoursperweek'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers * 100, 1)
print(rich_percentage)
print(df.columns)
df=df.rename(columns={' native-country  ':"nativecountry"})
print(df)
country=len(df[df['nativecountry'] == '>50k'])
print(country)
percountry=round(len(country[country['salary'] == '>50k']) / len(country) * 100, 1)
print(percountry)