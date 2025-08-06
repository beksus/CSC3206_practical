########## student's code ##########
# If you need to import any library, you may do it here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
####################################

def student_details():
  ########## student's code ##########
  ##########    Task 1     ##########
  # 1. Update the name and id to your name and student id
  studentName = "Beksutlan Kirgizbaev"
  studentId = "22078406"
  ####################################
  return studentName, studentId

def load_file():
  ########## student's code ##########
  ##########    Task 2     ##########
  # 1. load the csv file to be a pandas DataFrame with vairable name: "df"
  #    (note that the csv file has no header)
  #    add/set the headers of the columns (from left to right) to be
  #        cache, channelmin, channelmax, publishedperformance, estimatedperformance
  df = pd.read_csv("dataset.csv", header=None)
  df.columns = ["cache", "channelmin", "channelmax", "publishedperformance", "estimatedperformance"]
  ####################################
  return df

def train_clustering_model(df):
  ########## student's code ##########
  ##########    Task 3     ##########
  # 1. initialise a kmeans model with 5 clusters using variable name: "kmModel"
  # 2. train the kmeans model using the following columns from df
  #      publishedperformance, estimatedperformance
  from sklearn.cluster import KMeans
  kmModel = KMeans(n_clusters=5, random_state=42)
  kmModel.fit(df[["publishedperformance", "estimatedperformance"]])
  ####################################
  return kmModel

def test_clustering_model(df, kmModel):
  ########## student's code ##########
  ##########    Task 4     ##########
  # 1. use any 10 rows from df and identify/predict their clusters
  # 2. save the identified cluster index with variable name: "outcome"
  outcome = kmModel.predict(df[["publishedperformance", "estimatedperformance"]].head(10))
  ####################################
  return outcome

def add_clustering_result_to_data(df, kmModel):
  ########## student's code ##########
  ##########    Task 5     ##########
  # 1. predict the clusters of every row in df
  # 2. convert the cluster numbers (0,1,2,3,4,5) to alphabets (a,b,c,d,e)
  # 3. add the cluster outcome as a new column called "cresult"
  df['cresult'] = kmModel.predict(df[["publishedperformance", "estimatedperformance"]])
  df['cresult'] = df['cresult'].apply(lambda x: chr(x + ord('a')))
  ####################################
  return df

def train_decision_tree(df):
  ########## student's code ##########
  ##########    Task 6     ##########
  # 1. Import DecisionTreeClassifier from sklearn
  from sklearn.tree import DecisionTreeClassifier
  # 2. Initialise a decision tree model with maximum depth of 5
  dtModel = DecisionTreeClassifier(max_depth=5, random_state=42)
  # 3. Train the model using 'channelmin' and 'channelmax' as features, and 'estimatedperformance' as the target
  dtModel.fit(df[['channelmin', 'channelmax']], df['estimatedperformance'])
  ####################################
  return dtModel

def test_decision_tree(df, dtModel):
  ########## student's code ##########
  ##########    Task 7     ##########
  # 1. Predict the class using the trained decision tree for all rows
  predictions = dtModel.predict(df[['channelmin', 'channelmax']])
  # 2. Add the predicted outcome as a new column called "dresult"
  df['dresult'] = predictions.astype(str)
  ####################################
  return df

def save_to_file(df):
  ########## student's code ##########
  ##########    Task 8     ##########
  # 1. Save the dataframe "df" to a csv file with the name of "finalresults.csv"
  df.to_csv("finalresults.csv", index=False)
  ####################################