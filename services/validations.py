def check_list_items(list_of_dicts: list, str: str) -> bool:
    for item in list_of_dicts:
        if isinstance(item, dict):
            for k, v in item.items():
                if str in v:
                    return True, v
                else:
                    return False
        return False