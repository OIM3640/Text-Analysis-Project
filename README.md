# Text-Analysis-Project
## **1. Project Overview**

For this project, I used a variety of different types of APIs not only because it made the project more interesting, but also because I thought it would help me learn	 more than if I had just used project gutenberg again. I initially tried to use wikipedia for information on CPI and stock market data, but I had trouble getting only the information I wanted to print. So instead I used Alpha Vantage API and the News API to analyze various economic news articles and data. Through the use of these APIs I extracted monthly CPI, closing stock market prices, and news articles related to the health of the economy for a given period of time. Using this information, I was able to conduct sentiment analysis of the news articles and calculate moving averages for the S&P 500 index. Taking these factors into account my program gives various suggestions on how to invest.


## **2. Implementation** 

When it comes to implementation, the project relies on API’s and data structures to retrieve and save financial information and news articles. As stated above, I used Alpha Vantage API for financial information and the News API for the articles .After the extraction process, the data is stored and processed in dictionaries and lists. For example, in the function get t_last_12_months_cpi, the data is stored in a dictionary, while the get_moving_average function uses lists.

I liked using the NLTK Vader sentiment analyzer due to its ability to easily analyze the sentiment of a given string. I see myself using this analyzer a lot in the future. I wish I had been able to analyze tweets, but my developer request is still under review. 

ChatGPT was a wonderful resource to use in this project. Whenever I came across a problem and really couldn't solve it after thinking it through, chatGPT was able to help me with the issue. When I used ChatGPT, it was primarily in the form of questions like “can you read this code and tell me what I am missing?” or “here is the error response given in the command prompt, what is going wrong with my code?”. ChaGPT was always very quick to help me find bugs and make my code better. I also used ChatGPT to organize my docstrings into a more organized format. Overall chatGPT was very helpful in giving me direction on what I was missing and gave very helpful suggestions on how best to improve my code.

I couldnt figure out how to upload supplement images using markedown format so I just included them as attached files in the repository.


## **3. Results**

For the past several years I have been trading alot in my free time. In order to be effective at trading I have found that it is extremely important to read the news and stay up to date on current events. For the past several months my general feeling of the market has been quite negative as we have seen several bank collapses and interest rates still increasing. When I decided to build this tool and gauge sentiment based on news articles, I expected the sentiment scores to be quite negative. Instead, what I found was that articles were more neutral or positive about the outlook on the economy. This was interesting to me because it showed me that I have a bias toward the negative when it comes to the market when maybe I shouldn't.

Another aspect of this project was implementing the Alpha Vantage API to extract closing price data.I have used moving averages to trade before, but generally the trading program I use calculates them for me automatically. I found the extraction and calculation process rewarding as it has helped me understand more about how trading algorithms work and their impact on the market. I now see many use cases for APIs in my everyday life.

Overall, the program provides market insights by combining multiple forms of analysis. For Example, the moving averages for a crossover analysis helps the user understand whether the S&P 500 is showing a bullish or bearish trend. Furthermore, In an inflationary time like we are in today monitoring changes in CPI becomes very important. The inflation analysis aspect of this program informs the user whether or not inflation is at concerning levels or accelerating. Finally, sentiment analysis provides a general overview of market sentiment which could give users a better understanding of whether or not experts and general sentiment think they should invest or divest. After running the program, I hope that  the user will have a good idea as to whether or not to invest, short, or hold stocks.


## **4. Reflection**

From a process perspective, the project went quite well. I struggled at times getting certain data in the correct format, but after time and pressure I was able to figure it out. Getting this project done took me much longer than I had expected, however I am proud of the work that I did.

I think there is always room for improvement when it comes to projects like this. If I had more time I would have liked to improve the sophistication of my sentiment analysis by building in more complex terms relating to finance that the sentiment analysis may not be weighing properly. Secondly I would like to incorporate more sophisticated algorithms for market analysis. By analyzing trends in volatility and volumes, I would have an even better understanding of where the market might be headed on any given day.

From a learning perspective, this project was fantastic. I feel like I have grasped the concepts of APIs and I see the many potential use cases for them in everyday life. ChatGPT was also an incredible learning tool and helped move along the process when I was stuck on a difficult concept. The knowledge gained from this exercise will be instrumental in further projects and will help me as I continue to build out this market analysis tool.

 
