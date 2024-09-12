from pandas import read_csv
from numpy import nan
dataset = read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv', header=None)
dataset2 = dataset.iloc[:, 1:8] # removing column 1 and 9
find_na = dataset2[[1, 2, 3, 4, 5, 6, 7]] == 0 #finding 0 in the dataset, returns boolean value
dataset2[find_na] = nan #marking those 0 as nan