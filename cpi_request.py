import requests

api_key = 'EZ62YSL0CTUD8S3O'

def get_last_12_months_cpi(api_key):
    url = f"https://www.alphavantage.co/query?function=CPI&apikey={api_key}"
    response = requests.get(url)
    response_json = response.json()
    cpi_data = response_json["data"]
    last_12_months_cpi = {}

    for i in range(12):
        month = cpi_data[i]["date"]
        cpi = float(cpi_data[i]["value"])
        last_12_months_cpi[month] = cpi

    return last_12_months_cpi

last_12_months_cpi = get_last_12_months_cpi(api_key)
last_month_cpi = list(last_12_months_cpi.values())[0]
last_year_cpi = list(last_12_months_cpi.values())[-1]
month_pct_change = (last_month_cpi - list(last_12_months_cpi.values())[1]) / last_month_cpi * 100
year_pct_change = (last_year_cpi - list(last_12_months_cpi.values())[0]) / list(last_12_months_cpi.values())[0] * 100

print(f"The percentage change in seasonally adjusted inflation over the last month is {month_pct_change:.2f}%")
print(f"The percentage change in seasonally adjusted inflation over the last year is {year_pct_change:.2f}%")








