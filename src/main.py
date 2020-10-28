import os

import requests
from dotenv import load_dotenv

import data.mongo_service as mongo_service
import data.mongo_setup as mongo_setup


def main():
    load_dotenv()
    print("Running program")
    mongo_setup.global_init()

    fetch_alcohols()


def fetch_alcohols():
    page = 1
    alcohols = list()
    api_base_url = os.getenv('API_BASE_URL')
    api_key = os.getenv('API_KEY')
    headers = {'ocp-apim-subscription-key': api_key}

    while page > 0:
        try:
            print('Fetching alcohols from page {}'.format(page))
            r = requests.get(api_base_url +
                             'productsearch/search?page=%a' % page, headers=headers)

            if r.status_code == 200:
                data = r.json()

                if len(data['products']) > 0:
                    alcohols.extend(data['products'])
                    page += 1
                else:
                    page = -1

            else:
                print('Request failed with error {}: {}'.format(
                    r.status_code, r.json()))
                page = -1
        except Exception as e:
            print('Request failed: {}'.format(e))
            page = -1

    mongo_service.insert_documents(alcohols)


main()
