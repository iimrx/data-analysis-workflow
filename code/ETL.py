try:
    import os,time
    import pandas as pd
except Exception as e:
    print(f"error while importing packages! \n\n{e}")

try:
    #import datasets direct from github url(raw data)
    startExtracting = time.time() #starting time of Extracting data from github repo
    url  = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    data = pd.read_csv(url) #transfaring data to pandas dataframe
    endExtracting = time.time() #ending time of the Extracting proccess
    print(f'Time to Extract Data: {round(endExtracting-startExtracting,2)} sec')
except Exception as e: #if the proccess of Extracting the data didn't work, will print error message
    print(f'Error while Extracting data!\n\n{e}')

try:
    #extracting needed countries and making some data manipulation to handle null values
    data = data.loc[data['location']=='Saudi Arabia'] # extracting saudi arabia only data
    data.fillna(0, inplace=True) #replacing data after we checked to be zeros which means(not recorded)
    #~60 columns is to much and not all of them are needed,
    #so we gonna only take needed data columns to a new file and stay with it
    data = data[['iso_code','continent','location','date','total_cases','new_cases',
                'total_deaths','new_deaths','icu_patients','new_tests','total_tests',
                'positive_rate','total_vaccinations','people_vaccinated','people_fully_vaccinated',
                'new_vaccinations','population','median_age','aged_65_older','aged_70_older',
                'female_smokers','male_smokers','human_development_index'
                ]]
    #rechanging date column name
    data = data.rename(columns={'iso_code':'countries_code','continent':'region','location':'countries','people_fully_vaccinated':'fully_vaccinated','people_vaccinated':'vaccinated','total_vaccinations':'vaccinations'})
    #lets change date column to date type rather than object
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%d-%m-%y')
except Exception as e: #if the wrangling proccess didn't work, will print error message
    print(f'Error while wrangling the data!\n\n{e}')

try:
    #now lets save our new dataset to its path,
    #checking if the folder exists to overright or create new
    data.to_csv('./datasets/created/ksa.csv', index=False)
    print('Dataset File Saved!')
except: #if the file not exists well create new file
    save_loc = './datasets/created/ksa.csv' #path to the file
    if not os.path.exists(save_loc): #checking for the file
        os.mkdir(save_loc) #if not create new
    ksa.to_csv('./datasets/created/ksa.csv', index=False) #save
