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

#Used to test to make sure API key worked
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=9XOMX3XJU9HQH6LD'
#r = requests.get(url)
#data = r.json()
#print(data)

#put everything in a while loop so it can run again if user wants different data??
print('Stock Data Visualizer\n--------------------')

#ask the user for the stock symbol
def get_stock_symbol():
    while(True):
        while(True):
            stock_symbol = input('\nEnter the stock symbol you are looking for: ')
            return stock_symbol

#Ask user for the chart type
def get_chart_choice():
    while(True):
        print('\nChart types\n----------------')
        print('1. Bar')
        print('2. Line')
        try: 
            chart_choice= int(input("\nEnter the chart type you want (1, 2): "))
            if(chart_choice == 1 or chart_choice == 2):
                return chart_choice
            else:
                print("Enter a 1 or 2 for chart type")
        except ValueError:
            print("Enter a 1 or 2 for chart type")

#Ask user for the time series function they want the api to use           
def get_time_series():
    while(True):
        print('\nSelect the Time Series of the chart you want to generate\n----------------------------------------------------------')
        print('1. Intraday')
        print('2. Daily')
        print('3. Weekly')
        print('4. Monthly')
        try: 
            time_series_choice = int(input('\nEnter time series option (1, 2, 3, 4): '))
            if(time_series_choice == 1 or time_series_choice == 2 or time_series_choice == 3 or time_series_choice == 4):
                return time_series_choice
            else:
                print("Enter a 1, 2, 3, or 4 for time series")
        except ValueError:
            print("Enter a 1, 2, 3, or 4 for time series")


#Ask user for the start date
#make sure end date is after start date
def get_start_date():
    start_date = None
    while(True):
        start_date = str(input('\nEnter the start date (YYYY-MM-DD): '))
        return start_date

#ask the user for the end date
def get_end_date():
    #Ask user for the end date, make sure it is not before the start date(datetime??)
    while(True):
        end_date = input('\nEnter the end date (YYYY-MM-DD): ')
        return end_date
    
#creates bar chart
def bar_chart(start_date, end_date, data):
    #bar chart - basic strucutre from pygal website
    #bar_chart = pygal.Bar()
    #bar_chart.title = f`Stock data for {stock_symbol}`
    #bar_chart.x_labels = map(str, range(start_date[:4]), int(end_date[:4]))
    #bar_chart.add('name', [data])
    #bar_chart.render_in_browser() #should use lxml to render chart in broswer
    return

#creates line chart
def line_chart(start_date, end_date, data):
    #line chart - basic structure from pygal website
    #split the data from the website into lines (open, high, low, and close) and then add each to the chart 
    #line_chart = pygal.Line()
    #line_chart.title = f'Stock data for {stockSymbol}'
    #line_chart.x_labels = map(str, range(int(startDate[:4]), int(endDate[:4])))
    #line_chart.add('name', [data])
    #line_chart.render_in_browser() #should use lxml to render chart in broswer
    return

def main():
    while(True):
        stock_symbol = get_stock_symbol()
        chart_choice = get_chart_choice()
        time_series_choice = get_time_series()
        start_date = get_start_date()
        end_date = get_end_date()

        #sets the url based on the times series chosen by user
        if(time_series_choice == 1):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey=9XOMX3XJU9HQH6LD'
        elif(time_series_choice == 2):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey=9XOMX3XJU9HQH6LD'
        elif(time_series_choice == 3):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_symbol}&apikey=9XOMX3XJU9HQH6LD'
        elif(time_series_choice == 4):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={stock_symbol}&apikey=9XOMX3XJU9HQH6LD'

        #gets the data using the API key
        r = requests.get(url)
        data = r.json()
        print(data)

        #sends that data to the functions to build the chart (also included start/end dates but not sure if we need them)
        if(chart_choice == 1):
            bar_chart(start_date, end_date, data)
        elif(chart_choice == 2):
            line_chart(start_date, end_date, data)

        makeAnother = input("Would you like to view mire stock data? Press 'y' to continue: ")
        if(makeAnother == 'y'):
            continue
        else:
            print("Thank you and Goodbye!")
            break




main()

#What we still need to do:
    #make sure user enters a valid stock symbol
    #make sure end date is not before start date
    #once we get the data from the API, use start and end date to limit dataset
    #create chart using pygal 
    #display chart using lmxl