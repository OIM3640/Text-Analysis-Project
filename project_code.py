import requests
import nltk
from newsapi import NewsApiClient
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer



# def get_moving_average(symbol, period, api_key):
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={api_key}'

#     response = requests.get(url)
#     data = response.json()['Time Series (Daily)']

#     # Extract the daily closing prices from the data for the specified period
#     closing_prices = []
#     for date in sorted(data.keys(), reverse=True)[:period]:
#         closing_prices.append(float(data[date]['4. close']))

#     # Calculate the moving average
#     moving_average = sum(closing_prices) / period

#     # Return the moving average
#     return moving_average

# symbol = 'SPY'
api_key_alpha_vantage = 'EZ62YSL0CTUD8S3O'

# moving_average_5 = get_moving_average(symbol, 5, api_key_alpha_vantage)
# print(f'Current 5-day moving average for {symbol} stock: {moving_average_5:.2f}')

# moving_average_8 = get_moving_average(symbol, 8, api_key_alpha_vantage)
# print(f'Current 8-day moving average for {symbol} stock: {moving_average_8:.2f}')

# moving_average_13 = get_moving_average(symbol, 13, api_key_alpha_vantage)
# print(f'Current 13-day moving average for {symbol} stock: {moving_average_13:.2f}')

# def get_ma_crossover_response(symbol, period, api_key):
#     # Get the moving averages
#     moving_average_5 = get_moving_average(symbol, 5, api_key)
#     moving_average_8 = get_moving_average(symbol, 8, api_key)
#     moving_average_13 = get_moving_average(symbol, 13, api_key)

#     # Determine the crossover direction
#     if moving_average_5 > moving_average_8 and moving_average_8 > moving_average_13:
#         response = f"{symbol} has a bullish crossover, with the 5-day moving average crossing above the 8-day moving average and the 8-day moving average crossing above the 13-day moving average."
#     elif moving_average_5 > moving_average_8 and moving_average_5 < moving_average_13:
#         response = f"{symbol} has a somewhat bullish signal, with the 5-day moving average above the 8-day moving average but not yet crossing over the 13-day moving average."
#     elif moving_average_5 < moving_average_8 and moving_average_8 < moving_average_13:
#         response = f"{symbol} has a bearish crossover, with the 5-day moving average crossing below the 8-day moving average and the 8-day moving average crossing below the 13-day moving average."
#     elif moving_average_5 < moving_average_8 and moving_average_5 > moving_average_13:
#         response = f"{symbol} has a somewhat bearish signal, with the 5-day moving average below the 8-day moving average but not yet crossing below the 13-day moving average."
#     else:
#         response = f"{symbol} does not have a clear crossover pattern."

#     return response



import requests

def get_last_12_months_cpi(api_key_alpha_vantage):
    url = f"https://www.alphavantage.co/query?function=CPI&apikey={api_key_alpha_vantage}"
    response = requests.get(url)
    response_json = response.json()
    cpi_data = response_json["data"]
    last_12_months_cpi = {}

    for i in range(12):
        month = cpi_data[i]["date"]
        cpi = float(cpi_data[i]["value"])
        last_12_months_cpi[month] = cpi

    return last_12_months_cpi

def analyze_inflation(last_12_months_cpi):
    cpi_values = list(last_12_months_cpi.values())
    last_month_cpi = cpi_values[0]
    last_year_cpi = cpi_values[-1]
    month_pct_change = (last_month_cpi - cpi_values[1]) / last_month_cpi * 100
    year_pct_change = (last_year_cpi - cpi_values[0]) / cpi_values[0] * 100

    message = ""
    if year_pct_change > 2:
        message += f"The yearly percentage change in seasonally adjusted inflation ({year_pct_change:.2f}%) is above the Federal Reserve's target of 2%, which may lead to potential need for interest rate increases that could hurt stock prices.\n"
        if month_pct_change > year_pct_change:
            message += f"Furthermore, the monthly percentage change in inflation ({month_pct_change:.2f}%) is increasing over the yearly rate, indicating that Fed action may be imminent."
        else:
            message += f"However, the monthly percentage change in inflation ({month_pct_change:.2f}%) is not increasing over the yearly rate at the moment."
    elif month_pct_change > year_pct_change:
        message += f"The monthly percentage change in seasonally adjusted inflation ({month_pct_change:.2f}%) is increasing, which may signal potential need for Federal Reserve action to prevent inflation from spiraling out of control."
    else:
        message += f"The monthly percentage change in seasonally adjusted inflation ({month_pct_change:.2f}%) is not increasing at the moment."

    if message:
        print(message)

    last_month_cpi = list(last_12_months_cpi.values())[0]
    last_year_cpi = list(last_12_months_cpi.values())[-1]
    month_pct_change = (last_month_cpi - list(last_12_months_cpi.values())[1]) / last_month_cpi * 100
    year_pct_change = (last_year_cpi - list(last_12_months_cpi.values())[0]) / list(last_12_months_cpi.values())[0] * 100

    message = ""
    if year_pct_change > 2:
        message += f"The yearly percentage change in seasonally adjusted inflation ({year_pct_change:.2f}%) is above the Federal Reserve's target of 2%, which may lead to potential need for interest rate increases that could hurt stock prices.\n"
        if month_pct_change > year_pct_change:
            message += "Furthermore, the monthly percentage change in inflation is increasing over the yearly rate, indicating that Fed action may be imminent."
    elif month_pct_change > year_pct_change:
        message += "The monthly percentage change in seasonally adjusted inflation is increasing, which may signal potential need for Federal Reserve action to prevent inflation from spiraling out of control."

    if message:
        print(message)

api_key_alpha_vantage = "your_alpha_vantage_api_key_here"
last_12_months_cpi = get_last_12_months_cpi(api_key_alpha_vantage)
analyze_inflation(last_12_months_cpi)



# def get_article_sentiment(query, source, api_key):
#     # initialize NLTK's Vader module
#     nltk.download('vader_lexicon')

#     # initialize NewsApiClient with your API key
#     newsapi = NewsApiClient(api_key=api_key)

#     # set query parameters
#     language = 'en'

#     # get the latest article related to the query from the source
#     articles = newsapi.get_everything(q=query, sources=source, language=language)

#     # retrieve the URL of the first article in the response
#     url = articles['articles'][0]['url']

#     # create an Article object and download the article content
#     article = Article(url)
#     article.download()

#     # parse the article content and extract the main text
#     article.parse()
#     text = article.text

#     # perform sentiment analysis on the article text
#     analyzer = SentimentIntensityAnalyzer()
#     score = analyzer.polarity_scores(text)

#     # return the sentiment scores as a dictionary
#     return score


# api_key = 'a81a2f3a42104f77aa29a2cdd60a0623'



# import numpy as np

# def overall_market_sentiment(api_key):
#     # set the query terms
#     query_terms = ['stocks', 'cryptocurrency', 'federal reserve', 'gdp', 'trade', 'business', 'inflation', 'CPI','bonds','interest rates' ]

#     # set the news sources
#     sources = 'bbc-news,the-verge'

#     # initialize an empty list to store the sentiment scores
#     sentiment_scores = []

#     # loop through the query terms and get the sentiment score for each term
#     for term in query_terms:
#         score = get_article_sentiment(term, sources, api_key)
#         sentiment_scores.append(score['compound'])

#     # calculate the average sentiment score
#     avg_score = np.mean(sentiment_scores)

#     # return the average sentiment score
#     return avg_score

# def make_market_decision(avg_score): #replace invest with print statements with more detail.
#     if avg_score > 0.5:
#         return "Invest"
#     elif avg_score < -0.25:
#         return "Short"
#     else:
#         return "Hold"



