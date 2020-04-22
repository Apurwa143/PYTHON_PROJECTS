'''state wise total number of confirmed cases and death cases till 24th march.'''

import pandas as pd
import matplotlib.pyplot as plt

covid_data = pd.read_csv('raw_covid.csv')
country = covid_data['Country']
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Recovered'] - covid_data['Deaths']
date = covid_data['Date']
r_data = covid_data.groupby(["Date"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
r_data = r_data.sort_values(by='Confirmed', ascending=True)


p_data = covid_data.groupby(["Country"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
p_data = p_data.sort_values(by='Confirmed', ascending=False)
p_data = p_data.head(40)
plt.figure(figsize=(150, 50))
#plt.barh(p_data['Country'], p_data['Confirmed'], color='green', label="Confirmed")
#plt.barh(p_data['Country'], p_data['Recovered'], color='blue', label="Recovered")
#plt.barh(p_data['Country'], p_data['Active'], color='black', label="Active")
#plt.legend(loc="upper right")
plt.xlabel('Values')
plt.ylabel('Country')
plt.title('COVID-19 --Total Confirmed, Recovered and Active Cases Country wise')


plt.figure(figsize=(150, 50))
plt.plot_date(r_data['Date'], r_data['Confirmed'], color='green', linestyle='solid', label="Confirmed")
plt.plot_date(r_data['Date'], r_data['Recovered'], color='red', linestyle='solid', label="Recovered")
plt.plot_date(r_data['Date'], r_data['Deaths'], color='blue', linestyle='solid', label="Deaths")
plt.plot_date(r_data['Date'], r_data['Active'], color='black', linestyle='solid', label="Active")
plt.legend(loc="upper left")
plt.xlabel('Date')
plt.ylabel('Values')
plt.xticks(rotation=90)
plt.title('COVID-19--Total Deaths, Confirmed, Recovered and Active Cases All Over The World')



top = covid_data.groupby(["Country"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
top = top.sort_values(by='Confirmed', ascending=False)
top = top.head(10)
#plt.bar(top['Country'], top['Confirmed'], color='red', label='Confirmed')
#plt.bar(top['Country'], top['Recovered'], color='blue', label='Recovered')
#plt.bar(top['Country'], top['Active'], color='green', label='Active')
#plt.bar(top['Country'], top['Deaths'], color='yellow', label='Deaths')
plt.legend(loc="upper right")
plt.xlabel('Country')
plt.ylabel('Values')
plt.xticks(rotation=90)
plt.title('COVID-19--Total Deaths, Confirmed, Recovered and Active Cases of Top 10 Country')
plt.show()