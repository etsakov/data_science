import pandas as pd

df = pd.read_csv('course1_downloads/olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

# df = df.drop('Totals')
# print(df)
# print(df.head())

# ---- Question 0
# What is the first country in df?
def answer_zero():
    return df.iloc[0]
print(answer_zero())


# ---- Question 1
# Which country has won the most gold medals in summer games?
print(len(df))
copy_df = df.copy()
print(len(copy_df))

only_gold = copy_df.where(copy_df['Gold'] > 0)
only_gold = only_gold.dropna()

only_gold['country'] = only_gold.index
only_gold = only_gold.set_index('Gold')

max_gold = only_gold.loc[max(only_gold.index), 'country']
print(max_gold)


# ---- Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
copy_df = df.copy()
copy_df['country'] = copy_df.index

copy_df['Gld Diff'] = copy_df['Gold'] - copy_df['Gold.1']
copy_df = copy_df.set_index('Gld Diff')

max_diff = copy_df.loc[max(copy_df.index), 'country']

print(max(copy_df.index))
print(max_diff)


# ---- Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
copy_df = df.copy()
only_gold = copy_df.where(copy_df['Gold.1'] > 0)
only_gold = only_gold.dropna()
only_gold = only_gold.where(copy_df['Gold'] > 0)
only_gold = only_gold.dropna()

only_gold['country'] = only_gold.index
only_gold['Relative Gold'] = (copy_df['Gold'] - copy_df['Gold.1']) / copy_df['Gold.2']
only_gold = only_gold.set_index('Relative Gold')

max_relative = only_gold.loc[max(only_gold.index), 'country']

print(only_gold)
print(max(only_gold.index))
print(max_relative)


# ---- Question 4
# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created.
Incorrectly, you returned a variable of type <class 'pandas.indexes.numeric.Int64Index'> 
We expected a type of <class 'pandas.core.series.Series'>. 0.125 points we not awarded.
copy_df = df.copy()
copy_df['Points'] =  copy_df['Gold.2'] * 3 + copy_df['Silver.2'] * 2 + copy_df['Bronze.2']

print(copy_df['Points'])