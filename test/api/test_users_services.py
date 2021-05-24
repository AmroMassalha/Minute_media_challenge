from data.configuration import api_config
from Infra.api.users_service_api import UsersServicesApi
from services.validations import check_list_items

resp = UsersServicesApi()


def test_add_user():
    user_ = 'user1'
    id_ = 1
    add_user_rc = resp.post_user(name=user_, íd=id_)
    check_user_exist = resp.get_users(id_)
    assert add_user_rc[0] == True
    assert (check_list_items(check_user_exist[1], id_))[0] == True


def test_add_bulk_users():
    for new_user in api_config.users_to_add:
        assert (resp.post_user(**new_user))[1] == True


def test_empty_add_user():
    add_user_rc = resp.post_user({})
    assert add_user_rc[0] == False


def test_get_all_users():
    get_user_rc = resp.get_users()
    for item in get_user_rc[1]:
        assert item != None


def test_edit_user():
    user_ = 'user1'
    id_ = 2
    resp.post_user(name=user_, íd=id_)
    assert (resp.edit_user(id=id_, name='newName'))[0] == True


def test_delete_user():
    user_ = 'user1'
    id_ = 3
    resp.post_user(name=user_, íd=id_)
    assert (resp.delete_user(id=id_))[0] == True
