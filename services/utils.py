import random
import string


def check_list_items(list_of_dicts: list, str: str) -> bool:
    for item in list_of_dicts:
        if isinstance(item, dict):
            for k, v in item.items():
                if str in v:
                    return True, v
                else:
                    return False
        return False


def generate_random_str_or_num(typ="s"):
    if typ == "s":
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(4))
    elif typ != "n":
        letters = string.digits
        return ''.join(random.choice(letters) for i in range(4))


def check_strings_in_dict(dict_to_check: dict, string_to_check: str):
    for key, val in dict_to_check.items():
        if string_to_check in val:
            return True
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, dict):
                    rc = check_strings_in_dict(item, string_to_check)
                    if rc:
                        return True

    return False