from json import loads


def http_status_checker(fn):
    def wrapper(*args, **kwargs):
        try:
            res = fn(*args, **kwargs)
            if res.status_code >= 400:
                return False, res.resone
            return True, res.content
        except:
            return "failed to execute the request method"

    return wrapper