import requests

import data.mongo_service as mongo_service
import data.mongo_setup as mongo_setup


def main():
    print("Running program")
    mongo_setup.global_init()

    fetch_alcohols()


def fetch_alcohols():
    page = 1
    alcohols = list()
    api_key = '874f1ddde97d43f79d8a1b161a77ad31'

    headers = {'ocp-apim-subscription-key': api_key}

    while page > 0:
        try:
            print('Fetching alcohols from page {}'.format(page))
            r = requests.get(
                'https://api-extern.systembolaget.se/sb-api-ecommerce/v1/productsearch/search?page=%a' % page, headers=headers)

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
        except:
            print('Request failed')
            page = -1

    mongo_service.insert_documents(alcohols)


main()
