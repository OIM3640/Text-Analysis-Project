import requests
import nltk
from newsapi import NewsApiClient
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np


def get_moving_average(symbol, period, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={api_key}"

    response = requests.get(url)
    data = response.json()["Time Series (Daily)"]

    closing_prices = []
    for date in sorted(data.keys(), reverse=True)[:period]:
        closing_prices.append(float(data[date]["4. close"]))

    moving_average = sum(closing_prices) / period

    return moving_average


"""
get_moving_average(symbol, period, api_key):

This function retrieves the historical daily stock prices for a given symbol
from the Alpha Vantage API using the provided API key, extracts the closing prices
for the specified period (in days), calculates the simple moving average, and returns it as a floating-point number.

Inputs:

symbol: A string representing the stock symbol to retrieve data for.
period: An integer representing the number of days to calculate the moving average for.
api_key: A string representing the API key to authenticate the Alpha Vantage API requests with.
Output:

A floating-point number representing the moving average of the stock's closing prices for the specified period.
"""


def get_ma_crossover_response(symbol, period, api_key):

    moving_average_5 = get_moving_average(symbol, 5, api_key)
    moving_average_8 = get_moving_average(symbol, 8, api_key)
    moving_average_13 = get_moving_average(symbol, 13, api_key)

    if moving_average_5 > moving_average_8 and moving_average_8 > moving_average_13:
        response = f"{symbol} has a bullish crossover, with the 5-day moving average crossing above the 8-day moving average and the 8-day moving average crossing above the 13-day moving average."
    elif moving_average_5 > moving_average_8 and moving_average_5 < moving_average_13:
        response = f"{symbol} has a somewhat bullish signal, with the 5-day moving average above the 8-day moving average but not yet crossing over the 13-day moving average."
    elif moving_average_5 < moving_average_8 and moving_average_8 < moving_average_13:
        response = f"{symbol} has a bearish crossover, with the 5-day moving average crossing below the 8-day moving average and the 8-day moving average crossing below the 13-day moving average."
    elif moving_average_5 < moving_average_8 and moving_average_5 > moving_average_13:
        response = f"{symbol} has a somewhat bearish signal, with the 5-day moving average below the 8-day moving average but not yet crossing below the 13-day moving average."
    else:
        response = f"{symbol} does not have a clear crossover pattern."

    return response


"""
get_ma_crossover_response(symbol, period, api_key):

This function uses the get_moving_average() function to calculate the moving averages
for a given stock symbol and then determines the direction of the crossover between the moving averages.
It returns a string message indicating the direction of the crossover and the moving averages involved.

Inputs:

symbol: A string representing the stock symbol to retrieve data for.
period: An integer representing the number of days to calculate the moving averages for.
api_key: A string representing the API key to authenticate the Alpha Vantage API requests with.
Output:

A string message indicating the direction of the crossover and the moving averages involved.
"""


def get_last_12_months_cpi(api_key_alpha_vantage):
    url = (
        f"https://www.alphavantage.co/query?function=CPI&apikey={api_key_alpha_vantage}"
    )
    response = requests.get(url)
    response_json = response.json()
    cpi_data = response_json["data"]
    last_12_months_cpi = {}

    for i in range(12):
        month = cpi_data[i]["date"]
        cpi = float(cpi_data[i]["value"])
        last_12_months_cpi[month] = cpi

    return last_12_months_cpi


"""
get_last_12_months_cpi(api_key_alpha_vantage):

This function retrieves the Consumer Price Index (CPI) data for the last 12 months
from the Alpha Vantage API using the provided API key, parses the data into a dictionary 
where the keys are the months and the values are the CPI values, and returns the dictionary.

Inputs:

api_key_alpha_vantage: A string representing the API key to authenticate the Alpha Vantage API requests with.
Output:

A dictionary where the keys are the months and the values are the CPI values for the last 12 months.
"""


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
    month_pct_change = (
        (last_month_cpi - list(last_12_months_cpi.values())[1]) / last_month_cpi * 100
    )
    year_pct_change = (
        (last_year_cpi - list(last_12_months_cpi.values())[0])
        / list(last_12_months_cpi.values())[0]
        * 100
    )

    message = ""
    if year_pct_change > 2:
        message += f"The yearly percentage change in seasonally adjusted inflation ({year_pct_change:.2f}%) is above the Federal Reserve's target of 2%, which may lead to potential need for interest rate increases that could hurt stock prices.\n"
        if month_pct_change > year_pct_change:
            message += "Furthermore, the monthly percentage change in inflation is increasing over the yearly rate, indicating that Fed action may be imminent."
    elif month_pct_change > year_pct_change:
        message += "The monthly percentage change in seasonally adjusted inflation is increasing, which may signal potential need for Federal Reserve action to prevent inflation from spiraling out of control."

    if message:
        print(message)


"""
analyze_inflation(last_12_months_cpi):

This function analyzes the inflation trends over the last 12 months using the CPI data from
the provided dictionary. It calculates the percentage change in CPI for the last month and the last year,
determines if the yearly change is above the Federal Reserve's target of 2%, and returns a string message indicating the inflation trend.

Inputs:

last_12_months_cpi: A dictionary where the keys are the months and the values are the CPI values for the last 12 months.
Output:

A string message indicating the inflation trend over the last 12 months.
"""


def get_article_sentiment(query, source, api_key):

    nltk.download("vader_lexicon")

    newsapi = NewsApiClient(api_key=api_key)

    language = "en"

    articles = newsapi.get_everything(q=query, sources=source, language=language)

    url = articles["articles"][0]["url"]

    article = Article(url)
    article.download()

    article.parse()
    text = article.text

    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    return score


"""
get_article_sentiment(query, source, api_key):

This function retrieves the latest article from the given source related to the
provided query using the News API with the provided API key, performs sentiment analysis on the 
article text using the VADER (Valence Aware Dictionary and sEntiment Reasoner) 
module from NLTK (Natural Language Toolkit), and returns a dictionary with the sentiment scores.

Inputs:

query: A string representing the search query for the article.
source: A string representing the news source to retrieve the article from.
api_key: A string representing the API key to authenticate the News API requests with.
Output:

A dictionary containing the sentiment scores for the article text.
"""


def overall_market_sentiment(api_key):

    query_terms = [
        "stocks",
        "cryptocurrency",
        "federal reserve",
        "gdp",
        "trade",
        "business",
        "inflation",
        "CPI",
        "bonds",
        "interest rates",
    ]

    sources = "bbc-news,the-verge"

    sentiment_scores = []

    for term in query_terms:
        score = get_article_sentiment(term, sources, api_key)
        sentiment_scores.append(score["compound"])

    avg_score = np.mean(sentiment_scores)

    return avg_score


"""
overall_market_sentiment(api_key):

This function calculates the average sentiment score for a list of query terms related to the market
using the get_article_sentiment() function and returns the average score.

Inputs:

api_key: A string representing the API key to authenticate the News API requests with.
Output:

A floating-point number representing the average sentiment score for the market-related query terms.
"""


def make_market_decision(avg_score):
    if avg_score > 0.5:
        return "Based on the positive sentiment score, it might be a good idea to invest in the market at this time."
    elif avg_score < -0.25:
        return "Based on the negative sentiment score, it might be a good idea to consider shorting or exiting the market at this time."
    else:
        return "Based on the current sentiment score, it might be a good idea to hold off on investing for now until sentiment becomes more strongly positive or negative."


"""
make_market_decision(avg_score):

This function takes in the average sentiment score for the market-related query terms and returns a
string message with a market decision based on the score. If the score is above 0.5, the message recommends
investing in the market. If the score is below -0.25, the message recommends shorting or exiting the market. 
Otherwise, the message recommends holding off on investing until sentiment becomes more strongly positive or negative.

Inputs:

avg_score: A floating-point number representing the average sentiment score for the market-related query terms.
Output:

A string message with a market decision based on the sentiment score.
"""


def main():
    symbol = "SPY"
    api_key_alpha_vantage = "EZ62YSL0CTUD8S3O"

    api_key_newsapi = "a81a2f3a42104f77aa29a2cdd60a0623"
    avg_sentiment = overall_market_sentiment(api_key_newsapi)
    decision = make_market_decision(avg_sentiment)
    print(decision)

    crossover_response = get_ma_crossover_response(symbol, 5, api_key_alpha_vantage)
    print(crossover_response)

    last_12_months_cpi = get_last_12_months_cpi(api_key_alpha_vantage)
    analyze_inflation(last_12_months_cpi)


"""
main():

This function is the main function of the script. 
It calls the overall_market_sentiment(), make_market_decision(), get_ma_crossover_response(),
get_last_12_months_cpi(), and analyze_inflation() functions to retrieve and analyze market data, 
and prints out the resulting messages. It takes no inputs and returns no outputs
"""

if __name__ == "__main__":
    main()
