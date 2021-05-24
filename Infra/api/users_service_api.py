# from email import header
import requests
from data.configuration import api_config
from services.http_status_checker import http_status_checker


class UsersServicesApi():
    def __init__(self) -> None:
        self.url = api_config.users_url

    @http_status_checker
    def get_users(self, *args):
        url = self.url
        if args:
            url += f'/{args[0]}'
        return requests.get(url=url)

    @http_status_checker
    def post_user(self, *args, **kwargs):
        return requests.post(url=self.url, headers=kwargs)

    @http_status_checker
    def edit_user(self, id, *args, **kwargs):
        url = self.url
        url += f'/{id}'
        return requests.put(url=url, headers=kwargs)

    @http_status_checker
    def delete_user(self, id, *args, **kwargs):
        url = self.url
        url += f'/{id}'
        return requests.put(url=url)


resp = UsersServicesApi()
print(resp.get_users())
print(resp.post_user(**{}))
print(resp.get_users(1))
print(resp.post_user(íd=None, name=''))
print(resp.delete_user(None))
# print(resp.post_user(name='n'.encode(), íd=333))
# for new_user in api_config.users_to_add:
#     print(resp.post_user(**new_user))
