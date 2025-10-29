#Stock data visualizer
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
import datetime
import pygal 
import lxml

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
        user_start_date = str(input('\nEnter the start date (YYYY-MM-DD): '))
        try:
            #turns into datetime format
            start_date = datetime.datetime.strptime(user_start_date, '%Y-%m-%d').date()
            return start_date
        #gives error if not in correct format
        except ValueError:
            print("Invalid date format, use YYYY-MM-DD")

#ask the user for the end date
def get_end_date(start_date):
    #Ask user for the end date, make sure it is not before the start date
    while(True):
        user_end_date = input('\nEnter the end date (YYYY-MM-DD): ')
        try:
            #turns into datetime format
            end_date = datetime.datetime.strptime(user_end_date, '%Y-%m-%d').date()
            #makes sure end date is after start date and gives error if not
            if end_date >= start_date:
                return end_date
            else:
                print("End date must be after start date.")
        #gives error if not in correct format
        except ValueError:
            print("Invalid date format, use YYYY-MM-DD")
    
#creates bar chart
def bar_chart(start_date, end_date, data):
    #Checks API for data availablity from given values and grabs data from API
    key = next((k for k in data.keys() if "Time Series" in k), None)
    if not key:
        print("No valid time series data found.")
        return
    #Assigns data to time_series 
    time_series = data[key]
    # Filter data between start_date and end_date
    filtered_data = {}
    for date_str, values in time_series.items():
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if start_date <= date_obj <= end_date:
                filtered_data[date_obj] = float(values['4. close'])
        except:
            continue
    if not filtered_data:
        print("No data in the selected range.")
        return
    # Sort by date
    filtered_data = dict(sorted(filtered_data.items()))
    # Create a bar chart
    chart = pygal.Bar()
    chart.title = "Stock Closing Prices"
    chart.x_labels = [d.strftime('%Y-%m-%d') for d in filtered_data.keys()]
    chart.add("Closing Values", list(filtered_data.values()))
    chart.render_in_browser()

#creates line chart (Same code just for line chart)
def line_chart(start_date, end_date, data):
    #Checks API for data availablity from given values and grabs data from API
    key = next((k for k in data.keys() if "Time Series" in k), None)
    if not key:
        print("No valid time series data found.")
        return
    #Assigns data to time_series 
    time_series = data[key]
    # Filter data between start_date and end_date
    filtered_data = {}
    for date_str, values in time_series.items():
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if start_date <= date_obj <= end_date:
                filtered_data[date_obj] = float(values['4. close'])
        except:
            continue
    if not filtered_data:
        print("No data in the selected range.")
        return
    # Sort by date
    filtered_data = dict(sorted(filtered_data.items()))
    # Create a bar chart
    chart = pygal.Line()
    chart.title = "Stock Closing Prices"
    chart.x_labels = [d.strftime('%Y-%m-%d') for d in filtered_data.keys()]
    chart.add("Closing Values", list(filtered_data.values()))
    chart.render_in_browser()

#main function to contain while loop and functions to get information from user
def main():
    while(True):
        stock_symbol = get_stock_symbol()
        chart_choice = get_chart_choice()
        time_series_choice = get_time_series()
        start_date = get_start_date()
        end_date = get_end_date(start_date)

        #sets the url based on the times series chosen by user
        if(time_series_choice == 1):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey=9XOMX3XJU9HQH6LD'
        elif(time_series_choice == 2):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey=9XOMX3XJU9HQH6LD'
        elif(time_series_choice == 3):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_symbol}&apikey=9XOMX3XJU9HQH6LD'
        elif(time_series_choice == 4):
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock_symbol}&apikey=9XOMX3XJU9HQH6LD'

        #gets the data using the API key
        r = requests.get(url)
        data = r.json()
        #print(data)

        #sends that data to the functions to build the chart (also included start/end dates but not sure if we need them)
        if(chart_choice == 1):
            bar_chart(start_date, end_date, data)
        elif(chart_choice == 2):
            line_chart(start_date, end_date, data)

        makeAnother = input("Would you like to view more stock data? Press 'y' to continue: ")
        if(makeAnother == 'y'):
            continue
        else:
            print("Thank you and Goodbye!")
            break




main()
