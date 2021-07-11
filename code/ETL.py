try:
    import os
    import pandas as pd
except Exception as e:
    print(f"error while importing packages! \n\n{e}")

#import datasets direct from github url(raw data)
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
data = pd.read_csv(url)

#extracting needed countries and making some data manipulation to handle null values
ksa = data.loc[data['location']=='Saudi Arabia'] # extracting saudi arabia only data
ksa.fillna(0, inplace=True) #replacing data after we checked to be zeros which means(not recorded)
#~60 columns is to much and not all of them are needed,
#so we gonna only take needed data columns to a new file and stay with it
ksa = ksa[['iso_code','continent','location','date','total_cases','new_cases',
            'total_deaths','new_deaths','icu_patients','new_tests','total_tests',
            'positive_rate','total_vaccinations','people_vaccinated','people_fully_vaccinated',
            'new_vaccinations','population','median_age','aged_65_older','aged_70_older',
            'female_smokers','male_smokers','human_development_index'
            ]]

#lets change date column to date type rather than object
ksa['date'] = pd.to_datetime(ksa['date'])

#now lets save our new dataset to its path,
#checking if the folder exists to overright or create new
try:
    ksa.to_csv('../datasets/created/ksa.csv', index=False)
except: #if the file not exists well create new file
    save_loc = '../datasets/created/ksa.csv' #path to the file
    if not os.path.exists(save_loc): #checking for the file
        os.mkdir(save_loc) #if not create new
    ksa.to_csv('../datasets/created/ksa.csv', index=False) #save