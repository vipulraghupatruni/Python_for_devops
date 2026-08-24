import requests  # import the requests library to make HTTP requests
API_KEY = "TP6CLTKW5MZYS9JM"

api_url = "https://www.alphavantage.co/"    #step 2 find a base url
#api_url ="https://www.alphavantage.co/" 


"query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

def get_stock_market_data(symbol):
# if is_timeseries:
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
# else:
 #   query = f"query?symbol={symbol}&apikey={API_KEY}"
    print(api_url+query)  # prints the complete URL with the API key
    
    response = requests.get(url=api_url+query)  # send a GET requestto the URL
    
    for key, value in response.json().items():  # iterate over the JSON response
        
        if key == "Time Series (Daily)":
           continue  # skip the "Time Series (Daily)" key
        else:
            print(key, ":", value)  # print each key-value pair
    
    #option2
    
    
    print(response.json())
    
    
    """
    if response.status_code == 200:  # check if the request was successful
        data = response.json()  # parse the JSON response
        print(data)  # print the data
    else:
        print("Error: ", response.status_code)  # print the error code if the request failed
        
        """


symbol = input("Enter the stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN): ")  # prompt the user to enter a stock symbol
is_timeseries = True
get_stock_market_data(symbol)  # call the function to get stock market data     
        
        