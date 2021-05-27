import requests, json
from data.configuration import api_config
from services.http_status_checker import http_status_checker


class ProductsServicesApi():
    def __init__(self) -> None:
        self.url = api_config.products_url

    @http_status_checker
    def get_products(self, *args):
        url = self.url
        if args:
            url += f'/{args[0]}'
        return requests.get(url=url, headers=api_config.headers)

    @http_status_checker
    def post_product(self, *args, **kwargs):
        resp = requests.post(url=self.url,
                             headers=api_config.headers,
                             data=json.dumps(kwargs))
        return resp

    @http_status_checker
    def edit_product(self, id, *args, **kwargs):
        url = self.url
        url += f'/{id}'
        return requests.put(url=url,
                            headers=api_config.headers,
                            data=json.dumps(kwargs))

    @http_status_checker
    def delete_product(self, id, *args, **kwargs):
        url = self.url
        url += f'/{id}'
        return requests.put(url=url, headers=api_config.headers)