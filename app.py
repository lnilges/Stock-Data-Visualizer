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
#import pygal 
#import lxml

#Use base link and use inputs below to fill in function, symbol, and interval values
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=9XOMX3XJU9HQH6LD'
#r = requests.get(url)
#data = r.json()

#print(data)

#put everything in a while loop so it can run again if user wants different data??
print('Stock Data Visualizer\n--------------------')

while(True):

    #ask user for stock symbol
    #need to check to make sure the symbol is valid
    stockSymbol = None
    while(True):
        stockSymbol = input('\nEnter the stock symbol you are looking for: ')
        break


    chartChoice = None
    #Ask user for the chart type
    while(True):
        print('\nChart types\n----------------')
        print('1. Bar')
        print('2. Line')
        try: 
            chartChoice= int(input("\nEnter the chart type you want (1, 2): "))
            if(chartChoice == 1 or chartChoice == 2):
                break
            else:
                print("Enter a 1 or 2 for chart type")
        except ValueError:
            print("Enter a 1 or 2 for chart type")
            

    url = None
    #Ask user for the time series function they want the api to use
    while(True):
        print('\nSelect the Time Series of the chart you want to generate\n----------------------------------------------------------')
        print('1. Intraday')
        print('2. Daily')
        print('3. Weekly')
        print('4. Monthly')
        try: 
            timeSeriesChoice = int(input('\nEnter time series option (1, 2, 3, 4): '))
            if(timeSeriesChoice == 1):
                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stockSymbol}&RANGE={startDate}&RANGE={endDate}&interval=5min&apikey=9XOMX3XJU9HQH6LD'
                break
            elif(timeSeriesChoice == 2):
                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockSymbol}&RANGE={startDate}&RANGE={endDate}&apikey=9XOMX3XJU9HQH6LD'
                break
            elif(timeSeriesChoice == 3):
                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stockSymbol}&RANGE={startDate}&RANGE={endDate}&apikey=9XOMX3XJU9HQH6LD'
                break
            elif(timeSeriesChoice == 4):
                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={stockSymbol}&RANGE={startDate}&RANGE={endDate}&apikey=9XOMX3XJU9HQH6LD'
                break
            else:
                print("Enter a 1, 2, 3, or 4 for time series")
        except ValueError:
            print("Enter a 1, 2, 3, or 4 for time series")


    #r = requests.get(url)
    #testData = r.json()
    #print(testData)

    #Ask user for the start date
    #make sure end date is after start date
    #need to move part with links below this or ask for start/end date within the same while loop
    startDate = None
    while(True):
        startDate = input('\nEnter the start date (YYYY-MM-DD): ')
        break


    #Ask user for the end date, make sure it is not before the start date(datetime??)
    endDate = None
    while(True):
        endDate = input('\nEnter the end date (YYYY-MM-DD): ')
        break


    #generate the graph

    #line chart
    #split the data from the website into lines (open, high, low, and close) and then add each to the chart 
    #pygal basic line chart
    #line_chart = pygal.Line()
    #line_chart.title = f'Stock data for {stockSymbol}'
    #line_chart.x_labels = map(str, range(int(startDate[:4]), int(endDate[:4])))
    #line_chart.add('name', [data])
    #line_chart.render()

    #bar chart

    #ask user if they want to look up more information



