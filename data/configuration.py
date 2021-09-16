class Config(dict):
    def __setitem__(self, k, v) -> None:
        super().__setitem__(k, v)
        setattr(Config, k, v)


api_config = Config()
web_config = Config()

######################API#########################

api_config["prefix"] = "http://"
api_config["endpoint"] = "localhost"
api_config["port"] = 7000
api_config["headers"] = {'Content-Type': 'application/json'}
api_config[
    "base_url"] = f"{api_config.prefix}{api_config.endpoint}:{api_config.port}"
api_config["products_url"] = f"{api_config.base_url}/products"

######################WEB#########################

web_config["prefix"] = "https://"
web_config["endpoint"] = "90min"
web_config["postfix"] = ".com"
web_config[
    "base_url"] = f"{web_config.prefix}{web_config.endpoint}{web_config.postfix}"
web_config[
    "binary_location"] = "/Applications/Chrome.app/Contents/MacOS/Google Chrome"
web_config["executable_path"] = "/Users/amassalh/Downloads/chromedriver"



def test():
    print("hello")