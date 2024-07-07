import requests
import math
import time

from Secrets.api_keys import TWELVE_API_KEY


#collects financial data from twelve data api
def get_stock_data(stock): 
    url = f"https://api.twelvedata.com/quote?symbol={stock}&apikey={TWELVE_API_KEY}"

    try:
        with requests.get(url) as response:

            print('grabbed instance')

            # check for invalid stock ticker user input
            try:
                message = response.json()['message']
                print(message)
                if "**symbol** parameter is missing or invalid" in message:
                    return 'invalid_stock'
            except:
                return response.json()
            
    
    except Exception as e:
        print("Error instance stock data :", e)
        
def get_stock_graph(stock, output_size=80): 
    url = f"https://api.twelvedata.com/time_series?symbol={stock}&interval=5min&outputsize={output_size}&apikey={TWELVE_API_KEY}"

    try:
        with requests.get(url) as response:
            print('grabbed graph')
            return response.json()
    
    except Exception as e:
        print("Error stock graph data:", e)

def package_stock_data(stock):
    stock_instance = get_stock_data(stock=stock)

    # kill the function if invalid user input
    if stock_instance == 'invalid_stock':
        return 'invalid_stock'

    stockGraphData = get_stock_graph(stock=stock)

    # update if the market is open
    is_market_open = stock_instance['is_market_open']

    # convert JSON strings to floats and 
    price_displayed = round(float(stock_instance['close']), 2)
    percent_change = round(float(stock_instance['percent_change']), 2)
    price_change = round(float(stock_instance['change']), 2)

    # calculate graph parameters
    stockGraphData = stockGraphData['values'][:64][::-1]

    #filter out quotes from previous day
    for index, quote in enumerate(stockGraphData):
        if "09:30:00" in quote['datetime']:
            stockGraphData = stockGraphData[index:]
            break

    # deturmine x-axis height by ratio of day in red
    quote_in_red = 1
    for quote in stockGraphData:
        quote_in_red += 1 if (quote['close']) < (stock_instance['previous_close']) else 0
    x_axis_height = math.ceil(31 - 16*(quote_in_red / len(stockGraphData))) 

    # find the range of stock price for the day
    high_dif = x_axis_height - 15
    high_dif = 1 if high_dif == 0 else high_dif
    low_dif = 31 - x_axis_height
    low_dif = 1 if low_dif == 0 else low_dif

    # establish a unit of measurement for each individual pixel 
    try:
        high_unit_measurement = (float(stock_instance['high']) - float(stock_instance['previous_close'])) / high_dif
    except ZeroDivisionError:
        high_unit_measurement = None
    try:
        low_unit_measurement = (float(stock_instance['previous_close']) - float(stock_instance['low'])) / low_dif
    except ZeroDivisionError:
        low_unit_measurement = None

    # deturmine x value offset for text
    stock_ticker_len = len(stock_instance['symbol'])
    percent_change_len = len(f"{percent_change:.2f}")
    price_change_len = len(f"{price_change:.2f}")

    # deturmine x value offset for triangle indicator
    triangle_x_offset = 2 + (stock_ticker_len*3) + stock_ticker_len
    for l in stock_instance['symbol']:
        triangle_x_offset += 1 if l == "N" or l == "H" or l == "O" or l == "G" else 0
        triangle_x_offset += 2 if l == "W" or l == "M" else 0

    data = {
        "stock_instance":stock_instance,
        "triangle_x_offset":triangle_x_offset,
        "price_displayed":price_displayed,
        "price_change_len":price_change_len,
        "price_change":price_change,
        "percent_change_len":percent_change_len,
        "percent_change":percent_change,
        "stockGraphData":stockGraphData,
        "x_axis_height":x_axis_height,
        "high_unit_measurement":high_unit_measurement,
        "low_unit_measurement":low_unit_measurement,
        "is_market_open":is_market_open
    }

    return data

# if market is closed print appropriate wait time
def market_data_sleep_mode():
    current_time = time.localtime()

    time_dict = {
    'hour': current_time.tm_hour,
    'minute': current_time.tm_min,
    'day_of_week': current_time.tm_wday  
    }

    hour = time_dict['hour']
    minute = time_dict['minute']
    day_of_week = time_dict['day_of_week']

    # if a weekend sleep for 4 hours
    if day_of_week == 5 or day_of_week == 6:
        print(f"Sleeping: It's the weekend")
        
        return True

    # time check after market close 
    elif hour >= 16:
        seconds_to_sleep = 60 * ((((24 * 60) - ((hour * 60) + minute)) + (9.5 * 60))) 
        print_hours = int((seconds_to_sleep / 60) / 60)  
        print_minutes = int((seconds_to_sleep / 60) % 60)
        print(f"Sleeping: {print_hours} hours and {print_minutes} minutes till next market open")
        
        return True
    
    # time check before market open
    elif hour <= 9.5:
        seconds_to_sleep = 60 * (((9.5 * 60) - ((hour * 60) + minute)))
        print_hours = int((seconds_to_sleep / 60) / 60)  
        print_minutes = int((seconds_to_sleep / 60) % 60)
        print(f"Sleeping: {print_hours} hours and {print_minutes} minutes till next market open")
        
        return True
    
    return False