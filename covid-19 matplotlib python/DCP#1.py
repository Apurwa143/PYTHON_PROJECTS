import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#--------------------------------Extracting China's DataSet--------------------
covid_data = pd.read_csv('covid-19.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Recovered'] - covid_data['Deaths']
np_data = np.array(covid_data)
china = [0, 0, 0, 0, 0, 0]
china = np.array(china)
for i in range(0, 15725):
    a = []
    b = []
    if(np_data[i][1]=="China"):
        for j in range(0, 6):
             a = np.array((np_data[i][j]))
             b = np.hstack((b, a))
        #print(b)
        china = np.vstack((china, b))
china = pd.DataFrame(china, columns=['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths', 'Active'])
china = china.drop(china.index[[0]])
#print(china)
#--------------------------------Extracting India's DataSet--------------------
india = [0, 0, 0, 0, 0, 0]
india = np.array(india)
for i in range(0, 15725):
    a = []
    b = []
    if(np_data[i][1]=="India"):
        for j in range(0, 6):
             a = np.array((np_data[i][j]))
             b = np.hstack((b, a))
        #print(b)
        india = np.vstack((india, b))

india = pd.DataFrame(india, columns=['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths', 'Active'])
india = india.drop(india.index[[0]])
#print(india)
#----------------------------------------------------------------------------
usa = [0, 0, 0, 0, 0, 0]
usa = np.array(usa)
for i in range(0, 15725):
    a = []
    b = []
    if(np_data[i][1]=="US"):
        for j in range(0, 6):
             a = np.array((np_data[i][j]))
             b = np.hstack((b, a))
        #print(b)
        usa = np.vstack((usa, b))
usa = pd.DataFrame(usa, columns=['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths', 'Active'])
usa = usa.drop(usa.index[[0]])
#print(china)
#------------------------------------------------------------------------------------------
spain = [0, 0, 0, 0, 0, 0]
spain = np.array(spain)
for i in range(0, 15725):
    a = []
    b = []
    if(np_data[i][1]=="Spain"):
        for j in range(0, 6):
             a = np.array((np_data[i][j]))
             b = np.hstack((b, a))
        #print(b)
        spain = np.vstack((spain, b))
spain = pd.DataFrame(spain, columns=['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths', 'Active'])
spain = spain.drop(spain.index[[0]])
#print(china)
#------------------------------------------------------------------------------------
italy = [0, 0, 0, 0, 0, 0]
italy = np.array(italy)
for i in range(0, 15725):
    a = []
    b = []
    if(np_data[i][1]=="Italy"):
        for j in range(0, 6):
             a = np.array((np_data[i][j]))
             b = np.hstack((b, a))
        #print(b)
        italy = np.vstack((italy, b))
italy = pd.DataFrame(italy, columns=['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths', 'Active'])
italy = italy.drop(italy.index[[0]])
#--------------------------------------------------------------------------------------
dat = pd.to_datetime(china['Date'])
ind = india['Confirmed'].astype(int)
chi = china['Confirmed'].astype(int)
us = usa['Confirmed'].astype(int)
it = italy['Confirmed'].astype(int)
spa = spain['Confirmed'].astype(int)
plt.figure(figsize=(150, 60))
plt.plot_date(india['Date'], ind, color='green', linestyle='solid', label="INDIA", marker=None)
plt.plot_date(india['Date'], chi, color='red', linestyle='solid', label="CHINA", marker=None)
plt.plot_date(india['Date'], spa, color='black', linestyle='solid', label="SPAIN", marker=None)
plt.plot_date(india['Date'], us, color='blue', linestyle='solid', label="USA", marker=None)
plt.plot_date(india['Date'], it, color='orange', linestyle='solid', label="ITALY", marker=None)
plt.legend(loc="upper left")
plt.xlabel('Date')
plt.ylabel('Values')
plt.grid()
plt.xticks(rotation=90, fontsize=8)
plt.title('COVID-19 confirmed cases of some countries')
plt.show()
