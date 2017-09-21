import pandas as pd

census_df = pd.read_csv('course1_downloads/census.csv')


# ---- Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.

copy_census_df = census_df.copy()
sumlev_2 = copy_census_df[copy_census_df['SUMLEV'] == 50]
columns_to_keep = ['STNAME', 'CTYNAME', 'COUNTY']
sumlev_2 = sumlev_2[columns_to_keep]
sumlev_2 = sumlev_2.set_index('STNAME')

states = list()
for i in sumlev_2.index:
    if i in states:
        pass
    else:
        states.append(i)

state_pop = dict()
for i in states:
    state_pop[i] = len(sumlev_2.loc[i])

max_state = max(state_pop, key=lambda k: state_pop[k])
print(max_state)


# ---- Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? 
# This function should return a list of string values.
copy_census_df = census_df.copy()
sumlev_2 = copy_census_df[copy_census_df['SUMLEV'] == 50]
sumlev_2 = sumlev_2.set_index(['STNAME', 'CENSUS2010POP'])

pop_dict = dict()
pop_list = list()
for i in sumlev_2.index.get_level_values(0):
    pop_dict[i] = sum(sumlev_2.loc[i].index.sort_values()[-3:])
    if sum(sumlev_2.loc[i].index.sort_values()[-3:]) in pop_list:
        pass
    else:
        pop_list.append(int(sum(sumlev_2.loc[i].index.sort_values()[-3:])))

top_three_pop = sorted(pop_list)[-3:]
top_three_state = []
for j in pop_dict.items():
    if j[1] in top_three_pop:
        top_three_state.append(j[0])
print(top_three_state)


# ---- Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# This function should return a single string value.
copy_census_df = census_df.copy()
sumlev_2 = copy_census_df[copy_census_df['SUMLEV'] == 50]

pop_list = ['POPESTIMATE2010',
               'POPESTIMATE2011',
               'POPESTIMATE2012',
               'POPESTIMATE2013',
               'POPESTIMATE2014',
               'POPESTIMATE2015']

pop_dict = dict()
for i in sumlev_2.index:
    pop_dict[sumlev_2.loc[i]['CTYNAME']] = max(sumlev_2.loc[i][pop_list]) - min(sumlev_2.loc[i][pop_list])

max_diff_cnty = max(pop_dict, key=lambda k: pop_dict[k])
print(max_diff_cnty)


# ---- Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
copy_census_df = census_df.copy()

sumlev_2 = copy_census_df[copy_census_df['SUMLEV'] == 50]
reg_df = sumlev_2[sumlev_2['REGION'] != 3]
reg_df = reg_df[reg_df['REGION'] != 4]
reg_df = reg_df[reg_df['POPESTIMATE2015'] > reg_df['POPESTIMATE2014']]
reg_df = reg_df[reg_df['CTYNAME'] == 'Washington County']
columns_to_keep = ['STNAME', 'CTYNAME']
reg_df = reg_df[columns_to_keep]

print(reg_df)
