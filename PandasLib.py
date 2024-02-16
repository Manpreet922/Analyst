import pandas as pd

Album_lis = {'Artist Name' :['Amrinder Gill','Diljit Dosanjh','Gippy Grewal','Amrinder Gill'],
             'Album Name' : ['Judaa','Born to Shine','Back to Basics','Judaa'],
             'Release Year' :[2000, 2001,2009,2000]}

df = pd.DataFrame(Album_lis)
#print(df)

# Column Selection, Slicing by Name
#print(df[['Release Year','Album Name','Artist Name']])
# Column Selection, Slicing by Position
#print(df[0:2])

# Accessing based on loc method, loc method works by label

#print(df.iloc[-1])

#Finding with unique method

#R_D = df['Artist Name'].unique()
#print(R_D)


#Adding Filters to dataframes

R_D = df['Artist Name'] == 'Amrinder Gill'
#print(R_D)

print(df.describe())

#df.to_csv('Sample_data.csv', index=False)