import pandas as pd
import numpy as np
data={ 'name':['rahul','kaviya','thariq','latha'],
       'age':[16,21,24,27],
       'salary':[50000,30000,46000,51500],
       'dep':['mech','cse','ece','it']
       }
df=pd.DataFrame(data)
print(df)

print('\ndescribe:')
print(df.describe())

print('\ninfo:')
print(df.info())

print('\nfirst row:')
print(df.head(2))

print('\nlast rows:')
print(df.tail(2))

print('\n filtered row:')
print(df['salary'])

print('\nin 2D:')
print(df[['salary','age']])

print('\n in fixed loc:')
print(df.loc[2])

print('\n in salary')
print(df.loc[0,'salary'])

print(df[2:])
print(df[:2])
print(df['salary'][2:])

print('\n in secific string index:')
print(df.iloc[1:3])

print('\n in salary:')
print(df.iloc[1,3])

print('\nfiltered data:')
print(df[df['dep']=='ece'])

print('\nfiltered data:')
print(df[df['salary']>45000])

print('\nlogical notation')
did=df[(df['salary']>50000) & (df['dep']=='it')]
print(df)

print('\nmin')
print(df['age'].mean())

print('\nmedian:')
print(df['age'].median())

print('\nsum:')
print(df['age'].sum())

print('\nstd:')
print(df['salary'].std())

print('\nsorting values:')
print(df.sort_values('age'))

print('\nsorting in dcending:')
print(df.sort_values('age',ascending=False))

print('\nchanging values:')
df['salary_euros']=df['salary']/96
print(df[['name','salary','salary_euros']])

def py(dep):
    if dep=='ece':
        return 1000
    elif dep=='cse':
        return 2000
    elif  dep=='cse':
        return 3000
    else:
        return 4000

df['updated']=df['dep'].apply(py)
print(df[['dep','salary','updated']])
