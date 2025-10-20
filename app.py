#This is the file to create our application

#requirements
#--------------
    #Ask the user to enter the stock symbol for the company they want data for.
    #Ask the user for the chart type they would like.
    #Ask the user for the time series function they want the api to use.
    #Ask the user for the beginning date in YYYY-MM-DD format.
    #Ask the user for the end date in YYYY-MM-DD format.
        #The end date should not be before the begin date
    #Generate a graph and open in the user’s default browser.

#API key: 9XOMX3XJU9HQH6LD

import requests

#Use base link and use inputs below to fill in function, symbol, and interval values
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=9XOMX3XJU9HQH6LD'
r = requests.get(url)
data = r.json()

print(data)

print('Stock Data Visualizer\n--------------------')

#ask user for stock symbol
stockSymbol = input('\nEnter the stock symbol you are looking for: ')


#Ask user for the chart type
print('\nChart types\n----------------')
print('1. Bar')
print('2. Line')
chartChoice= int(input("\nEnter the chart type you want (1, 2): "))


#Ask user for the time series function they want the api to use
print('\nSelect the Time Series of the chart you want to generate\n----------------------------------------------------------')
print('1. Intraday')
print('2. Daily')
print('3. Weekly')
print('4. Monthly')
timeSeriesChoice = int(input('\nEnter time series option (1, 2, 3, 4): '))


#Ask user for the start date
startDate = input('\nEnter the start date (YYYY-MM-DD): ')

#Ask user for the end date, make sure it is not before the start date(datetime??)
endDate = input('\nEnter the end date (YYYY-MM-DD): ')

#generate the graph

