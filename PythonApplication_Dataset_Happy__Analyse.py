import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data2015 = pd.read_csv('2015.csv')
data2016 = pd.read_csv('2016.csv')
data2017_ = pd.read_csv('2017.csv')
data2018_ = pd.read_csv('2018.csv')
data2019_ = pd.read_csv('2019.csv')

#1. Added a 'year' column into each dataset 
data2015['year'] = '2015'
data2016['year'] = '2016'
data2017_['year'] = '2017'
data2018_['year'] = '2018'
data2019_['year'] = '2019'

pd.to_datetime(data2015.year)
pd.to_datetime(data2016.year)
pd.to_datetime(data2017_.year)
pd.to_datetime(data2018_.year)
pd.to_datetime(data2019_.year)


# 2. Identified the columns that were relvant for my analysis, and present in all five datasets. Any column that was not relevant or not in all five datasets was dropped. 
columns_to_drop2015 = [
    'Region', 'Standard Error', 'Dystopia Residual'
]

columns_to_drop2016 = [
    'Region', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia Residual'
]

columns_to_drop2017 = [
    'Whisker.high', 'Whisker.low', 'Dystopia.Residual'
]

#no cols to drop for 2018 and 2019
data2015.drop(columns_to_drop2015, axis='columns', inplace=True)
data2016.drop(columns_to_drop2016, axis='columns', inplace=True)
data2017_.drop(columns_to_drop2017, axis='columns', inplace=True)

#3. Reorded the columns in all five data sets to ensure all columns were in the same order
data2017 = data2017_.iloc[:, [0,1,2,3,4,5,6,8,7,9]]
data2018 = data2018_.iloc[:, [1,0,2,3,4,5,6,8,7,9]]
data2019 = data2019_.iloc[:, [1,0,2,3,4,5,6,8,7,9]]

#4. Standardized the naming conventions of the coumns across all five data sets
data2015 = data2015.rename(columns={'Country': 'country', 'Happiness Rank': 'happiness_rank', 'Happiness Score': 'happiness_score', 'Economy (GDP per Capita)': 'GDP_per_capita', \
                                    'Family': 'social_support', 'Health (Life Expectancy)' : 'healthy_life_expectancy', 'Freedom': 'freedom', \
                                    'Trust (Government Corruption)': 'absence_of_corruption', 'Generosity': 'generosity'})

data2016 = data2016.rename(columns={'Country': 'country', 'Happiness Rank': 'happiness_rank', 'Happiness Score': 'happiness_score', 'Economy (GDP per Capita)': 'GDP_per_capita', \
                                    'Family': 'social_support', 'Health (Life Expectancy)' : 'healthy_life_expectancy', 'Freedom': 'freedom', \
                                    'Trust (Government Corruption)': 'absence_of_corruption', 'Generosity': 'generosity'})

data2017 = data2017.rename(columns={'Country': 'country', 'Happiness.Rank': 'happiness_rank', 'Happiness.Score': 'happiness_score', 'Economy..GDP.per.Capita.': 'GDP_per_capita', \
                                    'Family': 'social_support', 'Health..Life.Expectancy.' : 'healthy_life_expectancy', 'Freedom': 'freedom', \
                                    'Trust..Government.Corruption.': 'absence_of_corruption', 'Generosity': 'generosity'})

data2018 = data2018.rename(columns={'Country or region': 'country', 'Overall rank': 'happiness_rank', 'Score': 'happiness_score', 'GDP per capita': 'GDP_per_capita', \
                                    'Social support': 'social_support', 'Healthy life expectancy' : 'healthy_life_expectancy', 'Freedom to make life choices': 'freedom', \
                                    'Perceptions of corruption': 'absence_of_corruption', 'Generosity': 'generosity'})

data2019 = data2019.rename(columns={'Country or region': 'country', 'Overall rank': 'happiness_rank', 'Score': 'happiness_score', 'GDP per capita': 'GDP_per_capita', \
                                    'Social support': 'social_support', 'Healthy life expectancy' : 'healthy_life_expectancy', 'Freedom to make life choices': 'freedom', \
                                    'Perceptions of corruption': 'absence_of_corruption', 'Generosity': 'generosity'})

#5. Combined the five datasets into one
combined_data = pd.concat([data2015, data2016, data2017, data2018, data2019])
combined_data.head()

#Check for null values, determined that there is one null in the perceptions_of_corruption column
#print('combined_data:', combined_data.isnull().sum())

#Rrint all Data
print(data2019)
print(data2018)
print(data2017)
print(data2016)
print(data2015)

#Analysis
#Question 1

#1
x = combined_data['happiness_score']
y = combined_data['GDP_per_capita']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.xlabel("happiness_score")
plt.ylabel("GDP_per_capita")

plt.show()

#1 Claster
#c = combined_data['GDP_per_capita']
#s = combined_data['happiness_score']
#plt.scatter(x,y)
#if s < 50 :
 #   plt.plot(x,p(x),"g+")
#if s > 49 :
 #   plt.plot(x,p(x),"y+")
#plt.show()

#2
x = combined_data['happiness_score']
y = combined_data['social_support']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.xlabel("happiness_score")
plt.ylabel("social_support")

plt.show()

#3
x = combined_data['happiness_score']
y = combined_data['healthy_life_expectancy']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.xlabel("happiness_score")
plt.ylabel("healthy_life_expectancy")

plt.show()

#4
x = combined_data['happiness_score']
y = combined_data['freedom']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.xlabel("happiness_score")
plt.ylabel("freedom")

plt.show()

#5
x = combined_data['happiness_score']
y = combined_data['absence_of_corruption']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.xlabel("happiness_score")
plt.ylabel("absence_of_corruption")

plt.show()

#6 
x = combined_data['happiness_score']
y = combined_data['generosity']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.xlabel("happiness_score")
plt.ylabel("generosity")

plt.show()

#Question 2
#Find the average happiness scores of all countries grouped by year
happiness_score_by_year = combined_data.groupby(['year'])
happiness_score_by_year = happiness_score_by_year.mean()
happiness_score_by_year = pd.DataFrame(happiness_score_by_year,columns=['happiness_score'])
print (happiness_score_by_year)

#Plot the happiness scores of all countries grouped by year
happiness_score_by_year.plot();
plt.show()