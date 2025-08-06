########## INSTRUCTIONS ##########
# 1. Only add or modify codes within the blocks enclosed with
#    ########## student's code ##########
#
#    ####################################
##################################


########## student's code ##########
# If you need to import any library, you may do it here
...
####################################

def student_details():
  ########## student's code ##########
  ##########    Task 1     ##########
  # 1. Update the name and id to your name and student id
  studentName = "..."
  studentId = "..."
  ####################################
  return studentName, studentId

def load_file():
  ########## student's code ##########
  ##########    Task 2     ##########
  # 1. load the csv file to be a pandas DataFrame with vairable name: "df"
  #    (note that the csv file has no header)
  #    add/set the headers of the columns (from left to right) to be
  #        cache, channelmin, channelmax, publishedperformance, estimatedperformance
  ...
  ####################################
  return df

def train_clustering_model(df):
  ########## student's code ##########
  ##########    Task 3     ##########  
  # 1. initialise a kmeans model with 5 clusters using variable name: "kmModel"
  # 2. train the kmeans model using the following columns from df
  #      publishedperformance, estimatedperformance
  ...
  ####################################
  return kmModel

def test_clustering_model(df, kmModel):
  ########## student's code ##########
  ##########    Task 4     ##########  
  # 1. use any 10 rows from df and identify/predict their clusters
  # 2. save the identified cluster index with variable name: "outcome"
  ...
  ####################################
  return outcome

def add_clustering_result_to_data(df, kmModel):
  ########## student's code ##########
  ##########    Task 5     ##########  
  # 1. predict the clusters of every row in df
  # 2. convert the cluster numbers (0,1,2,3,4,5) to alphabets (a,b,c,d,e)
  # 3. add the cluster outcome as a new column called "cresult"
  ...
  ####################################
  return df

def train_decision_tree(df):
  ########## student's code ##########
  ##########    Task 6     ##########  
  # 1. initialise a decision tree model with maximum depth of 5 as variable: dtModel
  # 2. train the decision tree model to classify based on inputs of
  #    a. channelmin    
  #    b. channelmax
  #    to identify the output of "estimatedperformance"
  ...
  ####################################
  return dtModel

def test_decision_tree(df, dtModel):
  ########## student's code ##########
  ##########    Task 7     ##########  
  # 1. predict the class using the trained decision tree
  # 2. add the predicted outcome as a new column called "dresult"
  ...
  ####################################
  return df

def save_to_file(df):
  ########## student's code ##########
  ##########    Task 8     ##########  
  # 1. save the dataframe "df" to a csv file with the name of "finalresults.csv"
  ...
  ####################################

if __name__ == "__main__": 
  print("Only add or modify codes within the blocks enclosed with")
  print("########## student's code ##########")
  print("")
  print("####################################")
  print("DO NOT REMOVE OR MODIFY CODES FROM OTHER SECTIONS")
  print("")

  sname,sid = student_details()
  print(f"You are {sname} with student ID {sid}")  

  
  ########## student's code ##########
  # you do not need to change the code of this section
  # but you may modify the code for debugging purpose
  df = load_file()
  kmModel = train_clustering_model(df)
  results = test_clustering_model(df, kmModel)
  df = add_clustering_result_to_data(df, kmModel)

  dtModel = train_decision_tree(df)
  df = test_decision_tree(df, dtModel)
  save_to_file(df)
  ####################################
