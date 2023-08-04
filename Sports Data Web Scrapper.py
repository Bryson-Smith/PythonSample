import time

from selenium import webdriver

#from bs4 import BeautifulSoup

 

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

#import csv

import pandas as pd

 

import matplotlib.pyplot as plt

import numpy as np

 

'''options = Options()

options.headless=True

options.add_argument("--window-size=1920,1200")

options=options,'''

 

driver = webdriver.chrome.webdriver.WebDriver( executable_path='chromedriver')  # Optional argument, if not specified will search path.

def go_to_site():

   

    StatsPage_url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'

    driver.get (StatsPage_url)

    time.sleep(5)# Let the user actually see something!

 

 

def get_league_data():

   

    DropDownPath= '//*[@id="all_stats_standard_squads"]/div[1]/div/ul/li[2]/span'

    DropDownHover = '//*[@id="all_stats_standard_squads"]/div[1]/div/ul/li[2]/div/ul/li[4]'

    #ButtonPath= '//*[@id="all_stats_standard_squads"]/div[1]/div/ul/li[1]/div/ul/li[4]/button'

   

    wait = WebDriverWait(driver, 10)

    action = webdriver.ActionChains(driver)

   

    

    DropDown = wait.until(EC.visibility_of_all_elements_located((By.XPATH,DropDownPath)))

    action.move_to_element(DropDown[0]).perform()

    DropDownList = wait.until(EC.visibility_of_all_elements_located((By.XPATH,DropDownHover)))

    #action.move_to_element(DropDownList[4]).click().perform()

    #print(DropDownList[0].text)

    DropDownList[0].click()

   

    

    '''DropDownButton = wait.until(EC.visibility_of_all_elements_located((By.XPATH,ButtonPath)))

    DropDownButton[0].click()

    DataButton =driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()

   

 

    DataButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'CSV')]")))

    DataButton.click()'''

   

    

    DataDrop = driver.find_element_by_xpath('//*[@id="csv_stats_standard_squads"]')

    DataSet= DataDrop.text

    DataSet= DataSet.replace('--- When using SR data, please cite us and provide a link and/or a mention.',"").strip()

    #print(DataSet)

    return DataSet

 

def save_csv():

    with open('Premier-League-Stats.csv', 'w') as csvfile:

        for line in DataSet:

            csvfile.write(line)

    driver.quit()

   

def read_clean_data():

    df= pd.read_csv('Premier-League-Stats.csv',sep=',',index_col=0)

    MainColumnName= df.columns

    SubColumnName = df.iloc[0]

    FullColumnName =[]

    for x in range(len(df.columns)):

        substring = 'Unnamed'

        #print(MainColumnName[x].isalpha())

        if substring in MainColumnName[x]:

            FullColumnName.append(SubColumnName[x])

        elif MainColumnName[x].isalpha():

            FullColumnName.append(MainColumnName[x] + '-'+SubColumnName[x])

        else:

            FullColumnName.append(MainColumnName[x][:-2] + '-'+SubColumnName[x])

    #print(FullColumnName[0])

       

    

    df.columns =FullColumnName

    df=df.drop(df.index[0])

    df=df.astype(float)

    return df

 

def Scatter(x,y):

    ax1.scatter(x,y,color='red')

   

    

def BarChart(x,y):

    ind= np.arange(len(SportsData))

    width= 0.8

   

    p1 = plt.bar(ind, x, width, color='r', label='Penalty Kick Attempts')

    p2 = plt.bar([i+0.25*width for i in ind], y, width = width*0.5,alpha=0.5, color='b',label= "Penalty Kick Made")

    plt.xticks(ind+width/2.5,

               ['T{}'.format(i) for i in range(len(SportsData))] )

    plt.show()

 

if __name__ == "__main__":

    go_to_site()

    DataSet = get_league_data()

    save_csv()

    SportsData = read_clean_data()

    #fig, axs = plt.subplots(2)

    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1)

   

    Scatter(x=SportsData['Poss'],y=SportsData['Performance-Gls'])

   

    print('''Main Idea: Goals Based on Success of passes

         

          Notes: After 45% of successful passes is when you see a noticeable  higher number of goals. ''')

    BarChart(x=SportsData["Performance-PKatt"],y=SportsData["Performance-PK"])