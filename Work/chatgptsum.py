from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="966d42a19bf042c68e6bec614e7e74c4")

topic = "svb"

data = newsapi.get_everything(
        q=topic,
        from_param="2023-03-23",
        to="2023-03-24",
        language="en",
        sort_by="relevancy",
        page=1,
    )

data = data["articles"]

d = []
for i in data:
    x = i.get("description")
    d.append(x)

d = " ".join(d)

print(d)


summarized = """There have been recent bank collapses and runs on deposits in the US, causing concern about the stability of the banking system. The CEOs of Silicon Valley Bank and Signature Bank have been called to testify before the US Senate panel. Federal Reserve Chair Jerome Powell admits that the regulator was blindsided by the sudden collapse of Silicon Valley Bank, which sparked a panic in the financial markets. However, Powell declares that the banking system is sound and resilient. There are concerns about the risk of further bank failures, and the House Republicans are demanding detailed information from the Biden Administration. Some blame the failures on the rollback of Dodd-Frank, but others point to the poorly designed regulatory framework and government backing as the ultimate culprit.
Silicon Valley Bank's collapse is causing instability in the global banking system, prompting investors to adjust to more challenging economic and lending conditions. The sudden fall of SVB left regulators stumped, and a paper analyzing more than 4,800 U.S. banks was conducted to determine their exposure to the risks that led to the failure of SVB. Billions of dollars in deposits poured into the nation's banking giants, and the government protected depositors. Startups are having a hard time finding funding in the private equity markets, but fortunately, non-dilutive capital is available from the government and Google. Some banks are considered "unsafe" in the crypto market, and banking shares slipped in Europe on Thursday. The Federal Reserve is weighing the risks of continued high inflation, and JPMorgan Chase & Co analysts estimate that the "most vulnerable" U.S. banks are likely to have lost a total of about $1 trillion in deposits since last year. Citigroup CEO Jane Fraser said that banking crises have happened before, but this may be the first one accelerated by mobile banking and social media."""