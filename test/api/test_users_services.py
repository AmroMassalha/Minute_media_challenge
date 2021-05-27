import ast
from data.configuration import api_config
from Infra.api.users_service_api import ProductsServicesApi
from services.utils import check_list_items, generate_random_str_or_num, check_strings_in_dict

resp = ProductsServicesApi()


def test_check_the_created_procut_BUG_1():
    """[the name of the product is hardcoded table]
    """
    user_ = generate_random_str_or_num()
    id_ = generate_random_str_or_num(1)
    relatedProducts_ = [{'test': 'test1'}]

    resp.post_product(name=user_, id=id_, relatedProducts=relatedProducts_)

    check_user_exist = resp.get_products()
    for item in ast.literal_eval(check_user_exist[1].decode("utf-8")):
        rc = check_strings_in_dict(item, user_)
        if rc:
            break
    assert (rc == True)


def test_check_the_created_procut_BUG_2():
    """[ID must be integer, was taken as str]
    """
    user_: str = generate_random_str_or_num()
    id_: int = generate_random_str_or_num()
    relatedProducts_ = [{'test': 'test1'}]

    create_rc = resp.post_product(name=user_,
                                  id=id_,
                                  relatedProducts=relatedProducts_)
    assert create_rc[0] == False


def test_get_all_users():
    get_user_rc = resp.get_products()
    assert len(ast.literal_eval(get_user_rc[1].decode("utf-8"))) >= 0


def test_edit_user():
    user_ = generate_random_str_or_num()
    id_ = generate_random_str_or_num(1)
    resp.post_product(name=user_, id=id_)
    assert (resp.edit_product(id=id_, name='newName'))[0] == True


def test_delete_user_BUG_3():
    """[Delete request not working]
    """
    user_ = generate_random_str_or_num()
    id_ = generate_random_str_or_num(1)
    resp.post_product(name=user_, id=id_)
    assert (resp.delete_product(id=id_))[0] == True
