import pandas as pd
from scipy import stats

# Data gathered from "http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html"
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0] # header for the data frame
data_rows = data[1::]  # data from rows 1 until the end
df = pd.DataFrame(data_rows, columns=column_names)

# convert to float values
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alcohol_mean   = df['Alcohol'].mean() 
alcohol_median = df['Alcohol'].median() 
alcohol_mode   = stats.mode(df['Alcohol'])
alcohol_range  = df['Alcohol'].max() - df['Alcohol'].min()
alcohol_std    = df['Alcohol'].std() 
alcohol_var    = df['Alcohol'].var() 

tobaco_mean   = df['Tobacco'].mean() 
tobaco_median = df['Tobacco'].median() 
tobaco_mode   = stats.mode(df['Tobacco'])
tobaco_range  = df['Tobacco'].max() - df['Tobacco'].min()
tobaco_std    = df['Tobacco'].std() 
tobaco_var    = df['Tobacco'].var() 

print('\n')
print('The mean for the Alcohol in the dataset is ... ' + str(alcohol_mean) + '.')
print('The median for the Alcohol in the dataset is ... ' + str(alcohol_median) + '.')
print('The mode values for the Alcohol in the dataset are ...' + str(alcohol_mode[0]).strip('[]') + '.')
print('The range for the Alcohol in the dataset is ... ' + str(alcohol_range) + '.')
print('The standard deviation for the Alcohol in the dataset is ... ' + str(alcohol_std) + '.')
print('The varriance for the Alcohol in the dataset is ... ' + str(alcohol_var) + '.')

print('The mean for the Tobacco in the dataset is ... ' + str(tobaco_mean) + '.')
print('The median for the Tobacco in the dataset is ... ' + str(tobaco_median) + '.')
print('The mode values for the Tobacco in the dataset are ...' + str(tobaco_mode[0]).strip('[]') + '.')
print('The range for the Tobacco in the dataset is ... ' + str(tobaco_range) + '.')
print('The standard deviation for the Tobacco in the dataset is ... ' + str(tobaco_std) + '.')
print('The varriance for the Tobacco in the dataset is ... ' + str(tobaco_var) + '.')








