try:
    import os,time
    import pandas as pd
except Exception as e:
    print(f"error while importing packages! \n\n{e}")

try:
    #import datasets from data.gov.sa
    startExtracting = time.time() #starting time of Extracting data from github repo
    data = pd.read_csv('./datasets/created/seekers.csv') #transfaring data to pandas dataframe
    endExtracting = time.time() #ending time of the Extracting proccess
    print(f'Time to Extract Data: {round(endExtracting-startExtracting,2)} sec')
except Exception as e: #if the proccess of Extracting the data didn't work, will print error message
    print(f'Error while Extracting data!\n\n{e}')

try:
    data.drop(data.index[[0]], inplace=True)
    data.columns = ['id','gender','region','city','age','edu_degree','major','gpa','gpa_from','inistitute','inserted_date','grad_date','record_from']
    
    data.drop(['record_from','grad_date','inserted_date','gpa_from','gpa'], axis=1, inplace=True)
    data.fillna('لا يوجد',inplace=True)
except Exception as e: #if the wrangling proccess didn't work, will print error message
    print(f'Error while wrangling the data!\n\n{e}')

#checking if the folder exists to overwrite or create new
save_loc = './datasets/created/seekers.csv' #path to the file
if not os.path.exists(save_loc): #checking for the file
    os.mkdir(save_loc) #if not create new
#now lets save our new dataset to its path,
data.to_csv(save_loc, index=False) #save
print('Dataset File Saved!')
