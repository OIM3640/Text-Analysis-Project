
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key= '1c96463708304daeb5f74385c1327bd1')
api_key = '1c96463708304daeb5f74385c1327bd1'

def get_api_sources(country_code):
    sources_response = newsapi.get_sources(
                                           country= country_code)
    sources = sources_response['sources'] if 'sources' in sources_response else []

    # Print the details of each source
    for i, source in enumerate(sources):
        print(f"Source {i}:")
        print(f"ID: {source['id']}")
        print(f"Name: {source['name']}")
        print(f"Description: {source['description']}")
        print(f"URL: {source['url']}")
        print('-' * 100)
    else:
        print('no source')

# Call the function and print its results
def main():
    'runs the countries in get_api_sources functions'
    get_api_sources('us')
    get_api_sources('tr')
    get_api_sources('il')
    get_api_sources('sa')
    get_api_sources('eg')

if __name__ == '__main__':
    main()





